"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Adriana Martinkova
email: martinkova.adriana01@gmail.com
discord: adaadrisek123#8811
"""
import random
import time


def generate_four_digit_number():
    return str(random.randint(1000, 9999))


def get_user_input():
    while True:
        user_input = input("Enter a number: ")
        # checking whether the input can be casted to int
        try:
            user_input_int = int(user_input)
            if user_input_int >= 1000 and user_input_int <= 9999:
                return user_input
            else:
                raise
        except:
            print("Invalid input, insert number between 1000 and 9999")


def get_cows(secret_str, user_str):
    number_of_cows = 0
    for number in user_str:
        if number in secret_str:
            number_of_cows += 1
    return number_of_cows


def get_bulls(secret_str, user_str):
    number_of_bulls = 0
    for index in range(0, 4):
        if secret_str[index] == user_str[index]:
            number_of_bulls += 1
    return number_of_bulls


def print_intermediate_result(number_of_bulls, number_of_cows):

    if number_of_bulls == 1:
        bull = "bull"
    else:
        bull = "bulls"
    if number_of_cows == 1:
        cow = "cow"
    else:
        cow = "cows"
    print(f"{number_of_bulls} {bull}, {number_of_cows} {cow}")


def eval_game(number_of_guesses):
    if number_of_guesses < 4:
        print("That's amazing!")
    elif number_of_guesses < 10:
        print("That's average.")
    else:
        print("That's not so good :-(")


def introduce_user():
    print("Hi there!")
    print("-" * 50)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 50)


if __name__ == "__main__":
    introduce_user()
    start_time = time.time()
    number_of_guesses = 0
    secret_str = generate_four_digit_number()
    while True:
        user_str = get_user_input()
        number_of_guesses += 1
        # evaluate user input
        number_of_bulls = get_bulls(secret_str, user_str)
        number_of_cows = get_cows(secret_str, user_str) - number_of_bulls

        print_intermediate_result(number_of_bulls, number_of_cows)
        print("-" * 50)
        if number_of_bulls == 4:
            print(
                f"Correct, you've guessed the right number in {number_of_guesses} guess(es)!"
            )
            break
    eval_game(number_of_guesses)
    print(f"Your game took {time.time()-start_time:.2f} seconds")