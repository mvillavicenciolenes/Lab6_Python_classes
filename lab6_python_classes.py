"""
Michael Villavicencio
Sep 20, Python classes

"""
print("\n ------ Example 1: exception handling -----")

def hour_ratio():
    try:
        hours = 24
        h = int(input("Please enter a number to divide 24 hours: "))

        hours /= h   # hours = hours/h
        return hours
    except ZeroDivisionError:
        print(f"The number {h} can't be divided by 24. Result is undefined")
    except ValueError:
        print(f"Input value was not a number.")
    except:
        print("Program has error")
# calling the function
print(hour_ratio())
print("\n=========== End of program 1 =========== \n")

print("\n ------ Example 2: classes -----")
# define a class named 'Complex'
class Complex:
    def __init__(self, realpart, imagpart) :
        self.r =  realpart
        self.i = imagpart

# create an instance of the class
point1 = Complex(3.0, -4.5)

# calling the instance object
real1 = point1.r
imag1 = point1.i

# prompt result
print(f"real number = {real1} with imaginary number = {imag1}")

print("\n ------ Example 3: classes with properties and methods -----")
class Car:
    # properties , attributes, of class Car
    def __init__(self, make, model, year ):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # methods of class Car
    # method 1: print of description of the class Car
    def get_descriptive_name(self):
        full_name = f"{self.year}, {self.make}, {self.model}"
        return full_name
    
    #method 2: read and print the odometer
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
    
    #method 3: update and print odometer
    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    
    # method 4: increment odometer
    def increment_odometer(self, miles):
        self.odometer_reading += miles

# create an instance of class Car
usercar1 = Car("audi", "a4", 2020)

# accessing properties
print(usercar1.year)

# accessing method 
print(usercar1.get_descriptive_name())
usercar1.read_odometer()
usercar1.update_odometer(100)
usercar1.read_odometer()
usercar1.update_odometer(20)
usercar1.read_odometer()

usercar1.increment_odometer(35)
usercar1.read_odometer()

print("\n ------ EXERCISE -----")

"""

Activity description: 
Create a Python class called BankAccount that represents a basic bank account. 
The class should have the following properties and methods:
Properties:
account_number: A string representing the account number.
account_holder: A string representing the name of the account holder.
balance: A float representing the current balance of the account.
 
Methods:
__init__(): Initializes the attributes of the class. 
It should take two parameters: account_number and account_holder. 
The balance should be initialized to 0.0.
deposit(amount): 
    Adds the specified amount to the account balance.
withdraw(amount): 
    Subtracts the specified amount from the account balance, if the balance is sufficient. 
If the balance is insufficient, print a message indicating that the withdrawal cannot be made.

Testing:
After creating the 'BankAccount' class, create an instance of the class and demonstrate the use of its methods by performing deposits and withdrawals as:
# Creating an instance of the BankAccount class
useraccount = BankAccount("123456789", "Student's name")
 
# Demonstrating deposits and withdrawals
useraccount.withdraw(700)
useraccount.deposit(1000)
useraccount.withdraw(500)
# prompt result
print(f"Final balance {useraccount .balance}")

"""

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0  
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount to be deposited {amount}. New available balance: {self.balance}")
        else:
            print("Only deposits are permitted with this transaction.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"No funds available. Current balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: {amount}. Your new balance is: {self.balance}")


# Testing the BankAccount class

useraccount = BankAccount("123456789", "Student's name")

print(f"\nAccount Holder: {useraccount.account_holder}")
print(f"Account Number: {useraccount.account_number}\n")

useraccount.withdraw(700)  
useraccount.deposit(1000) 
useraccount.withdraw(500) 

print(f"\nFinal balance: {useraccount.balance}\n")