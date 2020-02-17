# Exercise 1
# Write a class Book –every book has a ISBN, title and author.

class Book:
    def __init__(self,isbn,title,author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def __str__(self):
        return 'Book: {0}, Author: {1}, ISBN: {2}'.format(self.title,self.author,self.isbn)

p = Book(123456, 'The Name of the Wind', 'Patrick Ruthfus')

print(p.isbn)
print(p.title)
print(p.author)
print(p)

# Exercise 2
# Write a Python class to represent a rectangle. Include methods to calculate the area and parameter

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def parameter(self):
        return 'Rectange parameter is: ' + str(self.width*2 + self.height*2)

    def area(self):
        return 'Rectange area is: ' + str(self.width * self.height)

p = Rectangle(20,60)

print(p.parameter())
print(p.area())

# Exercise 3
# Write a class BankAccount. Every bank account has a balance. Include methods to deposit and withdraw money

class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        return "Depositing... New balance is: {0}".format(self.balance)

    def withdraw(self,amount):
        self.balance = self.balance - amount
        return "Withdrawing... New balance is: {0}".format(self.balance)

    def __str__(self):
        return "Current balance is: {0}".format(self.balance)

p = BankAccount(3000)
print(p)
print(p.withdraw(500))
print(p.deposit(1000))

# Exercise 4
# Extend the class Person and add a method older which returns true or false if a person is older than another person

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def comparison(self,other_person):
        if self.age > other_person.age:
            return "{0} is older than {1}".format(self.name,other_person.name)
        elif self.age == other_person.age:
            return "{0} is the same age as {1}".format(self.name,other_person.name)
        else:
            return "{0} is younger than {1}".format(self.name, other_person.name)

p1 = Person("Alvaro Sarria",29)
p2 = Person("Marc Virgili",30)

print(p1.comparison(p2))

# Advanced
# Write a class Student. Every student should have a name, student number and a list of marks
# (implemented as a python list) Include any appropriate methods, and a method to calculate the average mark.

class Student:
    def __init__(self,name,std_number,marks):
        self.name = name
        self.std_number = std_number
        self.marks = marks

    def __str__(self):
        return "Student: {0}, Student Number: {1}".format(self.name, self.std_number)

    def average(self):
        counter = 0
        for i in self.marks:
            counter += i
        return "Student: {0} has an average mark of {1}".format(self.std_number,round(counter/len(self.marks),2))

    def add_mark(self,new_mark):
        self.marks.append(new_mark)
        return "New mark has been added"

p = Student("Alvaro Sarria Rico",1914893,[4,4,8,7,6])
print(p)
print(p.average())
print(p.add_mark(10))
print(p.average())