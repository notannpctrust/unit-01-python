"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
print()
print()
print("-------TASK1--------")

#Just think of it as making a character in a game 

class Person:
    #making a species
    species = 'Human'
   
   #defining my "function" using a given name and age
    def __init__(self, name, age):

        #Two arguments(name and age)are being taken
        self.name = name
        self.age = age 
    
#Create a new Person object 
christopher = Person("Christopher", 18)
print(christopher.name)
print(christopher.age)


"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

print()
print()
print("------TASK2-------")

#Base Class
class Animal:
    def speak(self):
        pass

#Dog Class 
class Dog(Animal):
    def speak(self):#Giving "dog" a speak function
        print("Woof!")#Let "dog" say "Woof!" when called t speak 


#Cat class
class Cat(Animal):
    def speak(self):#Giving "cat" a speak function
        print("Meow!")#Let "cat" say "Meow!" when called to speak 

#Create two objects and call out both to speak 
dog = Dog()
dog.speak()

cat = Cat()
cat.speak()



"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

print()
print()
print("------TASK3--------")


#BankAccount class
class BankAccount:
    def __init__(self, owner , balance):
        self.owner
        self.balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrew:", amount)
        
        else:
            print("Not enough balance.")

#create an account
account = BankAccount("Christopher", 75)