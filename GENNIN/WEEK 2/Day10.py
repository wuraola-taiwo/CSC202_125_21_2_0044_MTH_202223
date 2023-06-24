# Days in months

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_months(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29

    return month_days[month - 1]
    
    
year = int(input("enter a year: "))
month = int(input("Enter a month: "))
days = days_in_months(year, month)
print(days)


# Calculator
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}
def calculator():
    num1 = float(input("Whats the first number: "))

    for i in operations:
        print(i)
    playing = True

    while playing:
        operation_symbol = input("Pick an operator from the list above ")

        num2 = float(input("Write another number: "))

        calc = operations[operation_symbol]
        soln = calc(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {soln}")

        again = input(f"Type 'y' to continue calculating {soln} or type 'n' to start a new calculation type: ").lower()
        if again == "y":
            num1 = soln
        else:
            playing = False
            calculator()
            
calculator()