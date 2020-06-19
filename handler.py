import json
import slack
from deadletter_watcher.create_slack_block import create_slack_block
from deadletter_watcher.secrets import get_secret

def hello(event, context):
    print(f"event:{event}, context:{context}")

    secrets = get_secret()

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


    slack_block = create_slack_block("eu-west-cluster","smtp-service", 5, deadletters)

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

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
