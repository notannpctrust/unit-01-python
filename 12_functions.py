"""
Task 1: Greeting
Write a function that takes a name as a 
argument and prints a greeting message like "Hello, [name]!".
"""

print()
print()
print("------TASK1-----")

#Making a function
def my_function(name):

    #printing and formatting the name value so the sentence wil be clear in terminal
    print(f"Hello, {name}.")

    #using my function and a single name  since there is one value inside the original function 
my_function("Wally West")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

print()
print()
print("------TASK2--------")

#Defining a function as a number 
def my_function1(number):

    #Using the return value since I am using math
    return number ** 2
#Storing my function in a variable and printing the final result
result = my_function1(4)
print(result)

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""

print()
print()
print("-----TASK3------")

#Defining a function as an even number
def even_number(number):

    #Using the return value again since the code involves math 
    return number % 2 == 0 
#Using two print statements to check both numbers if they are true and false or in this case even and odd
print(even_number(4))
print(even_number(7))

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""

print()
print()
print("-----TASK4-------")

#Defining a function as the area of a rectangle 
def area(length, width):

    #Using return vale for multiplying "length" and "width"
    return length * width

#Printing a pair of numbers acting as my length and width 
print(area(6,7))


"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
print()
print()
print("-----TASK5-----")

#Defining a function as temp
def temp(celsius):

    #returning the value using the formula for converting celsius to fahrenheit
    return (celsius * 9/5) + 32

#Printing my temp
print (temp(20))

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""


print()
print()
print("-------TASK6--------")

#Using a function named "average"
def average(numbers):

    #Using the return vale for the sum of the list of numbers divided by the length of the list of numbers
    return sum(numbers)/len(numbers)

#printing the result
print(average([10,20,30,40]))

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""

print()
print()
print("-----TASK7------")




