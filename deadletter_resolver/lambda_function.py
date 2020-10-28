import json
from urllib.parse import parse_qs
from typing import Tuple
from deadletter_resolver.payload import Payload
from slack import WebhookClient
# from victoria_email.replay_deadletters import replay
# from victoria_email.reconstruct_mail import reconstruct


def lambda_handler(event, context):
    print(f"event:{event}, context:{context}")
    # Get the payload from slack action button
    if event:
        payload = Payload(json.loads(parse_qs(event['body'])['payload'][0]))
        # get selected option value
        value = payload.get_selected_option_value()
        # get response url
        response_url = payload.get_response_url()

        if value == 'Replay':
            # TODO: invoke replay function from victoria
            message = 'Invoke victoria replay function'
        elif value == 'Reconstruct':
            # TODO: invoke replay function from victoria
            message = 'Invoke Victoria reconstruct function'
        else:
            message = 'No action item selected'

        # acknowledge action to user
        slack_client=WebhookClient(response_url)
        text = "Thanks for your request, we'll process it shortly."
        slack_client.send(text=text)

    else:
        message = 'No data passed'

    body = {
        "message": message
    }

    # send a response
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response



