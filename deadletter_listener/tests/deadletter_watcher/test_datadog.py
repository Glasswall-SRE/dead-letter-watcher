import pytest
from unittest.mock import patch
import deadletter_watcher.datadog as datadog
import datetime

@patch('requests.get')
def test_validate(patched_get):
    # Arrange
    patched_get.return_value.status_code = 200
    secrets = {
        "DL-WATCHER": {
            "DD_API_KEY" : "0121-DO-1"
        }
    }

    # Act
    response = datadog.validate(secrets)

    # Assert
    assert patched_get.called is True
    assert response.status_code == 200


@patch('deadletter_watcher.datadog.__datadog_request_tenant_id')
@patch('deadletter_watcher.datadog.__datadog_request_emails')
def test_datadog_log_query_successful_request(patched_emails, patched_tenant):
    # Arrange
    message_id = "12345678-1234-1234-1234-12345678901234"
    secrets = {
        "DL-WATCHER": {
            "DD_API_KEY" : "0121-DO-1"
        }
    }
    now = datetime.datetime.now()

    # Arrange Mock
    patched_emails.return_value = {
        'statusCode': 200,
        'logs': [
            {
                "content": {
                    "attributes" : {
                        "sender_email": "sender@unittest.com",
                        "recipient_email": "recipient@unittest.com"
                    }
                }
            }
        ]
    }
    patched_tenant.return_value = {
        'statusCode': 200,
        'logs': [
            {
                "content": {
                    "timestamp": "unittest_time",
                    "attributes" : {
                        "tenant_name": "unittest_tenant"
                    }
                }
            }
        ]
    }

    # Act
    deadletter_details = datadog.datadog_log_query(message_id, now, secrets)

    # Assert
    assert patched_emails.called is True
    assert patched_tenant.called is True
    assert deadletter_details['timestamp'] == "unittest_time" and \
            deadletter_details['tenant_name'] == "unittest_tenant" and \
            deadletter_details['sender_email'] == "sender@unittest.com" and \
            deadletter_details['recipient_email'] == "recipient@unittest.com"


@patch('deadletter_watcher.datadog.__datadog_request_tenant_id')
@patch('deadletter_watcher.datadog.__datadog_request_emails')
def test_datadog_log_query_email_details_not_found_in_logs(patched_emails, patched_tenant):
    # Arrange
    message_id = "12345678-1234-1234-1234-12345678901234"
    secrets = {
        "DL-WATCHER": {
            "DD_API_KEY" : "0121-DO-1"
        }
    }
    now = datetime.datetime.now()

    patched_emails.return_value = {
        # Empty logs
        'statusCode': 200,
        'logs': [],
    }

    # Act
    deadletter_details = datadog.datadog_log_query(message_id, now, secrets)

    error_message = "Cannot Find in DataDog Log"

    # Assert
    assert patched_emails.called is True
    assert patched_tenant.called is False
    assert deadletter_details['tenant_name'] == error_message
    assert deadletter_details['sender_email'] == error_message
    assert deadletter_details['recipient_email'] == error_message