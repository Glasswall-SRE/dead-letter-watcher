# Proposal

Rebuild for Email uses a queue system to communicate messages between microservices. This means that when there is an issue between two services there 
a dead letter is generated.

Currently dead letter recovery is incredibly manual and is a large toil burden for SRE to recover the message. The aim of this project
is to reduce that toil and make it as automated as possible for us to manage.

## Functional Requirements

- A slack message should be sent to #sre-alerts-filetrustemail when a dead letter occurs on any of our Production (UK South and US East).
  the slack message must contain the following details:
  - Transaction ID of the dead letter.
  - Tenant Name associated with the dead letter.
  - The senders email address of the dead letter.
  - The recievers email address of the dead letter.
  - The time the email was recieved into the cluster. This can be retrieved from SMTPReciever.
  - The time the email dead letter.
- The following options must be avaiable within the slack message:
   - Replay the dead letter using victorias mailtoil replay:
     - This means replaying just that specific dead letter through the same queue it dead lettered on.
   - Reconstruct the email using Victorias mailtoil reconstruct and have the option to:
     - Send to a specific email address.
     - The subject of the email.
     - Body of the email.
   - Replay the email through Rebuild for Email using Victorias mailtoil email replay.


## Non-Functional Requirements

- The service must be monitored by DataDog. Any failed invokations or throttling to be reported to a new Slack Channel #sre-alerts-automation.
- Any new automation logic defined as interacting with Rebuild for email to automate an action should be added to Victoria so SRE can do these actions manually.
- Fully deployable via Serverless Framework for every component.
- CI and CD Pipelines for the whole project.
- 80% code coverage with unit and intergration tests on all code.
- All access tokens are stored in key vaults or pulled from source and injected on boot. 
- Serverless and event driven. Ideally should not poll queues but be invoked when a dead letter happens. Nothing should be running hot like a microservice.
- All code is Sonarcloud quality checked.
- ReadME with an exact description on how to configure, setup and run from scratch. 
- Full handover to SRE
