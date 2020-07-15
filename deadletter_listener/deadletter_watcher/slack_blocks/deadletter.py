from typing import Dict


def create_deadletter_slack_block(trx_id: str, tenant: str, sender: str,
                                  receiver: str, timestamp: str):
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
            "text": f"*<fakeLink.datadoglink.com|{trx_id}>*\nTenant name: {tenant}\nSender: {sender}\nReceiver: {receiver}\nTime Received: {timestamp}"
        }
    }
    
