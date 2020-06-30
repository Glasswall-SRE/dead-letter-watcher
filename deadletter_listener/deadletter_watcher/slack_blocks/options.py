from typing import List, Dict


def create_options_slack_block(msg_id: str ,options: List[str]) -> List[Dict]:
    """Create a Slack Block which will contain a list of potential options
    a deadletter may have.
    Args:
        options: options that may be selected in drop down per deadletter
    Returns:
        Options Slack Block
    """
    if len(options) == 0:
        raise ValueError("Input Value cannot be an empty list")

    options_slack_blocks = []
    for option in options:
        slack_block = {
            "type": "button",
            "text": {
                "type": "plain_text",
                "emoji": True,
                "text": option
            },
            "value": f"value-{msg_id}-{option}"
        }
        options_slack_blocks.append(slack_block)
    return options_slack_blocks
