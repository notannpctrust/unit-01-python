"""
TASK 1:
Create a float variable, and then convert it to an integer
"""



# Making a variable 
my_float = 3.1459

#Converting the original float using the int() function 
my_integer = int(my_float)

# Printing both the original float and the converted integer 
print(my_float)
print(my_integer)

"""

TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
# Input a random number and concert it to a number
number = float(input("type a number"))

# Check the number's value
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")









