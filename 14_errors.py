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


"""
Example 2: Opening Files
"""

#The error here is that there is no file called "nonexistent.txt".
#Simply putting a try/except will "gracefully" accept the error
def read_file(filename):
 try: 
    file = open(filename, 'r')
    contents = file.read()
    print("File contents:", contents)
    file.close()
 except:
   print("That file does not exist.")

# Example usage:
read_file("nonexistent.txt")


"""
Example 3: List Items
"""
#The error here was that the given index was out of range from the list given in "my_list"
def get_item(lst, index):
 try:
    item = lst[index]
    print("Item:", item)
 except:IndexError
 print("That index is out of range.")

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)

"""
Example 4: Dictionaries
"""

#The error here was that there was no given key or value for "c"
def get_value(dictionary, key):
   try:
    value = dictionary[key]
    print("Value:", value)
   except:KeyError
   print("There was no {key} found within the dictionary.")

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""


#The error here was "example.txt" did not exist in the same directory as the one given 
#Using a try,except and finally gave access to allow the terminal to attempt to process the file
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    else:
       print("File has been completely read.")
       print("File contents:", contents)
    finally:
       print("Finished attempting to process the give file. ")

# Example usage:
process_file("example.txt")





      