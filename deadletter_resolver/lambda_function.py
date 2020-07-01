import json
import json
from urllib.parse import parse_qs
from typing import Tuple


def get_user_id(payload) -> str:
    return payload['user']['id']


def get_channel_id(payload) -> str:
    return payload['channel']['id']


def get_actioned_block_id(payload) -> str:
    return payload['actions'][0]['block_id']


def get_slack_block(block_id, payload):
    for block in payload['message']['blocks']:
        if block_id == block['block_id']:
            return block


def get_selected_option_value(payload) -> Tuple[str, str]:
    selected_option_value = payload['actions'][0]['value']
    items = selected_option_value.split("-")
    if items[0] == "value":
        if items[2] == "replay" or items[2] == "reconstruct":
            return items[1], items[2]
        else:
            print("Illegal value in action location")


def contact_victoria():
    pass


def lambda_handler(event, context):
    print(f"event:{event}, context:{context}")
    payload = json.loads(parse_qs(event['body'])['payload'][0])

    user_id = get_user_id(payload)
    channel_id = get_channel_id(payload)

    block_id = get_actioned_block_id(payload)
    block = get_slack_block(block_id, payload)

    trx_id, action = get_selected_option_value(payload)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
