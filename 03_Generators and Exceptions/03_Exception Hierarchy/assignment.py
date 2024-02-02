# try function Checks code for errors
try:
    First_value = int(input('Enter a number: '))
    Second_vaule=int(input("Enter another : "))
    print('The answer is: ', Second_vaule/First_value)

# except function lets you fix the error
# else block lets yo execute code when there is no error

try:
    #YOUDO divide number1 / number2 and set to answer
    #YOUDO  print the result of the division (aka answer with some helper text)
    pass  # YOUDO remove pass when done
except ZeroDivisionError:
    print("You provided a 0 and division by 0 is not possible, sorry")
except ValueError:
    print("You did not provide a number, so i will not calculate the answer")
