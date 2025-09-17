"""
TASK1 
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""

print("------task1---------")
print()
print()

#Stored correct password

correct_password = "Peace123"

#Ask for a password
user_input = input("")

#compare the passwords without using case sensitive
if user_input.lower() == correct_password.lower():
    print("Oh You're back,Welcome")
else:
    print("Nuh uh")



"""
TASK2
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""

print("------task2---------")
print()
print()

#Gather input from user
user_input = input("Enter Something: ")

#Check if the input is empty
if user_input.strip() == "":
   print("invalid bro try again")
else:
    print("valid bro you got it")

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurrences regardless of capitalization 
"""

print("------task3---------")
print()
print()


name= input("What's the best pet? Cat or Dog?:")
#So the user just needed to answer what they think their preference.
new_name = name.lower().replace("cat", "dog")
#Depending on what the user inputted it will automatically match with what they say.
print(new_name)
#Printing to the console.

"""
TASK4
Write a program that takes a person's name and age as input and prints it

"""

print("------task4---------")
print()
print()

name = "Christopher"
age = 16
print(f"My name is {name} and I am {age} years old.")


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

#Get two float inputs from the user
num1 = float(input("1.4"))
num2 = float(input("2.3"
""
""))

# Check for division by zero
if num2 == 0:
    print("Error: Cannot divide by zero.")
else:
    # Calculate quotient and round to 1 decimal place
    quotient = round(num1 / num2, 1)
    print("Quotient (rounded to nearest tenth):", quotient)



    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)


