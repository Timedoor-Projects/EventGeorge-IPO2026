# International Python Olympiad 2026
### Student: George

---

## About the Event

The International Python Olympiad (IPO) 2026 is a programming competition for young students to showcase their Python skills. Participants build a real Python project from scratch and present it through a recorded video submission.

This folder contains all the materials prepared for George's participation in the event — including task instructions, reference code, and the final project.

---

## Project: Quiz Game

The final project is a terminal-based Quiz Game built entirely in Python.

The game lets a player enter their name, choose a quiz category, answer 5 questions, and then see their score along with a result message. At the end, the player can choose to play again or quit.

Everything runs in the terminal — no external libraries, no GUI, just basic Python.

---

## How the project is structured

The project is split into 3 tasks. Each task builds directly on the previous one, so by the end of Task 3 the student has a complete, working program.

**Task 1 — Simple Mini Quiz**

A 3-question Animal quiz. The player types their answer, the program says Correct or Wrong, and the final score is shown at the end. The goal here is just to get comfortable with `print()`, `input()`, variables, and `if/else`.

**Task 2 — Quiz with Categories**

The quiz now has a category menu. The player picks between Animals, Science, or Math before the questions start. This introduces `elif` and teaches the student how to structure a larger program with multiple branches.

**Task 3 — Final Project**

The complete game. Adds the player's name, expands each category to 5 questions, calculates a percentage score, shows a result message based on how well the player did, and lets the player choose to play again using a `while` loop. This is the version that gets submitted to IPO.

---

## Files in this folder

```
Event-George/
│
├── README.md                   ← you are here
│
├── International Python Olympiad '26.pdf
├── IPO 2026 Poster.pdf
│
└── Quiz Game/
    │
    ├── student_assignment.md   ← full project overview for the student
    │
    ├── task1_assignment.md     ← step-by-step instructions for Task 1
    ├── task2_assignment.md     ← step-by-step instructions for Task 2
    ├── task3_assignment.md     ← step-by-step instructions for Task 3
    │
    ├── task1.py                ← reference code for Task 1
    ├── task2.py                ← reference code for Task 2
    └── task3.py                ← reference code for Task 3 (final project)
```

The `_assignment.md` files are the student-facing instruction sheets. The `.py` files are the complete reference code — for the instructor's use, not to be shared with the student upfront.

---

## How to run the programs

Make sure Python 3 is installed, then run any of the files from the terminal:

```bash
python3 task1.py
python3 task2.py
python3 task3.py
```

No additional setup or libraries needed.

---

## Final project requirements (Task 3 checklist)

Before the student submits, the program must have all of these:

- Opening title screen
- Player name input
- Category menu (Animals, Science, Math)
- 5 questions per category
- Correct / Wrong feedback after each answer
- Score counter
- Percentage calculation
- Result message based on percentage:
  - 80% and above → "Excellent Python Coder!"
  - 60% to 79% → "Great Job!"
  - Below 60% → "Keep Practicing!"
- Play again option
- Student's name in a comment at the top of the file
- Saved as `quiz_game.py`

---

## Python concepts covered

The three tasks together cover:

`print()` · `input()` · variables · `if / elif / else` · `.lower()` · `while True` · `break` · `continue` · percentage calculation · string concatenation with `+` · `str()` for type conversion

All of this is basic Python — no classes, no functions, no external libraries. Everything a beginner needs to build a complete project on their own.

---

*Prepared for IPO 2026 — George*
