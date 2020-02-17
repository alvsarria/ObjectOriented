# Exercise 1
# Using the classes from last week, try out the different options for the attributes (accessible/not accessible)

class Book:
    def __init__(self,isbn,title,author):
        self.__isbn = isbn
        self.__title = title
        self.__author = author

    def __str__(self):
        return 'Book: {0}, Author: {1}, ISBN: {2}'.format(self.title,self.author,self.isbn)

    def get_title(self):
        return self.__title

p = Book(123456, 'The Name of the Wind', 'Patrick Ruthfus')

try:
    print(p.__title)
except AttributeError:
    print("title private!")

print(p.get_title())
print(p._Book__title)

# Exercise 2
# Modify the class Person so it uses one variable to represent the full name, e.g. ‘John Smith’.
# How would you access the first name and the surname?

class Person:
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name.split(" ")[0]

    def get_surname(self):
        return self.__name.split(" ")[1]

p = Person("Alvaro Sarria")

print(p.get_name())
print(p.get_surname())

# Exercise 3
# Extend the program from last week about the class Book and modify it so that it will create 5 books at run-time
# and add them to a list. Print the contents of the list

class Book:
    def __init__(self,title,author):
        self.__title = title
        self.__author = author

    def __str__(self):
        return 'Book: {0}, Author: {1}'.format(self.__title,self.__author)

books = []

#for i in range(5):
#    books.append(Book(input("Title"),input("Author")))

#for i in books:
#    print(i)

# Exercise 4
# Design and implement a Clock class that measures hours, minutes and seconds. Think about:
#   •How many variables you need in order to represent a class?
#   •How would you initialize an instance of a clock?
#   •How can you set the time if time is given in the format “hh:mm:ss”?
#   •How can you “print” a clock

class Clock:
    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def set_time(self,new_hour,new_minute,new_second):
        self.__hour = new_hour
        self.__minute = new_minute
        self.__second = new_second

    def __str__(self):
        if self.__hour < 10:
            self.__hour = "0" + str(self.__hour)
        if self.__minute < 10:
            self.__minute = "0" + str(self.__minute)
        if self.__second < 10:
            self.__second = "0" + str(self.__second)
        return "{0}:{1}:{2}".format(self.__hour,self.__minute,self.__second)

p = Clock(0,0,0)
print(p)
p.set_time(int(input("Insert new hour: ")),int(input("Insert new minute: ")),int(input("Insert new second:")))
print(p)