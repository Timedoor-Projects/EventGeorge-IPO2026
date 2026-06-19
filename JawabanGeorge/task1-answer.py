# Task 1 - Simple Mini Quiz
# Name: George
score = 0
print("===========================")  # REVISI: jumlah "=" harusnya 25, bukan 27
print("Welcome to the Animal Quiz!")
print("===========================")  # REVISI: jumlah "=" harusnya 25, bukan 27
# REVISI: tambahkan print() di sini untuk blank line setelah judul
print("Question 1:")
print("What is the largest animal in the world?")
answer1 = input("Your answer: ")
answer1 = answer1.lower()
if answer1 == "blue whale":  # REVISI: jawaban seharusnya "whale", bukan "blue whale"
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is: blue whale")  # REVISI: ganti jadi "whale"
print()
print("Question 2:")
print("What animal can fly and lay eggs?")
answer2 = input("your answer: ")  # REVISI: "your" harusnya "Your" (huruf kapital)
answer2 = answer2.lower()
if answer2 == "bird":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is: bird")
    print()  # REVISI: pindahkan print() ini ke luar blok else (sejajar dengan if)
print("Question 3:")
print("What do you call the process when animals sleep through winter?")
answer3 = input("your answer: ")  # REVISI: "your" harusnya "Your" (huruf kapital)
answer3 = answer3.lower()
if answer3 == "hibernation":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is: hibernation")
    print()  # REVISI: pindahkan print() ini ke luar blok else (sejajar dengan if)

print("======================")  # REVISI: jumlah "=" harusnya 25, bukan 22
print("Your score:", score, "out of 3")
print("======================")  # REVISI: jumlah "=" harusnya 25, bukan 22
