# Number Guessing Game
import random

lowest_num = 1
highest_num = 100
no_of_guesses = 0

answer = random.randint(lowest_num, highest_num)
is_running = True

print(f"Select a number between between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        no_of_guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between between {lowest_num} and {highest_num}")
        elif guess < answer:
            print(f"{guess} is low! Try again.")
        elif guess > answer:
            print(f"{guess} is high! Try again.")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of Guesses: {no_of_guesses}")
            is_running = False
        
                    
    else:
        print(f"{guess} is an invalid input.")
        print(f"Please select a number between between {lowest_num} and {highest_num}")
    