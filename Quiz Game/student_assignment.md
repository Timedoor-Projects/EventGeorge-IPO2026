# IPO Quiz Game 2026
### Final Project — Student Assignment

---

## Overview

For your final project, you're going to build a Quiz Game in Python. This is a real, working program that runs in the terminal and lets someone actually play a quiz.

The game will have a title screen, ask for the player's name, let them choose a category, ask 5 questions, calculate their score and percentage, and then ask if they want to play again.

When it's done, you'll have something you can actually show and record for the International Python Olympiad 2026.

---

## How the project is split up

The project is broken into 3 tasks. Each one builds on the previous one, so don't skip ahead.

**Task 1** — Build a simple 3-question Animal quiz. Get comfortable with `print()`, `input()`, variables, and `if/else`.

**Task 2** — Add a category menu. The player now picks between Animals, Science, or Math before the questions start. You'll learn how to use `elif` and how to structure a bigger program.

**Task 3** — Finish the whole game. Add the player's name, expand to 5 questions per category, calculate a percentage, show a result message, and add a play again option using a `while` loop.

There's a separate instruction sheet for each task. Work through them in order.

---

## What your finished game needs to have

By the end of Task 3, your program must include all of these:

- A title screen when the program starts
- The player types in their name
- A menu to choose a category (Animals, Science, or Math)
- 5 questions per category
- After each answer, the program says Correct or Wrong
- If wrong, the correct answer is shown
- A final result screen showing the score and percentage
- A message based on how well they did:
  - 80% or above → "Excellent Python Coder!"
  - 60% to 79% → "Great Job!"
  - Below 60% → "Keep Practicing!"
- At the end, the player can choose to play again or quit

---

## Rules

- Use only basic Python — no importing any libraries
- Everything runs in the terminal, no windows or buttons
- Save your final file as `quiz_game.py`
- Write your name in a comment at the top of the file

---

## Questions you can use

You're welcome to use these, or come up with your own.

**Animals**
1. What is the largest animal in the world? → whale
2. What animal can fly and lay eggs? → bird
3. What do you call the process when animals sleep through winter? → hibernation
4. What eight-legged animal spins webs? → spider
5. What animal sheds its skin to grow? → snake

**Science**
1. What is the largest planet in our solar system? → jupiter
2. What do plants need to make their own food? → sunlight
3. What gas do we breathe in to stay alive? → oxygen
4. How many planets are in our solar system? → 8
5. What is the process called when plants make food using sunlight? → photosynthesis

**Math**
1. What is 7 x 8? → 56
2. What is 100 - 37? → 63
3. What is 15 + 28? → 43
4. What is 144 divided by 12? → 12
5. What is the area of a square with a side length of 9? → 81

---

## What the finished program should look like

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

Enter your choice (1/2/3): 2

You chose: SCIENCE
---------------------------------

Question 1:
What is the largest planet in our solar system?
Your answer: jupiter
Correct!

...

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

## Concepts you'll use across all 3 tasks

`print()` — shows text on the screen

`input()` — waits for the player to type something

Variables — store data like the player's name, their answer, and the score

`if / elif / else` — makes decisions based on conditions

`.lower()` — converts text to all lowercase so "Whale" and "whale" are treated the same

`while True` — keeps the game running in a loop

`break` — stops the loop and ends the game

`str()` — converts a number to text so you can join it with other text

---

## Submission checklist

Before you submit, go through this list:

- [ ] Opening title screen
- [ ] Player name is asked and used
- [ ] Category menu works
- [ ] Each category has 5 questions
- [ ] Correct / Wrong feedback for every answer
- [ ] Score is tracked correctly
- [ ] Percentage is calculated
- [ ] Result message matches the percentage
- [ ] Play again works
- [ ] Goodbye message when quitting
- [ ] Your name is in a comment at the top
- [ ] File saved as `quiz_game.py`
- [ ] No errors when running

---

## Bonus

If you finish early, try adding a 4th category on any topic you like. It just needs to follow the same format as the other three — 5 questions, same style, same scoring.

---

Good luck — you've got this.
