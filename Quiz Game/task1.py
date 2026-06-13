# ================================================
# TASK 1 - Simple Mini Quiz
# Topic: Animal Quiz
# ================================================

# Variable to store the score
score = 0

# --- Quiz Title ---
print("=========================")
print("Welcome to the Animal Quiz!")
print("=========================")
print()

# ------------------------------------------------
# QUESTION 1
# ------------------------------------------------
print("Question 1:")
print("What is the largest animal in the world?")
answer1 = input("Your answer: ")

# Convert to lowercase so "Whale" and "whale" are treated the same
answer1 = answer1.lower()

if answer1 == "whale":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is: whale")

print()

# ------------------------------------------------
# QUESTION 2
# ------------------------------------------------
print("Question 2:")
print("What animal can fly and lay eggs?")
answer2 = input("Your answer: ")

answer2 = answer2.lower()

if answer2 == "bird":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is: bird")

print()

# ------------------------------------------------
# QUESTION 3
# ------------------------------------------------
print("Question 3:")
print("What do you call the process when animals sleep through winter?")
answer3 = input("Your answer: ")

answer3 = answer3.lower()

if answer3 == "hibernation":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is: hibernation")

print()

# ------------------------------------------------
# FINAL RESULT
# ------------------------------------------------
print("=========================")
print("Your score:", score, "out of 3")
print("=========================")
