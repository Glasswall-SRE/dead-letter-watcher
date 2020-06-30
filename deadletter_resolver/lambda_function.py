import json
import json
from urllib.parse import parse_qs

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

def is_run_clicked(payload) -> bool:
    if "value-run" == payload['actions'][0]['value']:
        return True
    return False

def lambda_handler(event, context):
    print(f"event:{event}, context:{context}")
    payload = json.loads(parse_qs(event['body'])['payload'][0])

    user_id = get_user_id(payload)
    channel_id = get_channel_id(payload)

    block_id = get_actioned_block_id(payload)
    block = get_slack_block(block_id, payload)

    if is_run_clicked(payload):
        print("Run Clicked")


    action_id = payload['actions'][0]['action_id']
    action_block_id = payload['actions'][0]['block_id']
    selected_option_value = payload['actions'][0]['selected_option']['value']
    selected_option_text = payload['actions'][0]['selected_option']['text']['text']




    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

