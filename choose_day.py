# Exercise 1
import random


def check_day(user_choice: str) -> str:

    match user_choice:
        case "1":
            return "Sunday";
        case "2":
            return "Monday";
        case "3":
            return "Tuesday";
        case "4":
            return "Wednesday";
        case "5":
            return "Thursday";
        case "6":
            return "Friday";
        case "7":
            return "Saturday";
        case _:
            if any(char.isalpha() for char in user_choice):
                raise ValueError("number cannot contain letters. Please enter a valid number");
            else:
                raise ValueError("number out of range");


def choose_day() -> None:

    while True:
        try:

            user_choice: str = input("Please choose a day in the week (1-7) : ");
            result: str = check_day(user_choice);
            print(result);
            return;

        except ValueError as e:
            print(e);