import memory_board as mb
import pytest


# Tests for memory board


def test_handle_flip_attempt_invalid_row_position():
    # Arrange
    board: dict[tuple[int, int], dict[str, any]] = mb.prepare_board();
    rows: int = 4;
    columns: int = 4;
    row: str = "4";
    col: str = "3";

    with pytest.raises(IndexError) as ex:
        mb.flipped_card_check(board, row, col, rows, columns);  # Invalid position (out of bounds)

    assert str(ex.value) == f"Invalid position. Row {row} is out of bounds.";


def test_handle_flip_attempt_invalid_col_position():
    # Arrange
    board: dict[tuple[int, int], dict[str, any]] = mb.prepare_board();
    rows: int = 4;
    columns: int = 4;
    row: str = "3";
    col: str = "4";

    with pytest.raises(IndexError) as ex:
        mb.flipped_card_check(board, row, col, rows, columns);  # Invalid position (out of bounds)

    assert str(ex.value) == f"Invalid position. Column {col} is out of bounds.";


def test_handle_flip_attempt_already_flipped_or_matched():
    # Arrange
    board: dict[tuple[int, int], dict[str, any]] = mb.prepare_board();
    rows: int = 4;
    columns: int = 4;
    expected_message: list[str] = [];

    for position in board:
        if board[position]['matched']:
            message: str = "This card has already been matched. Please select another position.";
        elif board[position]['flipped']:
            message: str = "This card is already flipped. Please select another position.";
        else:
            message: str = "This position is valid.";

        expected_message.append(message);

    # Act
    results: list[str] = [];
    for row in range(rows):
        for col in range(columns):
            result = mb.flipped_card_check(board, str(row), str(col), rows, columns);
            results.append(result);

    print("Expected messages:", expected_message)
    print("Actual results:", results)

    # Assert
    assert results == expected_message;


def test_handle_flip_attempt_invalid_input_for_row():
    # Arrange
    board: dict[tuple[int, int], dict[str, any]] = mb.prepare_board();
    rows: int = 4;
    columns: int = 4;
    row: str = "ab";
    col: str = "3";

    with pytest.raises(ValueError) as ex:
        mb.flipped_card_check(board, row, col, rows, columns) # Invalid input;


def test_handle_flip_attempt_invalid_input_for_col():
    # Arrange
    board: dict[tuple[int, int], dict[str, any]] = mb.prepare_board();
    rows: int = 4;
    columns: int = 4;
    row: str = "3";
    col: str = "ab";

    with pytest.raises(ValueError) as ex:
        mb.flipped_card_check(board, row, col, rows, columns);  # Invalid input
