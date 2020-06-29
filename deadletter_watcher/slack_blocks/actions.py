def create_actions_slack_block():
    """Run action will trigger events to V.I.C.T.O.R.I.A
    Actions Slack Block will provide the Inputs from the user to respond.
    Returns:
        Actions Slack Block
    """
    return {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "emoji": True,
                    "text": "Run"
                },
                "value": "Run"
            }
        ]
    }
