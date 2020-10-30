
class Payload:
    def __init__(self, payload_event) -> None:
        self.payload_event = payload_event

    def get_user_id(self) -> str:
        return self.payload_event['user']['id']

    def get_channel_id(self) -> str:
        return self.payload_event['channel']['id']

    def get_actioned_block_id(self) -> str:
        return self.payload_event['actions'][0]['block_id']

    def get_slack_block(self, block_id):
        for block in self.payload_event['message']['blocks']:
            if block_id == block['block_id']:
                return block

    def get_selected_option_value(self) -> str:
        """
            gets the user selected action from slack
            # e.g value-msgid=123-option=Replay
        """
        value = self.payload_event['actions'][0]['value']

        return value.split('=')[2]

    def get_response_url(self) -> str:
        """
            gets the slack webhook to acknowledge action item from user
        """
        return self.payload_event['response_url']