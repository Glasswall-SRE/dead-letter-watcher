import requests
from deadletter_watcher.util import set_datetime
import datetime
import json

def validate(secrets):
    validate_headers = {
            'DD-API-KEY': secrets['DL-WATCHER']['DD_API_KEY'],
        }
    validation_session = requests.Session()
    validation_session.headers = validate_headers
    response = validation_session.get("https://api.datadoghq.eu/api/v1/validate")

def datadog_request(trx_id: str, from_datetime: str, to_datetime: str, secrets):
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
    trx_id = message_id
    from_string_time = set_datetime(event_time - datetime.timedelta(days=2))
    to_string_time = set_datetime(event_time)

    dd_response = datadog_request(trx_id, from_string_time, to_string_time, secrets)

    response = json.loads(dd_response.text)

    return response['logs'][0]['content']['attributes']
