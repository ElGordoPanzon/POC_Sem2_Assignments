try:
    value = int(input('Enter a number: '))
    Second_vaule=int(input("Enter another : "))
    print('The answer is: ', Second_vaule/value)

except ZeroDivisionError:
    print("You provided a 0 and division by 0 is not possible, sorry")
except ValueError:
    print("You did not provide a number, so i will not calculate the answer")
except:
    print("Something weird happened here, sorry")