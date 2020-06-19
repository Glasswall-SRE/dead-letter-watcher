import pulumi
import pulumi_azure as azure
from pulumi_azure import monitoring
from pulumi_azure import core

APP_NAME="dead-letter-watcher"
ENDPOINT="https://o8l52l2o29.execute-api.eu-west-2.amazonaws.com/dev/listener"

# Heirarchy
# Resource Group / Contains the Dev Service Bus Namespace
SERVICE_BUS_RESOURCE_GROUP="rgp-weu-gwc-filetrust-dev-sb"
# Service Bus Namespace / Contains all the Queues
SB_NAMESPACE="glasswall-sb-weu-gwc-filetrust-dev"
# Queues
QUEUES="list of queues"


action_group = monitoring.ActionGroup(f"{APP_NAME}-ag",
    short_name=APP_NAME,
    resource_group_name=SERVICE_BUS_RESOURCE_GROUP,
    webhook_receivers=[
        {
            'name': f"{APP_NAME}-webhook",
            'service_uri': ENDPOINT,
        }
    ]
)

metric_alert = monitoring.MetricAlert(f"{APP_NAME}-ma",
    resource_group_name=SERVICE_BUS_RESOURCE_GROUP,
    scopes=azure.servicebus.get_namespace(name=SB_NAMESPACE).id,
    actions=[
        {
            'action_group_id' : action_group.id 
        }
    ],
    criterias=[
        {
            'aggregation' : 'Average',
            'metricName' : 'deadletter-metric',
            'metricNamespace' : 'deadletter-metric-namespace',
            'operator' : 'GreaterThan',
            'threshold' : 0,
            'dimensions': [
                {
                    'name' : 'EntityName',
                    'operator' : 'Include',
                    'values' : [
                        "dataretention",
                        "fileanalysis",
                        "fileinspection",
                        "filepreview",
                        "fileprotect",
                        "filereleasedeletenotification",
                        "filereleaserequest",
                        "filerouter",
                        "heldfilenotification",
                        "heldfilerelease",
                        "heldfilerouter",
                        "messageinspection",
                        "messageregeneration",
                        "notification",
                        "smtptransmission",
                        "threatassessor",
                        "threatcensor",
                        "transactionchecker",
                        "transactionreport"
                    ]
                }
            ]
        }
    ]
)

action_rule = monitoring.ActionRuleActionGroup(f"{APP_NAME}-ar",
    resource_group_name=SERVICE_BUS_RESOURCE_GROUP,
    description="trigger for deadletter appearing in service bus queue",
    action_group_id=action_group.id,
    scope={
        'type': 'Resource',
        'resourceIds' : core.get_resource_group(name=SERVICE_BUS_RESOURCE_GROUP).id
    },
    condition={
        'monitorService' : {
            'operator' : 'Equals',
            'values' : ['Platform']
        },
        'alertRuleId' : {
            'operator' : 'Equals',
            'values' : [ metric_alert.id ]
        }

    }
    
)