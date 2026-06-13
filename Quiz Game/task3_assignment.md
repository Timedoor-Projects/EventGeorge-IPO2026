# Task 3 - Final Project: IPO Quiz Game 2026

This is the last task, and it's where everything comes together.

We're going to take what you built in Task 2 and turn it into a complete, polished quiz game that's ready to submit to the International Python Olympiad. By the end, you'll have a program that asks for the player's name, lets them choose a category, goes through 5 questions, shows their score and percentage, gives them a message based on how well they did, and then asks if they want to play again.

It's more steps than the previous tasks, but we're going to go through it one piece at a time.

---

## What the final program should look like

```
=================================
       IPO QUIZ GAME 2026        
=================================
    Test Your Knowledge Here!    
=================================

Enter your name: George

Hello, George! Welcome to the Quiz Game!

=================================
Choose a Category:
1. Animals
2. Science
3. Math
=================================

Enter your choice (1/2/3): 1

You chose: ANIMALS
---------------------------------

Question 1:
What is the largest animal in the world?
Your answer: whale
Correct!

Question 2:
What animal can fly and lay eggs?
Your answer: bird
Correct!

Question 3:
What do you call the process when animals sleep through winter?
Your answer: sleep
Wrong! The correct answer is: hibernation

Question 4:
What eight-legged animal spins webs?
Your answer: spider
Correct!

Question 5:
What animal sheds its skin to grow?
Your answer: snake
Correct!

=================================
FINAL RESULT - George
=================================
Score      : 4 out of 5
Percentage : 80%
=================================
Excellent Python Coder!
=================================

Play again? (y/n): n

=================================
Thanks for playing, George!
See you at IPO 2026!
=================================
```

---

## Getting started

Open `task2.py` and save it as `task3.py`. Update the top comment:

```python
# Task 3 - Final Project: IPO Quiz Game 2026
# Developed from Task 2
# Name: ________________
```

---

## Let's go through the changes

### Part 1 — Wrap everything in a while loop

This is the biggest structural change. We want the game to keep running until the player decides to quit. In Python, we do that with `while True:`.

Go to the very beginning of your code (right after the comments) and add:

```python
while True:
```

Then indent everything below it by one level. Everything inside the `while True:` block will repeat each time the player finishes a round.

We'll add the `break` command later — that's what stops the loop when the player wants to quit.

---

### Part 2 — Make the title look nicer

Update the title borders from `=========================` to `=================================` (33 equal signs). Also add a subtitle line:

```
=================================
       IPO QUIZ GAME 2026        
=================================
    Test Your Knowledge Here!    
=================================
```

---

### Part 3 — Ask for the player's name

After the title, ask the player to type their name and save it in a variable called `name`:

```python
name = input("Enter your name: ")
print()
print("Hello, " + name + "! Welcome to the Quiz Game!")
print()
```

The `+` sign joins text together. So if `name` is `"George"`, the second line will print:
`Hello, George! Welcome to the Quiz Game!`

---

### Part 4 — Update the menu borders

Change the menu borders to match the new title style (`=================================`).

---

### Part 5 — Add total_questions variable

Before the `if choice == "1":` line, update your score setup to also include a `total_questions` variable:

```python
score = 0
total_questions = 5
```

We'll use `total_questions` when calculating the percentage later.

---

### Part 6 — Add 2 more questions to each category

Each category currently has 3 questions. We need to add 2 more to reach 5.

**2 more questions for Animals:**

Question 4: What eight-legged animal spins webs? → `spider`

Question 5: What animal sheds its skin to grow? → `snake`

**2 more questions for Science:**

Question 4: How many planets are in our solar system? → `8`
(no `.lower()` needed here since the answer is a number)

Question 5: What is the process called when plants make food using sunlight? → `photosynthesis`

**2 more questions for Math:**

Question 4: What is 144 divided by 12? → `12`

Question 5: What is the area of a square with a side length of 9? → `81`

Use the same question format as before — just add them after Question 3 in each category block.

---

### Part 7 — Add continue to the invalid choice

Find your `else:` block and add `continue` after the error message:

```python
else:
    print("Invalid choice! Please enter 1, 2, or 3.")
    print()
    continue
```

`continue` sends the player back to the top of the `while True` loop immediately, so they can choose again instead of seeing a broken result screen.

---

### Part 8 — Replace the old score display

Delete the old score lines at the bottom and replace them with the new result section.

First, calculate the percentage:
```python
percentage = (score * 100) // total_questions
```

`//` divides and rounds down. So if the player got 4 out of 5:
`(4 * 100) // 5` = `400 // 5` = `80`

Then show the result:
```python
print("=================================")
print("FINAL RESULT - " + name)
print("=================================")
print("Score      :", score, "out of", total_questions)
print("Percentage :", str(percentage) + "%")
print("=================================")
```

`str(percentage)` turns the number 80 into the text "80" so we can attach "%" to it.

---

### Part 9 — Add the result message

After the result box, add a message based on the percentage:

```python
if percentage >= 80:
    print("Excellent Python Coder!")
elif percentage >= 60:
    print("Great Job!")
else:
    print("Keep Practicing!")

print("=================================")
print()
```

So if they score 80% or more they get the best message, 60-79% gets the middle one, and anything below 60% gets the encouragement message.

---

### Part 10 — Add the play again option

This is the last piece. After the result section, ask the player if they want to go again:

```python
play_again = input("Play again? (y/n): ").lower()
print()

if play_again != "y":
    print("=================================")
    print("Thanks for playing, " + name + "!")
    print("See you at IPO 2026!")
    print("=================================")
    break
```

If the player types `y`, nothing happens here — the `while True` loop just goes back to the top and starts the game again.

If the player types anything else (like `n`), the `break` command stops the loop and the program ends.

---

## Test before you submit

Run `python3 task3.py` and go through these checks:

- Answer all 5 questions correctly → should show 100%, "Excellent Python Coder!"
- Answer 4 out of 5 correctly → 80%, "Excellent Python Coder!"
- Answer 3 out of 5 correctly → 60%, "Great Job!"
- Answer 2 out of 5 correctly → 40%, "Keep Practicing!"
- Try all 3 categories
- Type `y` at the end → game should restart with the title screen
- Type `n` at the end → goodbye message should appear and program ends
- Try typing an invalid category number → should show error and ask again

---

## Final checklist

- [ ] Saved as `task3.py` with your name in the comment
- [ ] Everything is inside `while True:`
- [ ] Title screen shows up
- [ ] Player name is asked and used
- [ ] Category menu shows up correctly
- [ ] Animals has 5 questions
- [ ] Science has 5 questions
- [ ] Math has 5 questions
- [ ] Each question shows Correct or Wrong
- [ ] Score counted correctly
- [ ] Percentage calculated correctly
- [ ] Result shows score, percentage, and message
- [ ] 80%+ shows "Excellent Python Coder!"
- [ ] 60-79% shows "Great Job!"
- [ ] Below 60% shows "Keep Practicing!"
- [ ] Player can play again by typing `y`
- [ ] Goodbye message shows when player quits
- [ ] Program runs without errors from start to finish

---

## Bonus

Add a 4th category with 5 questions on any topic you like. It just needs to follow the same pattern as the other three.

---

That's it — once this is working, your quiz game is done and ready to present. Well done for making it all the way through!
