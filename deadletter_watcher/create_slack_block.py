from deadletter_watcher.slack_blocks.deadletter import create_deadletter_slack_block
from deadletter_watcher.slack_blocks.actions import create_actions_slack_block
from deadletter_watcher.slack_blocks.welcome import create_welcome_slack_block
from typing import Dict,List

def create_slack_block(cluster:str, service:str, count:int, deadletters : List[Dict]) -> List[Dict]:
    """Create a Slack Block from deadletter information
    Args:
        cluster: affected cluster
        service: affected service bus
        count: number of deadletters in service bus
        deadletters: List of Dicts containg deadletter information
        Dict Keys Required
        'message_id':str, 'tenant_name':str, 'sender':str, 'recipient':str
    Returns:
        Slack Block
    """
    block = []

    block.append(create_welcome_slack_block(cluster, service, count))

    block.append({
            "type": "divider"
        })

    for deadletter in deadletters:
        deadletter_slack_block = create_deadletter_slack_block(
            deadletter['message_id'],
            deadletter['tenant_name'],
            deadletter['sender'],
            deadletter['recipient']
        )
        block.append(deadletter_slack_block)

        block.append({
            "type": "divider"
        })

    block.append(create_actions_slack_block())
        
    return block