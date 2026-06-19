**# Task 3: Some things that need improvement.**

1. Q4 and Q5 only show up when Q3 is answered wrong

This is the biggest issue. Q4 and Q5 ended up inside the `else` block of Q3. So if the player gets Q3 right, the game just skips Q4 and Q5 entirely. This happens for all 3 categories.

```py
# wrong:
if answer3 == "hibernation":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")
    print()
    print("Question 4:")   # ← only runs if Q3 is WRONG
    ...
    print("Question 5:")   # ← only runs if Q3 is WRONG

# should be (Q4 and Q5 outside the else):
if answer3 == "hibernation":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")
print()
print("Question 4:")       # ← always runs
...
print("Question 5:")       # ← always runs
```

2. The final result section is also in the wrong place

Same problem — the FINAL RESULT only appears when Q5 is answered wrong. If the player gets Q5 right, no result screen shows up at all.

3. `play_again` is used before it's defined — program will crash

You check `if play_again != "y":` early in the code, but `play_again = input(...)` is only written near the bottom of the Math section. When the player picks Animals or Science, Python will crash with an error because `play_again` doesn't exist yet.

4. `if/elif/else` still not fixed from Task 2

Science and Math still use `if` instead of `elif`, so the structure is still broken from the previous task.

5. Stray line in Science section

There's a random line that always prints before Science Q2:

```py
print("Wrong! The correct answer is sunlight") # ← this shouldn't be here
print("What do plants need to make their own food?") 6. Small things:
```

6. Small things:
   - "Exelent!" → should be "Excellent!"
   - Category labels should be uppercase: "You chose: ANIMALS" not "You chose Animals"
   - The or "sun" bug from Task 2 is still there

---

1. Animals questions are still outside the if block

Only the header is inside `if choice == "1":`, but the actual questions run no matter what the player picks:

```py
# wrong:
if choice == "1":
    print("You chose Animals")
    print("-----------------")
print("Question 1:") # outside the if, always runs

# should be:

if choice == "1":
    print("You chose Animals")
    print("-----------------")
    print("Question 1:") # indented inside the if
```

Because of this, the final result and play again prompt also always run right after the Animals section, no matter which category was chosen.

2. Science Q4 and Q5 are still inside the `else` block

Same issue from v1 that didn't get fixed. Q4 only shows if Q3 is wrong, and Q5 only shows if Q4 is wrong:

```py
# wrong:
else:
    print("Wrong!")
    print("Question 4:") # only runs if Q3 is wrong

# should be:
else:
    print("Wrong!")
print()
print("Question 4:") # always runs
```

Same thing happens in Math Q4 and Q5.

3. Science and Math still use if instead of elif

```py
# wrong:
if choice == "2":
if choice == "3":

# should be:
elif choice == "2":
elif choice == "3":
```

4. The invalid input message is in the wrong place

Right now it's connected to `if play_again != "y":` instead of the category selection — so it shows up when the player types `y` to play again, which doesn't make sense.

5. Small things to fix:

   - "Exellent!" → "Excellent!"
   - Category labels should be uppercase — "You chose: ANIMALS", not "You chose Animals"
   - Missing print("Question 1:") before the first Math question
