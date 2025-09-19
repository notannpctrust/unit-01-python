import math

#Addition is +
#Subtraction is -
#Multiplication is *
#Division would be /
#Using a remainder would be % ( remember to put the print for the remainder)
#Using Exponents would be **  
#Printing a rounded int or float would be "result = round(variable)""
#Absolute value would be "abs" and to actually use it would be abs(variable)
#power function = Absolute value  pow(x,y)
#max/min tells the maximum/minimum of a set of numbers respectively so using min/max(x,y,z) would work
#Square root = math.sqrt

#Just a little welcoming
print("Running_Calculator.py............")
print()
print()
print()
print("Welcome,User.")
print()
print()
print()
print("By the way you cant put 0 as a denominator,just dont try it.")

#Getting variables for numbers and operators 
num1 = float(input("First number:"   ))
print()
print()
print()
op = input("Choose your operator: +, -, *, /, //(Rounding), **(Exponents), %(Remainder)")
print()
print()
print()
num2 = float(input("Second number:"   ))
print()
print()
print()

#Making many if/elif statements for each operator.Short and Simple.Including the Part where division by zero isn't allowed
if op == "+":
    print(f"Result: {num1+num2}")
elif op == "-":
    print(f"Result: {num1 - num2}")
elif op == "*":
    print(f"Result: {num1 * num2}")
elif op == "/":
    if num2 == 0:
        print("I did say division my 0 IS NOT allowed.")
    else:
        print(f"Result: {num1 / num2}")
elif op == "//":
    if num2 == 0:
        print("Stop toying with the system.Division with the 0 wont work.")
    else:
        print(f"Result: {num1 // num2}")
elif op == "**":
    print(f"Result: {num1 ** num2}")
elif op == "%":
    if num2 == 0
       print("You are doing this on purpose,aren't you?Division by 0 IS NOT ALLOWED.")
    else:
     print(f"Result: {num1 % num2}")
else:
    print("Error:Invalid Error ")


