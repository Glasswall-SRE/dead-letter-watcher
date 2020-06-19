from typing import List, Dict

def create_options_slack_block(options: List[str]) -> List[Dict]:
    """Create a Slack Block which will contain a list of potential options
    a deadletter may have.
    Args:
        options: options that may be selected in drop down per deadletter
    Returns:
        Options Slack Block
    """
    options_slack_blocks = []
    for option in options:
        slack_block = {
            "text": {
                "type": "plain_text",
                "emoji": True,
                "text": option
            },
            "value": f"value-{option}"
        }
        options_slack_blocks.append(slack_block)
    return options_slack_blocks
