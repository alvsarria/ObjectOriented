# Excercise 1:
# Write a Python program to ask the user for their name
# (e.g. John) and print "Hello John" on the screen

def name_caller():
    name = input("Insert your name to be printed: ")
    print(name)

# uncomment the function caller to get the output
# name_caller()

# Exercise 2:
# Write a Python program to ask the user for their name and age,
# and print them on the screen in the format "Hello John, you are 20 years old"

def name_age_caller():
    name = input("Insert your name: ")
    age = input("Insert your age: ")
    # print("Hello " + str(name) + ", you are " + str(age) + " years old")
    print("Hello {0}, you are {1} years old".format(str(name), str(age)))

# uncomment the function caller to get the output
# name_age_caller()

# Exercise 3:
# Write a Python program to ask the user for width and hight of a rectangle and print the area.

def rectangle_area():
    width = int(input("Introduce the width of a rectangle (in cm): "))
    height = int(input("Introduce the height of a rectange (in cm): "))
    print("The area of the selected rectangle is " + str(width*height) + " cm^2")

# uncomment the function caller to get the output
# rectangle_area()