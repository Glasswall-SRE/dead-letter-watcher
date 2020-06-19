def create_welcome_slack_block(cluster, service, count):
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"Hi SRE, Oopsie Whoopsie, UwU, You have Service Bus Dead Letters:\nCluster : {cluster}\nService : {service}\nCount : {count}"
        },
    }