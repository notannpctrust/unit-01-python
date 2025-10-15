from datetime import datetime

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print()
print()
print("-------TASK1--------")

#Making a variable for the current date and time
my_date = datetime.now()
#Printing the current date and time
print("Current date and time:", my_date)


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

print()
print()
print("-----TASK2-----")
#Making a variable for the current date and time
my_date = datetime.now()

#Formatting the date into MM/DD/YY
formatted_date = my_date.strftime("%m/%d/%Y")
print(f"Current time in U.S. format:, {formatted_date}")

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
print()
print()
print("-----TASK3-------")
#Getting two random date strings 
d1 = datetime.strptime("2025-10-07", "%Y-%m-%d")
d2 = datetime.strptime("2025-10-14", "%Y-%m-%d")
#printing the difference using "-"
print("Difference in days:", (d2 - d1).days)

"""
Exercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print()
print()
print("------TASK4-----")