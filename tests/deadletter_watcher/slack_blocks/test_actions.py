import pytest
import deadletter_watcher.slack_blocks.actions as actions

def test_create_actions_slack_block():
    # Arrange
    # Act
    actions_block = actions.create_actions_slack_block()
    # Assert
    assert actions_block["elements"][0]["value"] == "Run" and \
        actions_block["elements"][0]["text"]["text"] == "Run"