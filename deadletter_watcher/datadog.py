import requests
from deadletter_watcher.util import set_datetime
import datetime
import json

def validate(secrets):
    """Validates datadog API key by contacting GET validate HTTP Request
    Args:
        secrets: access to the DD_API_KEY required
    Returns:
        response from validate GET request
    """
    validate_headers = {
            'DD-API-KEY': secrets['DL-WATCHER']['DD_API_KEY'],
        }
    validation_session = requests.Session()
    validation_session.headers = validate_headers
    response = validation_session.get("https://api.datadoghq.eu/api/v1/validate")
    return response

def __datadog_request(trx_id: str, from_datetime: str, to_datetime: str, secrets):
    """Makes a call to datadog logs query. To search for log containing
    sender email, recipient email relating to transaction ID
    Args:
        trx_id: transaction ID to query
        from_datetime: format yyyy-mm-ddThh:mm:ssZ
        to_datetime: format yyyy-mm-ddThh:mm:ssZ
        secrets: secrets obtained from get_secret()
    Returns:
        response from /v1/logs-queries/list
    """
    session = requests.Session()
    session.headers = {
        'DD-API-KEY' : secrets['DL-WATCHER']['DD_API_KEY'],
        'DD-APPLICATION-KEY' : secrets['DL-WATCHER']['DD_APP_KEY'],
        'Content-Type': 'application/json',
        'Cookie': 'DD-PSHARD=0'
    }
    # Add to restrict to 1 in payload
    payload = f"{{ \"query\": \"@transaction_id:{trx_id} service:filetrust-smtpreceiver +From +To\",\"time\" : {{\"from\": \"{from_datetime}\",\"to\": \"{to_datetime}\"}}}}"
    response = session.post("https://api.datadoghq.eu/api/v1/logs-queries/list", data=payload)
    return response


def datadog_log_query(message_id: str, event_time, secrets):
    """Makes a call to datadog logs query. To search for log containing
    sender email, recipient email relating to transaction ID
    Args:
        message_id: the message ID used as transaction id in query
        event_time: a datetime obj where the query will search 
        from 5 days before event_time to value of event_time
        secrets: secrets obtained from get_secret()
    Returns:
        response from /v1/logs-queries/list
    """
    from_string_time = set_datetime(event_time - datetime.timedelta(days=2))
    to_string_time = set_datetime(event_time)

    dd_response = __datadog_request(message_id, from_string_time, to_string_time, secrets)

    response = json.loads(dd_response.text)

    return response['logs'][0]['content']['attributes']
