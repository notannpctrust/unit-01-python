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

#Getting variables for numbers 
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

if op == "+":
    print(f"Result: {num1+num2}")
elif op == "-":
    print(f"Result: {num1 - num2}")
elif op == "*":
    print(f"Result: {num1 * num2}")
elif op == "/":
    print(f"Result: {num1 / num2}")
elif op == "//":
    print(f"Result: {num1 // num2}")
elif op == "**":
    print(f"Result: {num1 ** num2}")
elif op == "%":
    print(f"Result: {num1 % num2}")
else:
    print("Error:Invalid Error ")


