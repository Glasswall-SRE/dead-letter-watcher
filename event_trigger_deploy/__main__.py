import json
from secrets import get_secret
import pulumi_azure as azure
from pulumi_azure import monitoring
from pulumi_azure import core

secrets = json.loads(get_secret())

APP_NAME = "dead-letter-watcher"
SHORT_APP_NAME = "dl-wtcr"

ENDPOINT = secrets["PULUMI"]["DEADLETTER_WATCHER_ENDPOINT"]
QUEUES = secrets["PULUMI"]["SERVICE_BUS_QUEUES"]

non_prod_clusters = ["dev", "qa1", "qa2", "pent", "perf", "stage"]
prod_clusters = ["uksprod1", "uksprod2", "useprod1", "useprod2"]

for cluster in prod_clusters:
    SERVICE_BUS_RESOURCE_GROUP = secrets["PULUMI"]["clusters"][cluster][
        "SERVICE_BUS_RESOURCE_GROUP"]
    SB_NAMESPACE = secrets["PULUMI"]["clusters"][cluster][
        "SERVICE_BUS_NAMESPACE"]

    #  Create Action Group
    action_group = monitoring.ActionGroup(
        f"{SHORT_APP_NAME}-{cluster}",
        short_name=SHORT_APP_NAME,
        resource_group_name=SERVICE_BUS_RESOURCE_GROUP,
        webhook_receivers=[{
            'name': f"{APP_NAME}-webhook",
            'service_uri': ENDPOINT,
        }])

    # Create Metric Alert
    metric_alert = monitoring.MetricAlert(
        f"{SHORT_APP_NAME}-{cluster}",
        resource_group_name=SERVICE_BUS_RESOURCE_GROUP,
        scopes=azure.servicebus.get_namespace(
            name=SB_NAMESPACE,
            resource_group_name=SERVICE_BUS_RESOURCE_GROUP).id,
        actions=[{
            'action_group_id': action_group.id
        }],
        criterias=[{
            'aggregation': 'Average',
            'metricName': 'DeadletteredMessages',
            'metricNamespace': 'Microsoft.ServiceBus/namespaces',
            'operator': 'GreaterThan',
            'threshold': 0,
            'dimensions': [{
                'name': 'EntityName',
                'operator': 'Include',
                'values': QUEUES
            }]
        }])

    # Create Action Rule Action Group
    action_rule = monitoring.ActionRuleActionGroup(
        f"{SHORT_APP_NAME}-{cluster}",
        resource_group_name=SERVICE_BUS_RESOURCE_GROUP,
        description="trigger for deadletter appearing in service bus queue",
        action_group_id=action_group.id,
        scope={
            'type': 'ResourceGroup',
            'resourceIds': [core.get_resource_group(name=SERVICE_BUS_RESOURCE_GROUP).id]
        },
        condition={
            'monitorService': {
                'operator': 'Equals',
                'values': ['Platform']
            },
            'alertRuleId': {
                'operator': 'Equals',
                'values': [metric_alert.id]
            }
        })
