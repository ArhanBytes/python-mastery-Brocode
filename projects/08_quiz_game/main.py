questions = (
    "Which data structure uses FIFO (First In, First Out) principle?: ",
    "Which sorting algorithm has the best average-case time complexity?: ",
    "Which data structure is used in implementing recursion?: ",
    "Which algorithm is commonly used to find the shortest path in a graph?: ",
    "Which data structure provides fast lookup using keys?: ",
    "Which traversal method visits nodes in the order: Left, Root, Right?: ",
    "Which algorithm technique divides a problem into subproblems and combines solutions?: ",
    "Which data structure is best suited for implementing undo operations in text editors?: "
)

options = (
    ("A. Stack", "B. Queue", "C. Linked List", "D. Tree"),
    ("A. Bubble Sort", "B. Merge Sort", "C. Insertion Sort", "D. Selection Sort"),
    ("A. Queue", "B. Array", "C. Stack", "D. Hash Table"),
    ("A. Dijkstra’s Algorithm", "B. Binary Search", "C. Quick Sort", "D. BFS"),
    ("A. Array", "B. Hash Map", "C. Stack", "D. Linked List"),
    ("A. Preorder", "B. Inorder", "C. Postorder", "D. Level Order"),
    ("A. Greedy", "B. Divide and Conquer", "C. Dynamic Programming", "D. Backtracking"),
    ("A. Queue", "B. Stack", "C. Linked List", "D. Tree")
)

answers = ("B", "B", "C", "A", "B", "B", "B", "B")
guesses = []
scores = 0
question_num = 0

# printing question
for question in questions:
    print("--------------------------")  
    print(question)
    # printing options to that question
    for option in options[question_num]:
        print(option)

    while True:
        guess = input("Enter (A,B,C,D): ").upper()
        if not (guess == "A" or  guess == "B"  or  guess == "C"  or  guess == "D"):
            print(f"{guess} is an invalid option")
        else:
            break 
    if guess == answers[question_num]:
        print("Correct")
        scores += 1
    else:
        for option in options[question_num]:
            if option.find(answers[question_num], 0, 1) == 0:
                print(f"Incorrect!\n{option} is the correct answer")
                break
    
    guesses.append(guess)
    question_num += 1
    
print("Your Guess: ", end = "\t")
for guess in guesses:
    print(guess, end = " ")

print("\nRight Answer: ", end = "\t")
for answer in answers:
    print(answer, end=" ")
    
print(f"\nScore: {int(scores/len(questions) * 100)}%")