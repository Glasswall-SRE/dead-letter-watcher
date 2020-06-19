from typing import Dict
from deadletter_watcher.slack_blocks.options import create_options_slack_block

def create_deadletter_slack_block(trx_id : str, tenant : str, sender : str, receiver : str) -> Dict:
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"*<fakeLink.datadoglink.com|{trx_id}>*\nTenant Name: {tenant}\nSender:{sender}\nReceiver:{receiver}"
        },
        "accessory": {
            "type": "static_select",
            "placeholder": {
                "type": "plain_text",
                "emoji": True,
                "text": "Select Action"
            },
            "options": create_options_slack_block(["replay", "reconstruct"])
        }
    }