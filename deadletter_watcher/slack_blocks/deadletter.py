from typing import Dict
from deadletter_watcher.slack_blocks.options import create_options_slack_block

def create_deadletter_slack_block(trx_id: str, tenant: str,
                                  sender: str, receiver: str) -> Dict:
    """Create a Slack Block containing deadletter details
    Args:
        trx_id: message id from the deadlettered message
        tenant: tenant name message originated from
        sender: sender email address
        receiver: receiver email address
    Returns:
        Deadletter Slack Block
    """
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"*<fakeLink.datadoglink.com|{trx_id}>*\n\
                Tenant Name: {tenant}\n\
                Sender:{sender}\n\
                Receiver:{receiver}"
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
