# ================================================
# TASK 2 - Quiz with Categories
# Developed from Task 1
# ================================================

# Variable to store the score
score = 0

# --- Quiz Title ---
print("=========================")
print("         QUIZ GAME       ")
print("=========================")
print()

# --- Category Menu ---
print("Choose a Category:")
print("1. Animals")
print("2. Science")
print("3. Math")
print()

choice = input("Enter your choice (1/2/3): ")
print()

# ================================================
# CATEGORY 1 - ANIMALS
# ================================================
if choice == "1":
    print("You chose: ANIMALS")
    print("-------------------------")
    print()

    # Question 1
    print("Question 1:")
    print("What is the largest animal in the world?")
    answer = input("Your answer: ").lower()
    if answer == "whale":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: whale")
    print()

    # Question 2
    print("Question 2:")
    print("What animal can fly and lay eggs?")
    answer = input("Your answer: ").lower()
    if answer == "bird":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: bird")
    print()

    # Question 3
    print("Question 3:")
    print("What do you call the process when animals sleep through winter?")
    answer = input("Your answer: ").lower()
    if answer == "hibernation":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: hibernation")
    print()

# ================================================
# CATEGORY 2 - SCIENCE
# ================================================
elif choice == "2":
    print("You chose: SCIENCE")
    print("-------------------------")
    print()

    # Question 1
    print("Question 1:")
    print("What is the largest planet in our solar system?")
    answer = input("Your answer: ").lower()
    if answer == "jupiter":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: jupiter")
    print()

    # Question 2
    print("Question 2:")
    print("What do plants need to make their own food?")
    answer = input("Your answer: ").lower()
    if answer == "sunlight" or answer == "sun":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: sunlight")
    print()

    # Question 3
    print("Question 3:")
    print("What gas do we breathe in to stay alive?")
    answer = input("Your answer: ").lower()
    if answer == "oxygen":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: oxygen")
    print()

# ================================================
# CATEGORY 3 - MATH
# ================================================
elif choice == "3":
    print("You chose: MATH")
    print("-------------------------")
    print()

    # Question 1
    print("Question 1:")
    print("What is 7 x 8?")
    answer = input("Your answer: ")
    if answer == "56":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: 56")
    print()

    # Question 2
    print("Question 2:")
    print("What is 100 - 37?")
    answer = input("Your answer: ")
    if answer == "63":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: 63")
    print()

    # Question 3
    print("Question 3:")
    print("What is 15 + 28?")
    answer = input("Your answer: ")
    if answer == "43":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: 43")
    print()

# ================================================
# INVALID CHOICE
# ================================================
else:
    print("Invalid choice! Please enter 1, 2, or 3.")

# ================================================
# FINAL RESULT
# ================================================
print("=========================")
print("Your score:", score, "out of 3")
print("=========================")
