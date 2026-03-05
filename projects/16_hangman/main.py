# Hangman GAME

from word_list import words
import random

# dictionary of key: ()
hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\"),
}


def display_man(wrong_guessed):
    print("*********************")
    print("\n".join(hangman_art[wrong_guessed]))
    print("*********************")


def display_hint(kind, hint):
    print(kind, end=": ")
    print(" ".join(hint))


def display_answer(kind, answer):
    print(kind, end=": ")
    print(" ".join(answer))


def main():
    kind = random.choice(list(words.keys()))
    answer = list(random.choice(words[kind]))
    hint = ["_"] * len(answer)
    wrong_guessed = 0
    guessed_letter = set()
    is_running = True

    while is_running:
        display_man(wrong_guessed)
        display_hint(kind, hint)
        guess = input("Enter a letter: ").lower()
        if len(guess) > 1 or guess > "z" or guess < "a":
            print(f"{guess} is an invalid guess")
            continue

        if guess in guessed_letter:
            print(f"{guess} has already been guessed")
            continue

        guessed_letter.add(guess)

        if guess in answer:
            for index in range(len(answer)):
                if guess == answer[index]:
                    hint[index] = answer[index]
        else:
            wrong_guessed += 1

        if "_" not in hint:
            display_man(wrong_guessed)
            display_answer(kind,answer)
            print("YOU WIN")
            is_running = False
        if wrong_guessed >= len(hangman_art) - 1:
            display_man(wrong_guessed)
            display_answer(kind,answer)
            print("YOU LOST")
            is_running = False


if __name__ == "__main__":
    main()
