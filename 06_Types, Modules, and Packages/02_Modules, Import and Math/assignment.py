# We are going to make a little bit of code to handle finding the hypotenuse of
# a right triangle from user input.  
import math
leg1 = float(input("Enter the value of leg 1: "))
leg2 = float(input("Enter the value of leg 2: "))

hyp = math.hypot (leg1,leg2)

print("The hypotenuse is", hyp)