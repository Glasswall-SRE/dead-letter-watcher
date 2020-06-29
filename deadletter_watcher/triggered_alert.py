from typing import Union

class TriggeredAlert:
    def __init__(self, alert):
        self.alert = alert

    def get_deadletter_metric_value(self) -> Union[int, str]:
        try:
            condition = self.alert['data']['alertContext']['condition']
            for x in condition['allOf']:
                return x['metricValue']
        except:
            raise KeyError("metricValue key not found in specified location")
            
    
    def get_service_bus_queue_name(self) -> str:
        #TODO: What if multiple Queues are alerted on
        try:
            condition = self.alert['data']['alertContext']['condition']
            for x in condition['allOf']: 
                if x['metricName'] == "DeadletteredMessages":
                    for dimension in x['dimensions']:
                        if dimension['name'] == 'EntityName':
                            return dimension['value']
        except:
            raise KeyError("value key to specify service bus queue not found in specified location")
    
    def get_service_bus_name(self):
        return self.alert['data']['essentials']['alertTargetIDs'][0]

    def get_fired_datetime(self):
        return self.alert['data']['essentials']['firedDateTime']


