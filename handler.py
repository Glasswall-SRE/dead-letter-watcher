import json
import slack
from deadletter_watcher.create_slack_block import create_slack_block
from deadletter_watcher.secrets import get_secret
from deadletter_watcher.sample_az_alert import alert
from deadletter_watcher.triggered_alert import TriggeredAlert

def hello(event, context):
    print(f"event:{event}, context:{context}")
    
    az_event = alert

    triggered_alert = TriggeredAlert(az_event)

    secrets = json.loads(get_secret())['DL-WATCHER']

    client = slack.WebClient(secrets['BOT_TOKEN'])



    # To Delete ------- \/ \/ \/ \/ \/
    deadletter = {
        'message_id':'01234567-0123-0123-0123-01234567890123',
        'tenant_name':'test_tenant',
        'sender':'sender@mail.com',
        'recipient':'recipient@mail.com'
    }

    deadletters = [
        deadletter
    ]
    # To Delete ------- /\ /\ /\ /\ /\


    # https://docs.microsoft.com/en-us/rest/api/servicebus/queues/listkeys
    # https://docs.microsoft.com/en-us/rest/api/servicebus/queues/get#examples
    # https://stackoverflow.com/questions/31288018/reading-deadlettered-messages-from-service-bus-queue


    slack_block = create_slack_block(
        cluster=triggered_alert.get_cluster(),
        service=triggered_alert.get_service_bus_queue(), 
        count=str(triggered_alert.get_deadletter_metric_value()), 
        deadletters=deadletters
    )

    response = client.chat_postMessage(
        channel=secrets['SLACK_CHANNEL'], 
        text="deadletter", 
        blocks=json.dumps(slack_block)
    )

    response = {
        "statusCode": 200,
        "body": "OK"
    }

    print(f"response:{response}")
    return response
