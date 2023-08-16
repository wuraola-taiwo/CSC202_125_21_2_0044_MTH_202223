import random

# Average student height
student_heights = input("Please enter the heights of various students: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
sum_student_heights = sum(student_heights)
 len_students = len(student_heights)

sum_student_heights = 0

for height in student_heights:
    sum_student_heights += height

len_students = 0
for num in student_heights:
    len_students += 1

average_height = int(sum_student_heights) / int(len_students)

print(f"The average student height is {average_height}")

# High Score
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0

for i in student_scores:
    if i > highest_score:
        highest_score = i

print(f"The highest score is {highest_score}")

# Sum of even numbers

even_numbers = 0
for i in range(0, 101):
    if i % 2 == 0:
        even_numbers += i

print(even_numbers)

# FizzBuzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# Password Generator
low_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
cap_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

am_low = int(input("How many lowercase letters do you want: "))
am_cap = int(input("How many uppercase letters do you want: "))
am_num = int(input("How many numbers do you want: "))

password = []

for i in range(1, am_low + 1):
    letter_l = random.choice(low_letters)
    password += letter_l

for i in range(1, am_cap + 1):
    letter_c = random.choice(cap_letters)
    password += letter_c

for i in range(1, am_num + 1):
    letter_n = random.choice(numbers)
    password += str(letter_n)

random.shuffle(password)
for i in password:
    print(i, end="")
