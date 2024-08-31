import guess_number as gn
import pytest
# Tests for guess number game


def test_guess_correct():
    # Arrange
    x: int = 50;
    y: int = 50;
    expected: str = "BINGO";

    # Act
    actual: str = gn.check_guess(x, y);

    # Assert
    assert actual == expected;


def test_guess_higher():
    # Arrange
    x: int = 50;
    y: int = 20;
    expected: str = "guess higher";

    # Act
    actual: str = gn.check_guess(x, y);

    # Assert
    assert actual == expected


def test_guess_lower():
    # Arrange
    x: int = 20;
    y: int = 50;
    expected: str = "guess lower";

    # Act
    actual: str = gn.check_guess(x, y);

    # Assert
    assert actual == expected;


def test_guess_invalid_input():
    # Arrange
    x: int = 20;
    y: str = "forty_two";

    with pytest.raises(ValueError) as ex:
        gn.check_guess(x, y);


def test_guess_number_positive_out_of_range():
    # Arrange
    x: int = 20;
    y: int = 144;

    with pytest.raises(ValueError) as ex:
        gn.check_guess(x, y);

    # Assert
    assert str(ex.value) == "number out of range";


def test_guess_number_negative_out_of_range():
    # Arrange
    x: int = 20;
    y: int = -20;

    with pytest.raises(ValueError) as ex:
        gn.check_guess(x, y);

    # Assert
    assert str(ex.value) == "number out of range";