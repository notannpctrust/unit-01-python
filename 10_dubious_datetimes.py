from datetime import datetime

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print()
print()
print("------TASK1-------")

#Get the current date and time
my_date = datetime.now()

#Printing the result
print("Current date and time:")
print(my_date)


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

print()
print()
print("-----TASK2-----")

#Get the current date and time
my_date2 = datetime.now()

#Format the date in MM/DD/YYYY
formatted_date = my_date2.strftime("%m/%d/%Y")

#Print the result
print("Current date in the U.S. format (MM/DD/YYYY):")
print(formatted_date)


"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""


print()
print()
print("----TASK3----")

#Converting two random date strings into datetime "objects"
date1 = datetime.strptime("10/07/2025", "%m/%d/%Y")
date2 = datetime.strptime("10/14/2025", "%m/%d/%Y")

#Calculating and printing the difference in days using "-"
print(f"Difference in days: {(date2 - date1).days}")


"""
Exercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print()
print()
print("----TASK4----")

#Ask the user to enter their birthdate
birthday = input("Enter your birthdate (MM/DD/YYYY):")

#Convert the string input to a datetime object
birthday = datetime.strptime(birthday,"%m/%d/%Y")

#Get todays date
today = datetime.today()

#Calculate age (subtract 1 if birthday hasn't occurred yet)
age = today.year - birthday.year - ((today.month, today.day)  <  (birthday.month, birthday.day))

#Print the result
print(f"You are {age} years old,congrats you are just old.")






