# Task 2 - Quiz with Categories

Good job finishing Task 1! Now we're going to make the quiz a bit more interesting.

Instead of jumping straight into Animal questions, we're going to let the player **choose a category** first. The game will show a menu, the player picks a number, and then the right set of questions appears.

The 3 categories are:
- Animals (you already have this from Task 1!)
- Science
- Math

---

## What it should look like

```
=========================
         QUIZ GAME       
=========================

Choose a Category:
1. Animals
2. Science
3. Math

Enter your choice (1/2/3): 2

You chose: SCIENCE
-------------------------

Question 1:
What is the largest planet in our solar system?
Your answer: jupiter
Correct!

Question 2:
What do plants need to make their own food?
Your answer: water
Wrong! The correct answer is: sunlight

Question 3:
What gas do we breathe in to stay alive?
Your answer: oxygen
Correct!

=========================
Your score: 2 out of 3
=========================
```

---

## Getting started

Don't start from scratch! Open your `task1.py` file and save a copy of it as `task2.py`. That way we keep all the work you already did.

Update the comment at the top:
```python
# Task 2 - Quiz with Categories
# Developed from Task 1
# Name: ________________
```

---

## Here's what we need to add or change

### Part 1 — Update the title

Change the title to just say "QUIZ GAME" instead of "Welcome to the Animal Quiz!". Keep the border lines.

---

### Part 2 — Add the category menu

Right after the title (but before any questions), add a menu so the player can pick a category. Use `print()` for the options and `input()` to get their choice:

```python
print("Choose a Category:")
print("1. Animals")
print("2. Science")
print("3. Math")
print()

choice = input("Enter your choice (1/2/3): ")
print()
```

Whatever the player types gets stored in `choice`. This will be "1", "2", or "3".

Also make sure `score = 0` stays up at the top, before the menu.

---

### Part 3 — Wrap the Animal questions inside an if block

This is the important new thing in Task 2. Instead of always showing the Animal questions, we only show them when the player picks category 1.

Take all your Animal questions from Task 1 and put them inside this block:

```python
if choice == "1":
    print("You chose: ANIMALS")
    print("-------------------------")
    print()

    # your 3 animal questions go here (indented!)
```

Make sure everything inside is indented — that's how Python knows it belongs to the `if` block.

---

### Part 4 — Add Science questions using elif

Right after the Animals block, add `elif choice == "2":` for the Science category.

`elif` means "else if" — it only runs if the player chose 2, and only if they didn't choose 1.

```python
elif choice == "2":
    print("You chose: SCIENCE")
    print("-------------------------")
    print()

    # science questions go here
```

Here are the Science questions:

Question 1: What is the largest planet in our solar system? → answer: `jupiter`

Question 2: What do plants need to make their own food? → answer: `sunlight`
(tip: also accept `sun` as a valid answer using `or`)

Question 3: What gas do we breathe in to stay alive? → answer: `oxygen`

Use the same format as the Animal questions. Each question needs `print()` for the question text, `input()` for the answer, and `if/else` to check.

---

### Part 5 — Add Math questions using elif again

After the Science block, add `elif choice == "3":` for Math.

```python
elif choice == "3":
    print("You chose: MATH")
    print("-------------------------")
    print()

    # math questions go here
```

Math questions:

Question 1: What is 7 x 8? → `56`

Question 2: What is 100 - 37? → `63`

Question 3: What is 15 + 28? → `43`

One thing to note — for Math answers, don't use `.lower()` because the answers are numbers, not words. Just use `input()` on its own.

---

### Part 6 — Handle wrong input with else

What if the player types something like "5" or "abc"? We need to handle that. Add this after the last `elif`:

```python
else:
    print("Invalid choice! Please enter 1, 2, or 3.")
```

---

### Part 7 — Keep the score display at the end

Make sure your score `print()` lines are outside all the `if/elif/else` blocks — they should have no indentation. That way the score always shows up no matter which category was played.

---

## The structure of your program

If it helps, here's roughly how the whole program should flow:

```
Show title
Show menu
Get player's choice

if choice is "1":
    show animal questions

elif choice is "2":
    show science questions

elif choice is "3":
    show math questions

else:
    show error

Show final score
```

---

### Test all 3 categories

Run `python3 task2.py` and try each option:
- Type `1` — should show Animal questions
- Type `2` — should show Science questions  
- Type `3` — should show Math questions
- Type `9` — should show the invalid message

---

## Checklist

- [ ] Saved as `task2.py` with name in comment
- [ ] Title updated
- [ ] Menu shows 3 categories
- [ ] `choice` variable stores the player's pick
- [ ] `if choice == "1"` runs Animal questions
- [ ] `elif choice == "2"` runs Science questions
- [ ] `elif choice == "3"` runs Math questions
- [ ] `else` handles invalid input
- [ ] Score is counted correctly for each category
- [ ] Final score appears at the end
- [ ] All 3 categories work correctly when tested

---

## Bonus

Add a 4th category — Geography, Sports, Food, whatever you want. Add it as `elif choice == "4":` and don't forget to add option 4 to the menu!

---

One more task to go. Task 3 is the final version, and it's going to look really impressive.
