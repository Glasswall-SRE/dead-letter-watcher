import pytest
import deadletter_watcher.slack_blocks.welcome as welcome


def test_create_welcome_slack_block():
    # Arrange
    cluster = "test_prod"
    service = "test_fileoutputter"
    count = "500"
    # Act
    welcome_block = welcome.create_welcome_slack_block(cluster, service, count)
    # Assert
    assert welcome_block["type"] == "section" and \
        cluster in welcome_block["text"]["text"] and \
        service in welcome_block["text"]["text"] and \
        count in welcome_block["text"]["text"]
