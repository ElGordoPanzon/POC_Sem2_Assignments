
#Starter code
#YOUDO:  create first_name and last_name variable and 
# assign values using the input function
first_name = input ("Enter your first name: ")
last_name = input ("Enter your last name: ")

sep = " "
full_name = sep.join ([first_name, last_name])
print("Hello" , full_name)
