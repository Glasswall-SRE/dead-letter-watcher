import boto3
import base64
from botocore.exceptions import ClientError
from typing import Dict

def get_secret() -> Dict:
    """Obtain the secrets in the AWS Secrets Manager
    Returns:
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
            }
        }
    """
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name="eu-west-2"
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId="deadletter-watcher-secrets"
        )
    except ClientError as e:
            raise e
    else:
        if 'SecretString' in get_secret_value_response:
            return get_secret_value_response['SecretString']
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])