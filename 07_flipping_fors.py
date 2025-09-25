

"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
print()
print()
print()
#Defining a name.
name = "Mr.Brown"
for char in name:
    print(char)




"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
print()
print()
print()
numbers = [2 ,3, 4, 5, 6, 8, ]#Giving a list named "numbers"
total = 0 #giving total a value
for num in numbers:#
    total += num
print(f"The sum of the list elements is:{total}"  )#printing the total from the lust

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
print()
print()
print()

sentence = list("I, respect, females")

for x in sentence:
    print(x)

"""
Exercise 4:
Write a program that creates a dictionary (at least 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
print()
print()
print()

my_dict = { # Getting a dictionary/values
    "apples": 4,
    "oranges":9,
    "melons" :16,
    "grapes":8
}
for x in my_dict: #getting a for loop sor stating each iteration
    print(x)
