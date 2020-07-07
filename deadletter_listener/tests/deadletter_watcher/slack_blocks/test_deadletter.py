import pytest
import deadletter_watcher.slack_blocks.deadletter as dl_block


def test_create_deadletter_slack_block():
    # Arrange
    trx_id = "12345678-1234-1234-1234-123456879012"
    tenant = "test_tenant"
    sender = "sender@email.com"
    receiver = "receiver@email.com"
    timestamp = "2020-07-07T10:20:22.784Z"
    # Act
    deadletter_block = dl_block.create_deadletter_slack_block(
        trx_id=trx_id, tenant=tenant, sender=sender, receiver=receiver, timestamp=timestamp)
    # Assert
    assert deadletter_block["type"] == "section" and \
        trx_id in deadletter_block["text"]["text"] and \
        tenant in deadletter_block["text"]["text"] and \
        sender in deadletter_block["text"]["text"] and \
        receiver in deadletter_block["text"]["text"]
