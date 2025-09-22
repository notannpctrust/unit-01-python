"""
TASK1:
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.


"""

print()
print()
print()

#Using "i" as a variable so that I can get the correct values for my += statement
i = 1

while i < 11:
    print(i)
    i += 1

"""
TASK@
Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

#Here I did the same thing but backwards so that im basically saying 
#While 10 is less than 0 subtract 1 then print,then repeat until it reach  1
print()
print()
print()

i = 10

while i > 0:
    print(i)
    i -= 1


"""
TASK#
3.Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
print()
print()
print()

#Using the number and result variable I can state the different factorials with each number.
number = int(input("Give me a number: "))
result = 1

while number > 0:
    result = number * result
    number -= 1

print(result)

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
print()
print()
print()

password = "NewYork"
user_guess = "" 
while user_guess != password: 
    user_guess = input("Enter the password: ")
    if user_guess == password:
        print("Access Granted!") 
    else:
        print("Incorrect password, try again.") 





