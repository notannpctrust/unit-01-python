import os

"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""

#Getting the working directory
print()
print()
print("-----------TASK1------------")
current_directory = os.getcwd()

#Print the current working directory
print(f"The current working directory is:{current_directory}")


"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""

#Making an new directory myself
print()
print()
print("---------TASK2---------")
new_directory = os.getcwd()

print(os.listdir())

"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
print()
print()
print("--------TASK3-------")

if


