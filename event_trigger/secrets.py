import boto3
import base64
import json
import pulumi_azure as azure
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
    client = session.client(service_name='secretsmanager',
                            region_name="eu-west-2")

    get_secret_value_response = client.get_secret_value(
        SecretId="deadletter-watcher-secrets")

    if 'SecretString' in get_secret_value_response:
        return get_secret_value_response['SecretString']
    else:
        decoded_binary_secret = base64.b64decode(
            get_secret_value_response['SecretBinary'])
        return decoded_binary_secret


def get_service_bus_connection(namespace, resource_group):
    """
    Retrieves service bus connection string for a given namespace and resource group
    Args:
        namespace:
        resource_group:

    Returns:
        service bus connection string.
    """
    sb = azure.servicebus.get_namespace(name=namespace,
                                             resource_group_name=resource_group)
    return sb.default_primary_connection_string


def update_secret(sb_list):
    """
    Updates secrets in AWS based on service bus list details
    Args:
        sb_list:

    Returns:

    """
    if sb_list:
        service_bus_details = json.loads(sb_list)
        for sb in service_bus_details:
            sb_conn = get_service_bus_connection(sb['namespace'], sb['resourceGroup'])
            sb['connection_str'] = sb_conn
            print("successfully retrieved connection str")
            print(sb_conn)
        print(service_bus_details)

