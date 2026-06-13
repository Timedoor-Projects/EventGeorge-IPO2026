# Task 1 - Simple Mini Quiz

Okay, so for the first task, we're going to start small. You're going to build a quiz program that asks 3 questions about Animals. Nothing too complicated — just enough to get comfortable with the basics before we build something bigger.

By the end of this task, your program should be able to:
- Ask the player a question
- Read what they type
- Tell them if they got it right or wrong
- Show the final score at the end

---

## What the program should look like when you run it

```
=========================
Welcome to the Animal Quiz!
=========================

Question 1:
What is the largest animal in the world?
Your answer: whale
Correct!

Question 2:
What animal can fly and lay eggs?
Your answer: cat
Wrong! The correct answer is: bird

Question 3:
What do you call the process when animals sleep through winter?
Your answer: hibernation
Correct!

=========================
Your score: 2 out of 3
=========================
```

---

## Before you start

Create a new file called `task1.py`. At the very top, write a comment with your name:

```python
# Task 1 - Simple Mini Quiz
# Name: ________________
```

Comments in Python start with `#`. The computer ignores them — they're just notes for you (and your teacher).

---

## Now let's build it, one piece at a time

### Part 1 — The score variable

Before anything else, you need somewhere to keep track of the score. In Python, we use a **variable** for this. Think of it like a box with a label on it.

Add this at the top of your code (below the comments):

```python
score = 0
```

This creates a box called `score` and puts the number `0` inside it. Every time the player gets a question right, we'll add 1 to this box.

---

### Part 2 — Show the title

Use `print()` to show the quiz title. The `print()` function just displays text on the screen.

Try to get it to look like this:
```
=========================
Welcome to the Animal Quiz!
=========================
```

You'll need 3 lines of `print()`. After the title, add a blank line using `print()` with nothing inside it — this just skips a line to make it look cleaner.

---

### Part 3 — Ask the first question

Now we get to the fun part. Use `print()` to show the question, then use `input()` to wait for the player to type their answer.

```python
print("Question 1:")
print("What is the largest animal in the world?")
answer1 = input("Your answer: ")
```

`input()` pauses the program and waits. Whatever the player types gets saved into `answer1`.

One small thing — if the player types "Whale" with a capital W, we don't want that to be treated differently from "whale". So right after getting the answer, convert it to lowercase:

```python
answer1 = answer1.lower()
```

---

### Part 4 — Check if the answer is right

Now use `if` and `else` to check the answer. If it matches, add 1 to the score. If it doesn't, show the correct answer.

```python
if answer1 == "whale":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is: whale")

print()
```

Note: `==` means "is equal to". It's different from `=` which means "store this value".

---

### Part 5 — Questions 2 and 3

Do the same thing for the next two questions. Use `answer2` and `answer3` as your variable names.

**Question 2:**
- Question: What animal can fly and lay eggs?
- Correct answer: `bird`

**Question 3:**
- Question: What do you call the process when animals sleep through winter?
- Correct answer: `hibernation`

Copy the same pattern from Question 1 and change the question text and the answer.

---

### Part 6 — Show the final score

After all 3 questions, show the player's score:

```python
print("=========================")
print("Your score:", score, "out of 3")
print("=========================")
```

---

### Test it!

Save the file and run it:
```
python3 task1.py
```

Try answering everything correctly — you should get `3 out of 3`.
Then try answering everything wrong — you should get `0 out of 3`.

If something doesn't work, read the error message carefully. Python usually tells you which line has the problem.

---

## Quick checklist before moving on

- [ ] File saved as `task1.py`
- [ ] Name written in the comment at the top
- [ ] `score = 0` at the start
- [ ] Title shows up when the program runs
- [ ] 3 questions are asked
- [ ] Each question uses `input()` to get the player's answer
- [ ] Program says Correct or Wrong after each answer
- [ ] Score increases for correct answers
- [ ] Final score is shown at the end
- [ ] No errors when running

---

## Bonus (if you finish early)

Try adding a 4th question about an animal you like. Just follow the same pattern.
Don't forget to change `"out of 3"` to `"out of 4"` at the end!

---

Once everything works, you're ready for Task 2.
