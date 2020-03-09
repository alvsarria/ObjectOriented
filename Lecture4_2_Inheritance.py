from random import randint

#Exercise 1: Extend the set of shapes classes to also include Circle and Square. Each shape also has a
# color, centre (x,y) and can be moved (change the centre location)

class Polygon:
    def __init__(self, no_of_sides, center, color):
        self._n = no_of_sides
        self._sides = [int(input("Enter side " + str(i + 1) + " : ")) for i in range(self._n)]
        self._center = center
        self._color = color

    def display_sides(self):
        if type(self) != Circle:
            for i in range(self._n):
                print("Side", i + 1, "is", self._sides[i])
        else:
            print("Radius is", self._sides[0])

    def move(self, new_pos_x, new_pos_y):
        self._center[0] = new_pos_x
        self._center[1] = new_pos_y

    def __str__(self):
        if type(self) != Circle:
            return "Polygon with " + str(self._n) + " sides: " + str(self._sides)
        else:
            return "Circle with radius of " + str(self._sides)


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2, [0,0], "Red")

class Circle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 1, [0,0], "Blue")


# c  = Circle()
# r = Rectangle()

# print(c)
# print(r)

# c.display_sides()
# r.display_sides()

# print(c._center)
# c.move(1,2)
# print(c._center)
# print(r._center)
# r.move(3,6)
# print(r._center)

# Exercise 2: Design classes in Python to represent generic Animals, as well as Cats and Dogs.
# Each animal has a name and can make a sound. Write a small test program to test your classes.

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def __str__(self):
        return "This is a: {0}, and the sound it makes is: {1}".format(self.name,self.sound)

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, "Dog", "Bark")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self, "Cat", "Meow")

# d = Dog()
# print(d)

# c = Cat()
# print(c)


# Exercise 3: Using the BankAccountclass from few weeks ago design classes for SavingsAccount and CurrentAccount.
# SavingsAccount has an interest rate and a method to calculate interest. CurrentAccount has an overdraft.
# Make sure you override any necessary methods in the BankAccountclassCreate a list of BankAccountobjects
# (some SavingsAccount, some CurrentAccount). Write a update() function that iterates through each account,
# updating it in the following ways:
#  - SavingsAccounts get interest added (via the method you already wrote)
#  - CurrentAccounts get a letter sent if they are in overdraft

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

class SavingsAccounts(BankAccount):
    def update(self):
        self.balance = self.balance + self.balance * 0.01
        print("Added {0}€ from interest ratio".format(round(self.balance * 0.01,0)))

class CurrentAccounts(BankAccount):
    def update(self):
        if (self.balance < 0):
            print("Sending information letter")
        else:
            print(self)

def update(input):
    count = 0
    for i in input:
        count += 1
        print("Account number {0}:".format(str(count)))
        i.update()

accounts = []
for i in range(10):
    if i % 2 == 0:
        accounts.append(SavingsAccounts(randint(0,2000)))
    else:
        accounts.append(CurrentAccounts(randint(-1000,2000)))

update(accounts)