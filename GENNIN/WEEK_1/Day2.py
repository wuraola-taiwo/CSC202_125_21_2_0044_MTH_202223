# Data types, Numbers, Operations, Type conversion, f-String
#TIP CALCULATOR
print("Welcome to the tip Calculator.")
total_bill = float(input("What was the total Bill?\n$"))
no_of_people = int(input("How many people to split the bill?\n"))
percentage = int(input("What percentage tip would you like to give?\n10, 12 or 15?"))
final =round(((total_bill) / no_of_people) * (1 + percentage/100),2)
print("Each person should pay: $", final)
