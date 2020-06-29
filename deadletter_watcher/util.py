import datetime


def get_datetime(event_utc_time: str) -> datetime.datetime:
    """Create a datetime object from the argument event_utc_time
    Args:
        event_utc_time: str in utc form of the datetime to process.
        Note: millisecond figure will be truncated and removed if present.
        This truncation is REQUIRED for use in the DataDog Log API

    Returns:
        datetime object
    """
    try:
        #Check if milliseconds in event_utc_time, if so remove
        if "." in event_utc_time:
            new_time = event_utc_time.split(".")
            event_utc_time = new_time[0]

        return datetime.datetime.fromisoformat(event_utc_time)
    except:
        raise ValueError(
            "Invalid event_utc_time, unable to create datetime object")


def set_datetime(datetime_obj: datetime.datetime) -> str:
    """Create an iso standard datetime string, for query usage e.g. datadog.py
    Args:
        datetime_obj: a populate datetime object

    Returns:
        string in iso format as such `yyyy-mm-ddThh:mm:ssZ`
    """
    return datetime_obj.strftime('%Y-%m-%dT%H:%M:%SZ')
