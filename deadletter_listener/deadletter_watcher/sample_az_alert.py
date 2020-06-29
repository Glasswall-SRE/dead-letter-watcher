alert = {
    "schemaId": "azureMonitorCommonAlertSchema",
    "data": {
        "essentials": {
            "alertId":
            "/subscriptions/<subscription ID>/providers/Microsoft.AlertsManagement/alerts/b9569717-bc32-442f-add5-83a997729330",
            "alertRule": "WCUS-R2-Gen2",
            "severity": "Sev3",
            "signalType": "Metric",
            "monitorCondition": "Resolved",
            "monitoringService": "Platform",
            "alertTargetIDs": ["glasswall-sb-weu-gwc-filetrust-dev"],
            "originAlertId":
            "3f2d4487-b0fc-4125-8bd5-7ad17384221e_PipeLineAlertRG_microsoft.insights_metricAlerts_WCUS-R2-Gen2_-117781227",
            "firedDateTime": "2020-06-26T14:58:24.3713213Z",
            "resolvedDateTime": "2019-03-22T14:03:16.2246313Z",
            "description": "",
            "essentialsVersion": "1.0",
            "alertContextVersion": "1.0"
        },
        "alertContext": {
            "properties": None,
            "conditionType": "SingleResourceMultipleMetricCriteria",
            "condition": {
                "windowSize":
                "PT5M",
                "allOf": [{
                    "metricName":
                    "DeadletteredMessages",
                    "metricNamespace":
                    "Microsoft.ServiceBus/namespaces",
                    "operator":
                    "GreaterThan",
                    "threshold":
                    "0",
                    "timeAggregation":
                    "Average",
                    "dimensions": [{
                        "name": "EntityName",
                        "value": "smtptransmission"
                    }],
                    "metricValue":
                    31.1105
                }],
                "windowStartTime":
                "2019-03-22T13:40:03.064Z",
                "windowEndTime":
                "2019-03-22T13:45:03.064Z"
            }
        }
    }
}
