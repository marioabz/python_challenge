import pytest

from data_capture import DataCapture


@pytest.fixture
def data_capture() -> DataCapture:
    return DataCapture()


@pytest.fixture
def sequential_numbers_to_1000() -> list:

    return [i for i in range(1, 1001)]


@pytest.fixture
def fraction_of_sequential_numbers_to_50() -> list:
    return [i for i in range(1, 51)]


@pytest.fixture
def number_5_repeated_100_times() -> list:
    return [5 for _ in range(100)]


@pytest.fixture
def number_1000_repeated_10_times() -> list:
    return [1000 for _ in range(10)]


@pytest.fixture
def limits_repeated_10_times_each() -> list:
    return [1 for _ in range(10)] + [1000 for _ in range(10)]
