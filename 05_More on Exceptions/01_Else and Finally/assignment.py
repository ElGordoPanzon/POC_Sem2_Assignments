#Continue with code from 3.3

number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter another number"))
    answer=(number1/number2)
    print("The answer is", answer)
except ZeroDivisionError:
    print("division by zero is not possible.")
else:
    print("no values detected")
finally:
    print("Values taken care of")