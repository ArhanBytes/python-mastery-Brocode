# dice roll game
import random

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

dice = [] # it is list random generated die
total = 0
num_of_dice = int(input("How many dice?: "))

# generating random die
for i in range(num_of_dice):
    dice.append(random.randint(1,6))

# Printing Method 1: (horizontal Print)
# printing die art
# for i in range(num_of_dice):
#     # since it is tuple of multiple strings
#     for line in dice_art.get(dice[i]):
#         print(line)
        
# Printing Method 2: (Vertical Print)
for i in range(len(dice_art.get(1))): # outer loop will run length of our tuple(value) which is 5
    for die in dice: # inner loop will run number of dice
        print(dice_art.get(die)[i], end=" ")
    print()
    

# calculating total
for die in dice:
    total += die

print(f"Total: {total}")
