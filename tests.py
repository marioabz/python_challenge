import pytest

from data_capture import DataCapture
from custom_exceptions import OutOfRangeException, StatsNotUpdated
from fixtures import (
    data_capture,
    sequential_numbers_to_1000,
    fraction_of_sequential_numbers_to_50,
    number_5_repeated_100_times,
    number_1000_repeated_10_times,
    limits_repeated_10_times_each,
)
from utils import MAX_VALUE, MIN_VALUE


def test_data_capture_class(data_capture: DataCapture):
    assert data_capture


def test_data_capture_has_1000_elements(
    data_capture: DataCapture, sequential_numbers_to_1000: list
):
    obj = data_capture
    for number in sequential_numbers_to_1000:
        obj.add(number)
    obj.build_stats()

    assert obj.less(MAX_VALUE) == MAX_VALUE - 1
    assert obj.between(1, 10) == 10
    assert obj.greater(MAX_VALUE) == 0
    assert obj.less(MIN_VALUE) == 0


def test_data_capture_with_small_dataset(
    data_capture: DataCapture, fraction_of_sequential_numbers_to_50: list
):
    obj = data_capture
    for number in fraction_of_sequential_numbers_to_50:
        obj.add(number)
    obj.build_stats()
    assert obj.greater(50) == 0
    assert obj.less(51) == 50
    assert obj.between(1, 1000) == 50


def test_data_capture_repeated_number(
    data_capture: DataCapture, number_5_repeated_100_times: list
):
    obj = data_capture
    for number in number_5_repeated_100_times:
        obj.add(number)

    obj.build_stats()

    assert obj.less(5) == 0
    assert obj.greater(4) == 100


def test_data_capture_limit_number_repeated(
    data_capture: DataCapture,
    number_1000_repeated_10_times: list,
):
    obj = data_capture
    for number in number_1000_repeated_10_times:
        obj.add(number)

    obj.build_stats()

    assert obj.greater(999) == 10
    assert obj.less(1000) == 0


def test_data_capture_repeated_extremes(
    data_capture: DataCapture, limits_repeated_10_times_each: list
):
    obj = data_capture
    for number in limits_repeated_10_times_each:
        obj.add(number)

    obj.build_stats()

    assert obj.less(1000) == 10
    assert obj.greater(1) == 10
    assert obj.between(1, 1000) == 20


def tests_raises_out_of_range_exception(data_capture: DataCapture):
    obj = data_capture
    with pytest.raises(OutOfRangeException):
        obj.add(1001)
        assert True


def tests_raises_stats_not_updated(data_capture: DataCapture):
    obj = data_capture
    obj.add(1000)
    with pytest.raises(StatsNotUpdated):
        obj.less(1)
        assert True


def tests_raises_type_error(data_capture: DataCapture):
    obj = data_capture
    with pytest.raises(TypeError):
        obj.add("number")
        assert True
