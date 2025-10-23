"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
   try:
      result = num1 / num2
   except:
      print("Error:You CANNOT divide by zero no matter what!")

     

# Example usage:
divide_numbers(10, 0)
      