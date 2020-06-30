import json
import slack
from typing import List, Dict
from deadletter_watcher.create_slack_block import create_slack_block
from deadletter_watcher.secrets import get_secret
from deadletter_watcher.triggered_alert import TriggeredAlert
import deadletter_watcher.service_bus as sb
from deadletter_watcher.datadog import datadog_log_query
from deadletter_watcher.util import get_datetime


def get_cluster(service_bus_name: str) -> str:
    """get the cluster name from the service bus namespace name
    Args:
        service_bus_name
    Returns:
        name of the cluster
    """
    splitted = service_bus_name.split("-")
    return splitted[len(splitted) - 1]


def obtain_deadletter_ids(queue: str, cluster: str, secrets: str) -> List[str]:
    """get all the deadletter ids from DLQ in cluster and queue specified
    Args:
        queue: service bus queue name
        cluster: cluster name to query
        secrets: secrets obtained from get_secret()
    Returns:
        a list of deadletters ID's from the `queue` in `cluster`
    """
    service_bus_client = sb.connect(
        secrets['SERVICE_BUS_CONNECTION_STRINGS'][cluster])
    deadletter_ids = sb.get_all_dead_letter_ids(queue, service_bus_client)
    return deadletter_ids


def send_slack_notification(slack_block: List[Dict], secrets):
    """Makes a call to datadog logs query. To search for log containing
    sender email, recipient email relating to transaction ID
    Args:
        slack_block: a series of blocks to be sent via slack
        secrets: secrets obtained from get_secret()
    Returns:
        response from postMessage event to slack channel
    """
    slack_client = slack.WebClient(secrets['DL-WATCHER']['BOT_TOKEN'])
    response = slack_client.chat_postMessage(
        channel=secrets['DL-WATCHER']['SLACK_CHANNEL'],
        text="deadletter",
        blocks=json.dumps(slack_block))
    return response


def lambda_handler(event, context):
    print(f"event:{event}, context:{context}")

    event = json.loads( event.get("body") )

    triggered_alert = TriggeredAlert(event)

    secrets = json.loads(get_secret())

    service_bus_name = triggered_alert.get_service_bus_name()
    queue = triggered_alert.get_service_bus_queue_name()
    cluster = get_cluster(service_bus_name)
    triggered_time = triggered_alert.get_fired_datetime()

    triggered_time_obj = get_datetime(triggered_time)

    deadletter_ids = obtain_deadletter_ids(queue, cluster, secrets)
    deadletter_ids.append("1234")
    deadletter_ids.append("5678")

    deadletters = []
    for deadletter_id in deadletter_ids:

        attributes = datadog_log_query(deadletter_id, triggered_time_obj,
                                       secrets)

        deadletter = {
            'message_id': deadletter_id,
            'tenant_name': attributes['tenant_name'],
            'sender': attributes['sender_email'],
            'recipient': attributes['recipient_email']
        }
        deadletters.append(deadletter)

    slack_block = create_slack_block(
        cluster=cluster,
        service=queue,
        count=str(triggered_alert.get_deadletter_metric_value()),
        deadletters=deadletters)

    response = send_slack_notification(slack_block, secrets)

    print(f"response:{response}")
    return response
