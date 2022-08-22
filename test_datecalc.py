from datecalc import duration, when
from datetime import datetime


def test_zero_duration():
    # Arrange
    start_date = date.today()
    end_date = date.today()
    expected_output = 0

    # Act
    actual_output = duration(start_date, end_date)

    # Assert
    assert actual_output == expected_output

def test_zero_when():
    # Arrange
    start_date = date.today()
    days_between = 0
    expected_output = date.today()

    # Act
    actual_output = when(start_date, days_between)

    # Assert
    assert actual_output == expected_output
