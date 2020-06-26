import datetime

def get_datetime(event_utc_time: str):
    #Check if milliseconds in event_utc_time, if so remove
    if "." in event_utc_time:
        new_time = event_utc_time.split(".")
        event_utc_time = new_time[0]

    return datetime.datetime.fromisoformat(event_utc_time)

def set_datetime(datetime_obj):
    return  datetime_obj.isoformat() + "Z"