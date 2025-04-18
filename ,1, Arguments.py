# Positional argumnets and default arguments
def total_calc(bill_amount, tip_perc):
    # define function to calculate the tip on the bill:
    total = bill_amount*(1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

# Specify only bill_amount
# default value of tip percentage is used

total_calc(150, 20)

# define function to calculate cube: # if a number is divisble by 3:
def cube(number):
    return number * number * number

# define a function which will execute cube function if the user entered:
# number is divisible by 3
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

# display the result:
print(by_three(9))
print(by_three(4))

# function to calculate factorial
# recurtion = calling its self:
def factorial(n):
    if n == 0 or n == 1: # base case 0! and 1! are both 1
        return 1

    else:
        return n* factorial(n - 1) # recursived call

# input from the user
num = int(input("enter a number: "))

# check if the number is negative:
if num < 0:
    print("factorial does not exist for a negative numbers.")

else:
    print(f"The factorial of {num} is {factorial(num)}")















