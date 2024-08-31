import choose_day as gw
import pytest
# Tests for choose week


def test_choose_valid_day():
    # Arrange
    x: list[str] = ['1', '2', '3', '4', '5', '6', '7'];
    expected: list[str] = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    # Act
    actual: list[str] = [];
    for item in x:
        actual.append(gw.check_day(item));

    # Assert
    assert actual == expected;


def test_choose_invalid_day():
    # Arrange
    x: str = "0";

    with pytest.raises(ValueError) as ex:
        gw.check_day(x);

    # Assert
    assert str(ex.value) == "number out of range";


def test_choose_invalid_input():
    # Arrange
    x: str = "srg";

    with pytest.raises(ValueError) as ex:
        gw.check_day(x);

    # Assert
    assert str(ex.value) == "number cannot contain letters. Please enter a valid number";

