import pytest
import deadletter_watcher.triggered_alert as triggered_alert


def test_get_deadletter_metric_value_as_int():
    # Arrange
    alert = {
        "schemaId": "test",
        "data": {
            "essentials": {
                "alertContextVersion": "1.0"
            },
            "context": {
                "properties": None,
                "condition": {
                    "windowSize":
                    "PT5M",
                    "allOf": [{
                        "metricName": "DeadletteredMessages",
                        "dimensions": [{
                            "name": "EntityName",
                            "value": "smtptransmission"
                        }],
                        "metricValue": 31.1105
                    }],
                    "windowStartTime":
                    "2019-03-22T13:40:03.064Z"
                }
            }
        }
    }
    # Act
    trigger_alert_obj = triggered_alert.TriggeredAlert(alert)
    metric_value = trigger_alert_obj.get_deadletter_metric_value()
    # Assert
    assert metric_value == 31.1105


def test_get_deadletter_metric_value_as_str():
    # Arrange
    alert = {
        "schemaId": "test",
        "data": {
            "essentials": {
                "alertContextVersion": "1.0"
            },
            "context": {
                "properties": None,
                "condition": {
                    "windowSize":
                    "PT5M",
                    "allOf": [{
                        "metricName":
                        "DeadletteredMessages",
                        "dimensions": [{
                            "name": "EntityName",
                            "value": "smtptransmission"
                        }],
                        "metricValue":
                        "31.1105"
                    }],
                    "windowStartTime":
                    "2019-03-22T13:40:03.064Z"
                }
            }
        }
    }
    # Act
    trigger_alert_obj = triggered_alert.TriggeredAlert(alert)
    metric_value = trigger_alert_obj.get_deadletter_metric_value()
    # Assert
    assert metric_value == "31.1105"


def test_get_deadletter_metric_value_missing_key():
    # Arrange
    alert = {
        "schemaId": "test",
        "data": {
            "essentials": {
                "alertContextVersion": "1.0"
            },
            "context": {
                "properties": None,
                "condition": {
                    "windowSize":
                    "PT5M",
                    "allOf": [{
                        "metricName":
                        "DeadletteredMessages",
                        "dimensions": [{
                            "name": "EntityName",
                            "value": "smtptransmission"
                        }]
                    }],
                    "windowStartTime":
                    "2019-03-22T13:40:03.064Z"
                }
            }
        }
    }
    # Act
    trigger_alert_obj = triggered_alert.TriggeredAlert(alert)
    # Assert
    with pytest.raises(KeyError):
        metric_value = trigger_alert_obj.get_deadletter_metric_value()


def test_get_service_bus_queue_name():
    # Arrange
    alert = {
        "schemaId": "test",
        "data": {
            "essentials": {
                "alertContextVersion": "1.0"
            },
            "context": {
                "properties": None,
                "condition": {
                    "windowSize":
                    "PT5M",
                    "allOf": [{
                        "metricName":
                        "DeadletteredMessages",
                        "dimensions": [{
                            "name": "EntityName",
                            "value": "smtptransmission"
                        }]
                    }],
                    "windowStartTime":
                    "2019-03-22T13:40:03.064Z"
                }
            }
        }
    }
    # Act
    trigger_alert_obj = triggered_alert.TriggeredAlert(alert)
    service_bus_queue = trigger_alert_obj.get_service_bus_queue_name()
    # Assert
    assert "smtptransmission" == service_bus_queue


def test_get_service_bus_queue_name_missing_key():
    # Arrange
    alert = {
        "schemaId": "test",
        "data": {
            "essentials": {
                "alertContextVersion": "1.0"
            },
            "context": {
                "properties": None,
                "condition": {
                    "windowSize":
                    "PT5M",
                    "allOf": [{
                        "metricName": "DeadletteredMessages",
                        "dimensions": [{
                            "name": "EntityName"
                        }]
                    }],
                    "windowStartTime":
                    "2019-03-22T13:40:03.064Z"
                }
            }
        }
    }
    # Act
    trigger_alert_obj = triggered_alert.TriggeredAlert(alert)
    # Assert
    with pytest.raises(KeyError):
        service_bus_queue = trigger_alert_obj.get_service_bus_queue_name()
