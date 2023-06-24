# Conditional Statements, Logical Operators, Code blocks and Scope
#ROLLER COASTER ELIGIBILITY CHECKER
# print("Welcome to the rollercoaster!\n")
# bill = 0
# height = int(input("What is your height in cm?\n"))
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print(f'Child tickets are ${bill}\n')
#     elif age<= 18:
#         bill = 7
#         print(f'Youth tickets are ${bill}\n')
#     else:
#         bill = 12
#         print(f'Adult tickets are ${bill}\n')
#     photo_req = input("Do you want a photo taken?\nplease enter Y to represent yes or N to represent no\n")
#     if photo_req == "Y" or "y":
#         bill = bill + 3  #same as bill+=3
#
#     print(f'Your final bill is ${bill}')
# else:
#     print("Sorry, you have to grow taller befor you can ride")

#BMI CALCULATOR
# print("Welcome to BMI calculator\n")
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight / (height ** 2))
# if bmi < 18.5:
#     print(f'Your BMI is {bmi}, you are underweight')
# elif bmi <25:
#     print(f'Your BMI is {bmi}, you have a normal weight')
# elif bmi <30:
#     print(f'Your BMI is {bmi}, you are overweight')
# elif bmi <35:
#     print(f'Your BMI is {bmi}, you are obese')
# else:
#     print(f'Your BMI is {bmi}, you are clinically obese')

#leap year checker
# print("This app checks if a year is a leap year\n")
# year = int(input("Which year do you want to check\n"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year %400 == 0:
#             print(f'year {year} is a leap year')
#         else:
#             print(f'year {year} is not a leap year')
#     else:
#         print(f'year {year} is a leap year')
# else:
#     print(f'year {year} is not a leap year')

#PIZZA DELIVERIES
print("WELCOME TO PIZZA DELIVERIES")
bill = 0

size = input("What size of pizza do you want?\nS, M or L\n")
pepperoni = input("Do you want pepperoni?\nY or N\n")
cheese = input("Do you want extra cheese?\nY or N\n")
if size == "S" or "s":
    bill += 15
elif size == "M" or "m":
    bill += 20
else:
    bill += 25

if pepperoni == "Y" or "y":
    if size == "S" or "s":
        bill+=2
    else:
        bill +=3


if cheese == "Y" or "y":
    bill +=1
print(f'Your bill is ${bill}\n'
      f'Thanks for coming')



