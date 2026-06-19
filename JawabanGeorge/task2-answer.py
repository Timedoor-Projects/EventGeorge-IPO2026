# Task 2 - Quiz with Categories
# Developed from Task 1
# Name: George

print("=========")
print("QUIZ GAME")
print("=========")
score = 0
print("Choose a Category:")
print("1. Animals")
print("2. Science")
print("3. Math")
choice = input("Enter you choice (1/2/3): ")
print()
if choice == "1":
    print("You chose Animals")
    print("-----------------")
    print()


print()
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
print("======================")
print("Your score:", score, "out of 3")
print("======================")


if choice == "2":
    print("You chose: Science")
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
if answer2 == "sunlight" or "sun":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is: sunlight")
    print()
print("Question 3:")
print("What gas do we breathe in to stay alive?")
answer3 = input("your answer: ")
answer3 = answer3.lower()
if answer3 == "oxygen":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is: oxygen")
    print()
print("======================")
print("Your score:", score, "out of 3")
print("======================")


if choice == "3":
    print("You chose: Math")
    print("---------------")
    print()

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
print("======================")
print("Your score:", score, "out of 3")
print("======================")
