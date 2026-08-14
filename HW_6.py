print("Task1")
class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def get_info(self):
        return f"{self.name} works as {self.position} and earns {self.salary}$."
employee1=Employee("Anna", "QA Engineer",7000)
employee2=Employee("Viktor", "Manager",21000)
employee3=Employee("Alex", "Teacher",15000)
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print("--------------------------------------------------------------------------")

print("Task2")
class Product:
    def __init__(self, name, price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def buy (self,amount):
       if self.quantity>amount:
           self.quantity-=amount
           print(f"Remaining balance after purchase of {amount} items - {self.quantity} items.")
       else:
           print(f"Not enough products. The balance has not changed - {self.quantity} items.")
laptop=Product("laptop", 100, 5)
laptop.buy(2)
laptop.buy(10)
print("--------------------------------------------------------------------------")

print("Task3")
class Vehicle:
    def __init__(self, brand):
        self.brand=brand
    def move(self):
        return f"{self.brand} is moving."

class Car(Vehicle):
    def move(self):
        return f"{self.brand} is driving."

class Bicycle(Vehicle):
    def move(self):
        return f"{self.brand} is riding."
car=Car("Car")
bicycle=Bicycle("Bicycle")
print(car.move())
print(bicycle.move())
print("--------------------------------------------------------------------------")

print("Task4")
class User:
    country="Israel"
    def __init__(self, username, age):
        self.username=username
        self.age=age
user1=User("Nif-Nif", 14)
user2=User("Nuf-Nuf", 14.5)
user3=User("Naf-Naf", 15)
print(f"{user1.username} lives in {user1.country}.")
print(f"{user2.username} lives in {user2.country}.")
print(f"{user3.username} lives in {user3.country}.")
print("**********")

User.country="Canada"
print(f"{user1.username} lives in {user1.country}.")
print(f"{user2.username} lives in {user2.country}.")
print(f"{user3.username} lives in {user3.country}.")

'''
1. Class: Employee
Create an Employee class.
Requirements:
__init__(name, position, salary)
get_info() method
The method should return a string in the following format:
Anna works as QA Engineer and earns 7000
Create at least two employees and print the information for each of them.

2. Online Store
Create a Product class.
Attributes:
-name
-price
-quantity
Methods:
buy(amount)
Rules:
If there is enough stock, decrease the quantity.
If there is not enough stock, return the string: "Not enough products".
Test the class functionality with multiple calls.

3. Inheritance
Create a Vehicle class.
Method:
move() — returns "Vehicle is moving"
Create two classes: Car and Bicycle.
Override the move() method.
For example:
Car is driving
Bicycle is riding

4. Class Attribute
Create a User class.
Add a class attribute: country = "Israel".
Add instance attributes:
-username
-age
Create three users.
Change the class attribute value to User.country = "Canada".
Verify that it has changed for all users.
'''
