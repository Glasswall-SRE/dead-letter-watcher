def create_welcome_slack_block(cluster: str, service: str, count: str):
    """Creates a Slack Block containing a welcome message which displays
    a summary of the deadletter triggered issue.
    Returns:
        Welcome Slack Block
    """
    return {
        "type": "section",
        "text": {
            "type":
            "mrkdwn",
            "text":
            f"Hi SRE, You have Service Bus Dead Letters:\nCluster : {cluster}\nService : {service}\nCount : {count}"
        },
    }
