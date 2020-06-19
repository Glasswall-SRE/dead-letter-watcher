

def create_actions_slack_block():
    """Run action will trigger events to V.I.C.T.O.R.I.A
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
                "value": "run_action"
            }
        ]
    }