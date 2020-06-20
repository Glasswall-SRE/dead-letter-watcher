# dead-letter-watcher
A series of Azure Functions that wait for events to handle dead-letters

# Secrets
```
{
    "PULUMI": {
        "SERVICE_BUS_RESOURCE_GROUP": str,
        "SERVICE_BUS_NAMESPACE": str,
        "DEADLETTER_WATCHER_ENDPOINT": str,
        "SERVICE_BUS_QUEUES":[ str ]
    },
    "DL-WATCHER": {
        "SLACK_CHANNEL": str,
        "BOT_TOKEN": str
    },
    "SERVICE_BUS_CONNECTION_STRINGS": {
        { 'str': 'str' }
    }
}
```