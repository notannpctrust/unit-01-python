import random

"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""

print()
print()
print("---------TASK1--------")

#Thinking of rolling a six sided dice like 6 or 7 times
for i in range(10):
    roll = random.randint(1, 7)#This is being used for rolling the random integer between 1 and 7 
    print(f"Roll{i + 1}: {roll}")

"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
print()
print()
print("--------TASK2--------")

#Loop 5 times
for i in range(5):
    print(random.random())#print a random floating point between 0 and 1 

#Loop 5 times
for i in range(5):
    print(random.uniform(10,20))#Printing a random floating point between 10 and 20


"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""

print()
print()
print("-----TASK3------")

#Making a list full of colors
colors =  ["red", "blue", "green", "yellow", "purple"]

#the variable "selected" exists for putting the function random.sample inside.(colors,3) will choose 3 random colors from the list
selected = random.sample(colors,3)
#Printing the 3 randomly selected colors
print(selected)


"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""

print()
print()
print()

#Making a variable called "numbers" and giving a range from 1 to 11
numbers = list(range(1,11))
#This will shuffle the list of ranged numbers
random.shuffle(numbers)
#printing the final result 
print()

