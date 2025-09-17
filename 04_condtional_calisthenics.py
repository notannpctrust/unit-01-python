"""

Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.

"""

print("------task1---------")
print()
print()

#Giving a statement for a single integer 
if 5 > 3:
    print("thats true,you got it")
    #Stating an else statement for the False text
else:
    print("False bro,try again")



"""
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
"""
print("------task2---------")
print()
print()

#Setting up a random age,the age may seem large but it's needed for the if statement
age = 19
#Getting an input statement for the ticket price 
student = input("Are you a student? ")

#The if and else work for asking the different ticket prices for students/age.
if age <= 18 or student == "yes":
    print("Your ticket price will be $10")
else:
    print("Your ticket price will be $20")


'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

print("------task3---------")
print()
print()

myList = ["apple", "banana", "blueberries"]

fruit = input ("What fruits are in the list?")

if fruit in myList:
   print("That fruit is on the list")
else:
    print("That fruit is not on the list")