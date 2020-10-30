import requests
from deadletter_watcher.util import set_datetime
import datetime
import json
from typing import Dict, Union, Tuple


def validate(secrets: Dict) -> requests.models.Response:
    """Validates datadog API key by contacting GET validate HTTP Request
    Args:
        secrets: secrets obtained from get_secret()
    Returns:
        response from validate GET request
    """
    validate_headers = {
        'DD-API-KEY': secrets['DL-WATCHER']['DD_API_KEY'],
    }
    response = requests.get(
        "https://api.datadoghq.eu/api/v1/validate", headers=validate_headers)
    return response


def __datadog_request_emails(trx_id: str, from_datetime: str, to_datetime: str,
                      secrets: Dict) -> Dict:
    """Makes a call to datadog logs query. To search for log containing
    sender email, recipient email relating to transaction ID
    Args:
        trx_id: transaction ID to query
        from_datetime: format yyyy-mm-ddThh:mm:ssZ
        to_datetime: format yyyy-mm-ddThh:mm:ssZ
        secrets: secrets obtained from get_secret()
    Returns:
        inspect if dict contains 'statusCode' key, if it does
        an issue had occoured. if a successful response from
        /v1/logs-queries/list evaluate the 'logs' key

    """
    session = requests.Session()
    session.headers = {
        'DD-API-KEY': secrets['DL-WATCHER']['DD_API_KEY'],
        'DD-APPLICATION-KEY': secrets['DL-WATCHER']['DD_APP_KEY'],
        'Content-Type': 'application/json',
        'Cookie': 'DD-PSHARD=0'
    }
    #TODO Add to restrict to 1 in payload
    payload = f"{{ \"query\": \"@transaction_id:{trx_id} service:filetrust-smtpreceiver +From +To\",\"time\" : {{\"from\": \"{from_datetime}\",\"to\": \"{to_datetime}\"}}}}"
    response = session.post(
        "https://api.datadoghq.eu/api/v1/logs-queries/list", data=payload)

    if response.status_code != 200:
        return {
            "statusCode": response.status_code,
            "body": response.text
        }

    return json.loads(response.text)

def __datadog_request_tenant_id(trx_id: str, from_datetime: str, to_datetime: str,
                      secrets: Dict) -> Dict:
    """Makes a call to datadog logs query. To search for log containing
    sender email, recipient email relating to transaction ID
    Args:
        trx_id: transaction ID to query
        from_datetime: format yyyy-mm-ddThh:mm:ssZ
        to_datetime: format yyyy-mm-ddThh:mm:ssZ
        secrets: secrets obtained from get_secret()
    Returns:
        inspect if dict contains 'statusCode' key, if it does
        an issue had occoured. if a successful response from
        /v1/logs-queries/list evaluate the 'logs' key

    """
    session = requests.Session()
    session.headers = {
        'DD-API-KEY': secrets['DL-WATCHER']['DD_API_KEY'],
        'DD-APPLICATION-KEY': secrets['DL-WATCHER']['DD_APP_KEY'],
        'Content-Type': 'application/json',
        'Cookie': 'DD-PSHARD=0'
    }
    #TODO Add to restrict to 1 in payload
    payload = f"{{ \"query\": \"@transaction_id:{trx_id} +Tenant ID header value is\",\"time\" : {{\"from\": \"{from_datetime}\",\"to\": \"{to_datetime}\"}} }}"
    response = session.post(
        "https://api.datadoghq.eu/api/v1/logs-queries/list", data=payload)

    if response.status_code != 200:
        return {
            "statusCode": response.status_code,
            "body": response.text
        }

    return json.loads(response.text)

def __has_detected_issues(dd_response: Dict) -> Tuple[bool, Union[Dict, None]]:
    """Analyzes the response from __datadog_request() in order to
    determine any issues from the function.
    Args:
        dd_response: the return from __datadog_request()
    Returns:
        tuple of issues detected as boolean and response as Dict
        True: Issue found, False: No known issues found
        response will contain error message in format to go into slack block
    """
    issues_detected = False
    response = None

    if "statusCode" in dd_response and dd_response['statusCode'] != 200:
            response = {
                "tenant_name": dd_response["body"],
                "sender_email": dd_response["body"],
                "recipient_email": dd_response["body"]
            }

    if len(dd_response['logs']) < 1:
        _error = "Cannot Find in DataDog Log"
        response = {
            "tenant_name": _error,
            "sender_email": _error,
            "recipient_email": _error
        }

    if response != None:
        issues_detected = True

    return issues_detected, response

def datadog_log_query(message_id: str, event_time: datetime.datetime,
                      secrets: Dict) -> Dict:
    """Makes a call to datadog logs query. To search for log containing
    sender email, recipient email relating to transaction ID
    Args:
        message_id: the message ID used as transaction id in query
        event_time: a datetime obj where the query will search
        from 5 days before event_time to value of event_time
        secrets: secrets obtained from get_secret()
    Returns:
        response to contain attributes
    """
    from_string_time = set_datetime(event_time - datetime.timedelta(days=5))
    to_string_time = set_datetime(event_time)

    dd_response_emails = __datadog_request_emails(message_id, from_string_time,
                                    to_string_time, secrets)

    issues_detected, response = __has_detected_issues(dd_response_emails)
    if issues_detected == True:
        return response

    dd_response_tenant = __datadog_request_tenant_id(message_id, from_string_time, to_string_time, secrets)
    issues_detected, response = __has_detected_issues(dd_response_tenant)
    if issues_detected == True:
        return response


    emails = dd_response_emails['logs'][0]['content']['attributes']
    tenant = dd_response_tenant['logs'][0]['content']['attributes']

    return {
        'timestamp': dd_response_tenant['logs'][0]['content']['timestamp'],
        'tenant_name': tenant['tenant_name'],
        'sender_email': emails['sender_email'],
        'recipient_email': emails['recipient_email']
    }
