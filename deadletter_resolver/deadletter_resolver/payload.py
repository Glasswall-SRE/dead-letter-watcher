
class Payload:
    def __init__(self, payload_event) -> None:
        self.payload = payload_event


    def get_user_id(self) -> str:
        return self.payload['user']['id']


    def get_channel_id(self) -> str:
        return self.payload['channel']['id']


    def get_actioned_block_id(self) -> str:
        return self.payload['actions'][0]['block_id']


    def get_slack_block(self, block_id):
        for block in self.payload['message']['blocks']:
            if block_id == block['block_id']:
                return block


    def get_selected_option_value(self) -> str:
        return self.payload['actions'][0]['value']