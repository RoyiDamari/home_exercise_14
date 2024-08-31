import random


def prepare_board() -> dict[tuple[int, int], dict[str, any]]:
    rows: int = 4;
    columns: int = 4;
    cards: list[str] = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H'];

    random.shuffle(cards);
    board: dict[tuple[int, int], dict[str, any]] = {};
    card_index: int = 0;

    for row in range(rows):
        for col in range(columns):
            flipped = random.choice([True, False]);
            matched = False;
            if flipped:
                # If the card is flipped, randomly decide if it is also matched
                matched = random.choice([True, False]);

            board[(row, col)]: dict[str, any] = {
                'card': cards[card_index],
                'flipped': flipped,
                'matched': matched
            }
            card_index += 1;

    return board;


def flipped_card_check(board: dict[tuple[int, int], dict[str, any]], row: str, col: str, rows: int, columns: int) -> str:
    row: int = int(row);
    col: int = int(col);

    if row < 0 or row >= rows:
        raise IndexError(f"Invalid position. Row {row} is out of bounds.");

    if col < 0 or col >= columns:
        raise IndexError(f"Invalid position. Column {col} is out of bounds.");

    position: tuple[int, int] = (row, col);
    card_info: dict[str, any] = board[position];

    if card_info['matched']:
        return "This card has already been matched. Please select another position.";

    if card_info['flipped']:
        return "This card is already flipped. Please select another position.";

    return "This position is valid.";


def attempt_flip(board_game: dict[tuple[int, int], dict[str, any]]) -> None:
    rows: int = 4;
    columns: int = 4;

    while True:
        try:
            row: str = input(f"Enter the row number (0 to {rows - 1}): ");
            flipped_card_check(board_game, row, "0", rows, columns);

            row: int = int(row);

            all_flipped_or_matched: bool = all(
                board_game[(row, c)]['flipped'] or board_game[(row, c)]['matched'] for c in range(columns));

            if all_flipped_or_matched:
                print("All cards in this row are already flipped or matched. Please select another row.")
                continue;  # Ask for another row

            break;

        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter an integer value.");

        except IndexError:
            # Handle invalid position
            print("Invalid input. Please enter a valid index.")

    while True:
        try:
            col: str = input(f"Enter the column number (0 to {columns - 1}): ");
            result: str = flipped_card_check(board_game, str(row), col, rows, columns);

            col: int = int(col);
            position: tuple[int, int] = (row, col);

            if board_game[position]['matched'] or board_game[position]['flipped']:
                print(result);
                continue;
            else:
                print(result);
                break;

        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter an integer value.");

        except IndexError:
            # Handle invalid position
            print("Invalid input. Please enter a valid index.");


if __name__ == '__main__':
    # Initialize the game
    initial_board: dict[tuple[int, int], dict[str, any]] = prepare_board();
    attempt_flip(initial_board);