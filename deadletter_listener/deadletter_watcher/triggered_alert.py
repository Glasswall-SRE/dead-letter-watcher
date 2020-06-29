from typing import Union, Dict


class TriggeredAlert:
    def __init__(self, alert: Dict) -> None:
        """Create an object to store the alert event

        Args:
            alert: a dict object containg the triggered event
        """
        self.alert = alert

    def get_deadletter_metric_value(self) -> Union[int, str]:
        """obtain the metric value from the event.

        Returns:
            int of the metric value or if comes in as string will return string
        """
        try:
            condition = self.alert['data']['alertContext']['condition']
            for x in condition['allOf']:
                return x['metricValue']
        except KeyError:
            raise KeyError(
                "metricValue key in TriggeredAlert not found in specified location"
            )

    def get_service_bus_queue_name(self) -> str:
        """obtain the service bus queue name from the event.

        Returns:
            name of the service bus queue in the alert
        """
        #TODO: What if multiple Queues are alerted on
        try:
            condition = self.alert['data']['alertContext']['condition']
            for x in condition['allOf']:
                if x['metricName'] == "DeadletteredMessages":
                    for dimension in x['dimensions']:
                        if dimension['name'] == 'EntityName':
                            return dimension['value']
        except KeyError:
            raise KeyError(
                "value key in TriggeredAlert to specify service bus queue not found in specified location"
            )

    def get_service_bus_name(self) -> str:
        """obtain the service bus name from the event.
        Returns:
            name of the service bus in the alert
        """
        return self.alert['data']['essentials']['alertTargetIDs'][0]

    def get_fired_datetime(self) -> str:
        """obtain the time the event fired from the event.

        Returns:
            firedDateTime in the alert
        """
        return self.alert['data']['essentials']['firedDateTime']
