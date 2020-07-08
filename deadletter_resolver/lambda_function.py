import json
import json
from urllib.parse import parse_qs
from typing import Tuple
from deadletter_resolver.payload import Payload

def contact_victoria():
    pass


def lambda_handler(event, context):
    print(f"event:{event}, context:{context}")
    payload = Payload( json.loads(parse_qs(event['body'])['payload'][0]) )

    user_id = payload.get_user_id()
    channel_id = payload.get_channel_id()

    block_id = payload.get_actioned_block_id()
    block = payload.get_slack_block(block_id)

    value = payload.get_selected_option_value()

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
