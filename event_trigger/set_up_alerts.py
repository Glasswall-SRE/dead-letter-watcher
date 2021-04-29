import re
import json

from azure.mgmt.monitor import MonitorManagementClient
from azure.identity import DefaultAzureCredential
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import SubscriptionClient
from azure.mgmt.servicebus import ServiceBusManagementClient
from azure.servicebus.management import ServiceBusAdministrationClient
from secrets import get_secret

secrets = json.loads(get_secret())

APP_NAME = "dead-letter-watcher"
SHORT_APP_NAME = "dl-wtcr"

ENDPOINT = secrets["PULUMI"]["DEADLETTER_WATCHER_ENDPOINT"]

subscription_client = get_client_from_cli_profile(SubscriptionClient)

for sub in subscription_client.subscriptions.list():
    subscription_id = sub.subscription_id

    sb_client = ServiceBusManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=subscription_id
    )

    for sb in sb_client.namespaces.list():
        if sb.tags.get('group') == 'FileTrust':
            resource_id = sb.id
            resource_group_match = re.search('resourceGroups/(.*)/providers', sb.id)
            resource_group_name = resource_group_match.group(1)

            authorization_rule_keys = sb_client.namespaces.list_keys(resource_group_name=resource_group_name,
                                                   namespace_name=sb.name,
                                                   authorization_rule_name='RootManageSharedAccessKey')

            conn_str = authorization_rule_keys.primary_connection_string
            sb_admin_client = ServiceBusAdministrationClient.from_connection_string(conn_str)
            all_queues = [queue.name for queue in sb_admin_client.list_queues()]

            # create client
            monitor_client = MonitorManagementClient(
                DefaultAzureCredential(),
                subscription_id
            )

            # Create action group
            action_group = monitor_client.action_groups.create_or_update(
                resource_group_name,
                SHORT_APP_NAME,
                {
                    "location": "Global",
                    "group_short_name": SHORT_APP_NAME,
                    "enabled": True,
                    #"email_receivers": [
                    #    {
                    #        "name": "personalEmail",
                    #        "email_address": "mukulgupta2138@gmail.com",
                    #        "use_common_alert_schema": True
                    #    }
                    #],
                    "webhook_receivers": [
                        {
                            "name": f"{APP_NAME}-webhook",
                            "service_uri": ENDPOINT,
                            "use_common_alert_schema": False
                        }
                    ]
                }
            )
            print("Create action group:\n{}".format(action_group))

            rule_name = SHORT_APP_NAME
            my_alert = monitor_client.metric_alerts.create_or_update(
                resource_group_name,
                rule_name,
                {
                    'location': 'global',
                    'description': 'Trigger for deadletter appearing in service bus queue',
                    'severity': 3,
                    'enabled': True,
                    'name': rule_name,
                    'actions': [
                        {
                            "actionGroupId": action_group.id
                        }
                    ],
                    'evaluation_frequency': "PT1M",
                    'window_size': 'PT5M',
                    "criteria": {
                        "allOf": [
                            {
                                "threshold": 0,
                                "timeAggregation": "Average",
                                "operator": "GreaterThan",
                                "metricName": "DeadletteredMessages",
                                "metricNamespace": "Microsoft.ServiceBus/namespaces",
                                "name": "DeadletteredMessages",
                                "dimensions": [{
                                    'name': 'EntityName',
                                    'operator': 'Include',
                                    'values': all_queues
                                 }]
                            }
                        ],
                        "odata.type": "Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria"
                    },
                    "scopes": [
                        resource_id
                    ]
                }
            )

            print(my_alert)