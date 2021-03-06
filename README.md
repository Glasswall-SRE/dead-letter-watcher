<div align="center">

# dead-letter-watcher
A series of Azure Functions that wait for events to handle dead-letters

# CI

![CI Deadletter Watcher](https://github.com/glasswall-sre/dead-letter-watcher/workflows/CI%20Deadletter%20Watcher/badge.svg)
![CI Deadletter Resolver](https://github.com/glasswall-sre/dead-letter-watcher/workflows/CI%20Deadletter%20Resolver/badge.svg)

# CD

![CD Deadletter Watcher](https://github.com/glasswall-sre/dead-letter-watcher/workflows/CD%20Deadletter%20Watcher/badge.svg)
![CD Deadletter Resolver](https://github.com/glasswall-sre/dead-letter-watcher/workflows/CD%20Deadletter%20Resolver/badge.svg)
![CD Azure Event Trigger](https://github.com/glasswall-sre/dead-letter-watcher/workflows/CD%20Azure%20Event%20Trigger/badge.svg)

***

![PyPI pyversions](https://img.shields.io/badge/python-3.8-blue)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
![](https://img.shields.io/badge/Glasswall%20SRE-Approved-success)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/4146/badge)](https://bestpractices.coreinfrastructure.org/projects/4146)


</div>

## Motivation
The frequency with which deadletter messages cause call outs required a method of reducing time spent during these incidents and provide a automated solution to gather nessessary information and action the deadletters.
This repository provides the solution to allow an interactive way through Slack to action deadletters even from the comfort of a mobile device. 

<img src="example_alert.png" alt="drawing" width="400"/>

## Architecture
The archictecture comprises of 3 services:
- Event Trigger Service
- Deadletter Watcher Service
- Deadletter Resolver Service

<div align="center">

![Level 1 Context Diagram](./architecture_diagram/dead_letter_watcher_Level_1_Context.png)
### Level 1 Context Diagram

<br>
<br>
<br>

![Level 2 Container Diagram](./architecture_diagram/dead_letter_watcher_Level_2_Container.png)
### Level 2 Container Diagram

<br>
<br>
<br>

![Level 3 Component Diagram](./architecture_diagram/dead_letter_watcher_Level_3_Component.png)
### Level 3 Component Diagram

<br>
<br>
<br>

</div>

### Event Trigger Service
This service deploys the nessassary components in order to:
- create the alerts for when the deadlettered messages threshold surpases 0.
- contact the webook for deadletter-watcher service.

### Deadletter Watcher Service
This service will install all nessessary pip modules, deploy infrustructure to AWS required for a serverless API and also run the following actions:
- create the slack blocks UI to post to slack.
- search the relevant service bus queue from the event trigger alert for deadletters.
- obtain message id's and obtain further details about the message from DataDog such as recipient email, sender email.

### Deadletter Resolver Service
This service will
- interact with every action taking place on the UI sent to Slack from the Deadletter Watcher Service.
- contact V.I.C.T.O.R.I.A in order to run the action user triggered for the specific deadletter.

## Tech Stack
- Python 3.8
  - Slack API
  - DataDog API
  - AWS SDK
- Infrustructure
  - AWS
  - Azure
- CI/CD
  - GitHub Actions
  - Serverless
  - Pulumi

## FAQ

### How to Setup Deadletter Watcher in a different Slack Channel
- To setup Deadletter Watcher in another slack channel, insert the target channel id in the [Secrets Manager](#secrets) field of `SLACK_CHANNEL`
### How to add Queues or Clusters to Deadletter Watcher
- When a new queue or cluster is added that should be scrutenised by the Event Trigger Service, place the queue or cluster in the [Secrets Manager](#secrets) and redeploy the Event Trigger Service.

## Secrets
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

## Local Testing
Change working directory for the service intended for testing or amend any configs for test discovery to allow for the change of directory. Following that run the following command.
```
python -m pytest
```
