# Exercise 1
import random


def check_guess(lucky_number: int, user_guess: str) -> str:
    number: int = int(user_guess);

    if number < 0 or number > 100:
        raise ValueError("number out of range");

    if number == lucky_number:
        return "BINGO";

    elif number > lucky_number:
        return "guess lower";

    else:
        return "guess higher";


def play_game() -> None:
    print("Wellcome to guess a number game");
    lucky_number: int = random.randint(0, 100);

    while True:
        try:

            user_guess: str = input("Please guess a number: ");
            result: str = check_guess(lucky_number, user_guess);
            print(result);

            if result == "BINGO":
                return;

        except ValueError as e:
            print(e);


