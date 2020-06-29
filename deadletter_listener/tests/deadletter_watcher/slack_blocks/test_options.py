import pytest
import deadletter_watcher.slack_blocks.options as options_block


def test_create_options_slack_block_amount_of_blocks():
    # Arrange
    input_options = ["option1", "option2", "option3"]
    # Act
    options = options_block.create_options_slack_block(input_options)
    # Assert
    assert len(options) == len(input_options)


def test_create_options_slack_block_name_of_blocks():
    # Arrange
    input_options = ["option1", "option2", "option3"]
    # Act
    options_blocks = options_block.create_options_slack_block(input_options)
    # Assert
    for block, input_str in zip(options_blocks, input_options):
        assert block["text"]["text"] == input_str


def test_create_options_slack_block_empty_list_of_options():
    # Arrange
    input_options = []
    # Act
    # Assert
    with pytest.raises(ValueError):
        options_blocks = options_block.create_options_slack_block(
            input_options)
