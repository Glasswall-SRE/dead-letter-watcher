import datetime


def get_datetime(event_utc_time: str) -> datetime.datetime:
    """Create a datetime object from the argument event_utc_time
    Args:
        event_utc_time: str in utc form of the datetime to process.
        Note: millisecond figure will be truncated and removed if present.
        This truncation is REQUIRED for use in the DataDog Log API
        If there is a failure to parse the string, a RECOVERY ATTEMPT
        will occour by returning the date time of now

    Returns:
        datetime object of string parsed, otherwise datetime of NOW
    """
    try:
        #Check if milliseconds in event_utc_time, if so remove
        if "." in event_utc_time:
            new_time = event_utc_time.split(".")
            event_utc_time = new_time[0]

        return datetime.datetime.fromisoformat(event_utc_time)
    except ValueError:
        # Could not parse get now time instead
        return datetime.datetime.now()

def set_datetime(datetime_obj: datetime.datetime) -> str:
    """Create an iso standard datetime string, for query usage e.g. datadog.py
    Args:
        datetime_obj: a populate datetime object

    Returns:
        string in iso format as such `yyyy-mm-ddThh:mm:ssZ`
    """
    return datetime_obj.strftime('%Y-%m-%dT%H:%M:%SZ')
