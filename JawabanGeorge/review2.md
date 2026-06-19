**# Task 2: Some things that need improvement**

1. The `if/elif/else` part isn't entirely correct. No matter which category the player chooses, all 9 questions will appear. This is because the questions end up outside the if block, not inside it:

```py
# incorrect:
if choice == "1":
    print("You chose Animal")

print("Question 1:")  # this runs no matter what

# should be:
if choice == "1":
    print("You chose Animal")
    print("Question 1:")  # indented to only run when choice is "1"
```

2. Bug in Science Question 2 The way or is written, the answer is always correct even if the player types something wrong:

```py
# always True — bug!:
if answer2 == "sunlight" or "sun":

# should be:
if answer2 == "sunlight" or answer2 == "sun":
```

3. Missing invalid input handling If the player types something like "9", the program does nothing. Need to add an else at the end:

```py
else:
print("Invalid choice! Please enter 1, 2, or 3.")
```

4. Small things to fix
   - Typo on the input prompt: "Enter you choice" → "Enter your choice"
