import pytest
import deadletter_watcher.util
import datetime


def test_get_datetime_good_input():
    # Arrange
    parameter = "2020-06-26T14:58:24.3713213Z"
    # Act
    datetime_obj = deadletter_watcher.util.get_datetime(parameter)
    # Assert
    assert datetime_obj.year == 2020 and \
        datetime_obj.month == 6 and \
        datetime_obj.day == 26 and \
        datetime_obj.hour == 14 and \
        datetime_obj.minute == 58 and \
        datetime_obj.second == 24


def test_get_datetime_good_input_no_microseconds():
    # Arrange
    parameter = "2020-06-26T14:58:24"
    # Act
    datetime_obj = deadletter_watcher.util.get_datetime(parameter)
    # Assert
    assert datetime_obj.year == 2020 and \
        datetime_obj.month == 6 and \
        datetime_obj.day == 26 and \
        datetime_obj.hour == 14 and \
        datetime_obj.minute == 58 and \
        datetime_obj.second == 24


def test_get_datetime_bad_input():
    # Arrange
    parameter = "rubbish value"
    # Act
    now = deadletter_watcher.util.get_datetime(parameter)
    # Assert
    # Justification for assert. The NOW value obtained will be slight greater
    # than obtained a few miliseconds ago.
    assert datetime.datetime.now() >= now


def test_set_datetime_good_input():
    # Arrange
    datetime_obj = datetime.datetime(year=2020,
                                     month=5,
                                     day=23,
                                     hour=15,
                                     minute=10,
                                     second=0)
    # Act
    output = deadletter_watcher.util.set_datetime(datetime_obj)
    # Assert
    assert output == "2020-05-23T15:10:00Z"


def test_set_datetime_bad_input():
    # Arrange
    # Act
    # Assert
    with pytest.raises(Exception):
        deadletter_watcher.util.set_datetime(None)
