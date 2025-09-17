"""
TASK 1:
Create a float variable, and then convert it to an integer
"""

print("------task1---------")
print()
print()

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

print("------task2---------")
print()
print()


# Input a random number and concert it to a number
number = float(input("type a number"))

# Check the number's value
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


"""
TASK 3 
Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.

"""

print("------task3---------")
print()
print()

#Take integer input from the user
input1 = input("give me a float")

# Take float input from the user
num1= float(input1)

#Printing the results
print(type(num1))

"""
TASK4 

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""

print("------task4---------")
print()
print()

#Creating the dictionary
fruits = {
   'apple':18,
   'watermelon':30,
   'orange':17,

 }

#Printing the results
print("18:", fruits["apple"])


"""
TASK5
Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

print("------task5---------")
print()
print()

# original string 
number_string = "1, 2, 3, 4, 5"

#Conversion process (string into a tuple of integers)
number_tuple = tuple(int(num.strip()) for num in number_string.split(','))

#Printing Results
print("1, 2, 3, 4, 5", number_string)
print("")

"""
TASK6
Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.

"""

print("------task6---------")
print()
print()















