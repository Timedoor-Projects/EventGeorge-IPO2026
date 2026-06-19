while True:
    print("=================================")
    print("IPO QUIZ GAME 2026")
    print("=================================")
    print("Test Your Knowledge Here!")
    print("=================================")
    name = input("Enter your name: ")
    print()
    print("Hello, " + name + "! Welcome to the Quiz Game! ")
    print()
    print(">=>=>=>=>=>=>=>=>=>=>=>")
    print("Choose a Category:")
    print("1. Animals")
    print("2. Science")
    print("3. Math")
    print(">=>=>=>=>=>=>=>=>=>=>=>=>")
    choice = input("Enter your choice (1/2/3): ")
    print()
    score = 0
    total_questions = 5

    if choice == "1":
        print("You chose ANIMALS")
        print("-----------------")
        print("Question 1:")
        print("What is the largest animal in the world?")
        answer1 = input("Your answer: ")
        answer1 = answer1.lower()
    if answer1 == "blue whale":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: blue whale")
    print()
    print("Question 2:")
    print("What animal can fly and lay eggs?")
    answer2 = input("your answer: ")
    answer2 = answer2.lower()
    if answer2 == "bird":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: bird")
    print()
    print("Question 3:")
    print("What do you call the process when animals sleep through winter?")
    answer3 = input("your answer: ")
    answer3 = answer3.lower()
    if answer3 == "hibernation":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: hibernation")
    print()
    print("Question 4:")
    print("What eight-legged animal spins webs?")
    answer4 = input("your answer: ")
    answer4 = answer4.lower()
    if answer4 == "spider":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: spider")
    print()
    print("Question 5:")
    print("What animal sheds its skin to grow?")
    answer5 = input("your answer: ")
    answer5 = answer5.lower()
    if answer5 == "snake":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: snake")
    print()
    percentage = (score * 100) // total_questions
    print(":):):):):):):):):):):):):):):):):):)")
    print("FINAL RESULT - " + name)
    print(":):):):):):):):):):):):):):):):):):)")
    print("Score      :", score, "out of", total_questions)
    print("Percentage :", str(percentage) + "%")
    print(":):):):):):):):):):):):):):):):):):)")

    if percentage >= 80:
        print("Excellent!")
    elif percentage >= 60:
        print("Great Job")
    else:
        print("Keep Practicing!")

    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print()
    play_again = input("Play again? (y/n): ").lower()
    print()

    if play_again != "y":
        print("=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]")
        print("Thanks for playing, " + name + "!")
        print("Good bye :) !")
        print("=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]")
        break

    if choice == "2":
        print("You chose: SCIENCE")
    print("------------------")
    print()
    print("Question 1:")
    print("What is the largest planet in our solar system?")
    answer1 = input("Your answer: ")
    answer1 = answer1.lower()
    if answer1 == "jupiter":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: jupiter")
    print()
    print("Question 2:")
    print("What do plants need to make their own food?")
    answer2 = input("your answer: ")
    answer2 = answer2.lower()
    if answer2 == "sunlight" or answer2 == "sun":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is sunlight")
    print()
    print("Question 3:")
    print("What gas do we breath in to stay alive?")
    answer3 = input("Your answer: ")
    answer3 = answer3.lower()
    if answer3 == "oxygen":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: oxygen")
    print()
    print("Question 4:")
    print("How many planets are in our solar system?")
    answer4 = input("Your answer: ")
    answer4 = answer4.lower()
    if answer4 == "8":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: 8")
    print()
    print("Question 5:")
    print("What is the process called when plants make food using sunlight?")
    answer5 = input("Your answer: ")
    answer5 = answer5.lower()
    if answer5 == "photosynthesis":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: photosynthesis")
        print()
    percentage = (score * 100) // total_questions
    print(":):):):):):):):):):):):):):):):):):)")
    print("FINAL RESULT - " + name)
    print(":):):):):):):):):):):):):):):):):):)")
    print("Score      :", score, "out of", total_questions)
    print("Percentage :", str(percentage) + "%")
    print(":):):):):):):):):):):):):):):):):):)")

    if percentage >= 80:
        print("Excellent!")
    elif percentage >= 60:
        print("Great Job")
    else:
        print("Keep Practicing!")

        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print()
        play_again = input("Play again? (y/n): ").lower()
        print()

        if play_again != "y":
            print("=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]")
            print("Thanks for playing, " + name + "!")
            print("Good bye :) !")
            print("=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]")
            break

    if choice == "3":
        print("You chose: MATH")
        print("---------------")
        print()
    print("Question 1: ")
    print("What is 7 x 8?")
    answer1 = input("Your answer: ")
    if answer1 == "56":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: 56")
    print()
    print("Question 2:")
    print("What is 100 - 37?")
    answer2 = input("your answer: ")
    if answer2 == "63":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: 63")
        print()
    print("Question 3:")
    print("What is 15 + 28?")
    answer3 = input("your answer: ")
    if answer3 == "43":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: 43")
    print()
    print("Question 4:")
    print("What is 144 : 12?")
    answer4 = input("your answer: ")
    if answer4 == "12":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: 12")
    print()
    print("Question 5:")
    print("What is the area of a square with a side length of 9?")
    answer5 = input("your answer: ")
    if answer5 == "81":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is: 81")
        print()
        percentage = (score * 100) // total_questions
        print(":):):):):):):):):):):):):):):):):):)")
        print("FINAL RESULT - " + name)
        print(":):):):):):):):):):):):):):):):):):)")
        print("Score      :", score, "out of", total_questions)
        print("Percentage :", str(percentage) + "%")
        print(":):):):):):):):):):):):):):):):):):)")

        if percentage >= 80:
            print("Excellent!")
        elif percentage >= 60:
            print("Great Job")
        else:
            print("Keep Practicing!")

        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print()
        play_again = input("Play again? (y/n): ").lower()
        print()

        if play_again != "y":
            print("=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]")
            print("Thanks for playing, " + name + "!")
            print("Good bye :) !")
            print("=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]=]")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
            continue
