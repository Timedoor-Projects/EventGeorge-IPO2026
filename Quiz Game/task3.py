# ================================================
# TASK 3 - Final Project: IPO Quiz Game 2026
# Developed from Task 2
# Name: [Write your name here]
# ================================================

# Main loop - the program keeps running until the player chooses to quit
while True:

    # ============================================
    # OPENING SCREEN
    # ============================================
    print()
    print("=================================")
    print("       IPO QUIZ GAME 2026        ")
    print("=================================")
    print("    Test Your Knowledge Here!    ")
    print("=================================")
    print()

    # Player enters their name
    name = input("Enter your name: ")
    print()
    print("Hello, " + name + "! Welcome to the Quiz Game!")
    print()

    # ============================================
    # CATEGORY MENU
    # ============================================
    print("=================================")
    print("Choose a Category:")
    print("1. Animals")
    print("2. Science")
    print("3. Math")
    print("=================================")
    print()

    choice = input("Enter your choice (1/2/3): ")
    print()

    # Reset score at the start of each round
    score = 0
    total_questions = 5

    # ============================================
    # CATEGORY 1 - ANIMALS (5 Questions)
    # ============================================
    if choice == "1":
        print("You chose: ANIMALS")
        print("---------------------------------")
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

        # Question 4
        print("Question 4:")
        print("What eight-legged animal spins webs?")
        answer = input("Your answer: ").lower()
        if answer == "spider":
            print("Correct!")
            score = score + 1
        else:
            print("Wrong! The correct answer is: spider")
        print()

        # Question 5
        print("Question 5:")
        print("What animal sheds its skin to grow?")
        answer = input("Your answer: ").lower()
        if answer == "snake":
            print("Correct!")
            score = score + 1
        else:
            print("Wrong! The correct answer is: snake")
        print()

    # ============================================
    # CATEGORY 2 - SCIENCE (5 Questions)
    # ============================================
    elif choice == "2":
        print("You chose: SCIENCE")
        print("---------------------------------")
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

        # Question 4
        print("Question 4:")
        print("How many planets are in our solar system?")
        answer = input("Your answer: ")
        if answer == "8":
            print("Correct!")
            score = score + 1
        else:
            print("Wrong! The correct answer is: 8")
        print()

        # Question 5
        print("Question 5:")
        print("What is the process called when plants make food using sunlight?")
        answer = input("Your answer: ").lower()
        if answer == "photosynthesis":
            print("Correct!")
            score = score + 1
        else:
            print("Wrong! The correct answer is: photosynthesis")
        print()

    # ============================================
    # CATEGORY 3 - MATH (5 Questions)
    # ============================================
    elif choice == "3":
        print("You chose: MATH")
        print("---------------------------------")
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

        # Question 4
        print("Question 4:")
        print("What is 144 divided by 12?")
        answer = input("Your answer: ")
        if answer == "12":
            print("Correct!")
            score = score + 1
        else:
            print("Wrong! The correct answer is: 12")
        print()

        # Question 5
        print("Question 5:")
        print("What is the area of a square with a side length of 9?")
        answer = input("Your answer: ")
        if answer == "81":
            print("Correct!")
            score = score + 1
        else:
            print("Wrong! The correct answer is: 81")
        print()

    # ============================================
    # INVALID CHOICE
    # ============================================
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
        print()
        continue

    # ============================================
    # FINAL RESULT
    # ============================================
    percentage = (score * 100) // total_questions

    print("=================================")
    print("FINAL RESULT - " + name)
    print("=================================")
    print("Score      :", score, "out of", total_questions)
    print("Percentage :", str(percentage) + "%")
    print("=================================")

    if percentage >= 80:
        print("Excellent Python Coder!")
    elif percentage >= 60:
        print("Great Job!")
    else:
        print("Keep Practicing!")

    print("=================================")
    print()

    # ============================================
    # PLAY AGAIN OPTION
    # ============================================
    play_again = input("Play again? (y/n): ").lower()
    print()

    if play_again != "y":
        print("=================================")
        print("Thanks for playing, " + name + "!")
        print("See you at IPO 2026!")
        print("=================================")
        break
