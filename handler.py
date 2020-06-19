import json
import slack
from deadletter_watcher.create_slack_block import create_slack_block

def hello(event, context):
    print(f"event:{event}, context:{context}")
    # Will be moved to secrets manager
    secrets={
        'slack-channel':'private',
        'bot-token':'private'
    }

    client = slack.WebClient(secrets['bot-token'])


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
        channel=secrets['slack-channel'], 
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
