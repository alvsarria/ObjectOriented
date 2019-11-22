# Exercise 1: Write a function that takes a number as a parameter and prints the numbers from 1
# to that number on the screen.

def my_first_function(input):
    for i in range(1,input + 1):
        print(i, end = " ")

# my_first_function(5)

# Exercise 2: Write a function that takes a number as a parameter and iterates from 0 to that number.
# For each iteration, it will check if the current number is even or odd, and report that to the screen
# (e.g. "1 is odd, 2 is even").

def my_second_function(input):
    for i in range(0,input + 1):
        if i % 2 == 0:
            print("{0} is even".format(i))
        else:
            print("{0} is odd".format(i))

# my_second_function(5)

# Exercise 3: Write a function that takes a number as a parameter, iterates from 0 to that number,
# and for each iteration of the loop, multiplies the current number by 9 and prints the result (e.g. "2 * 9 = 18").

def my_third_function(input):
    for i in range(0,input + 1):
        print(i," * 9 = ",i * 9)

# my_third_function(5)

# Exercise 4: Write a function that asks the user for a number and prints the sum of all numbers from 1 to the number
# they enter.

def my_forth_function():
    ind_1 = int(input("Please insert a number: "))
    ind = 0
    for i in range(1, ind_1 + 1):
        ind = ind + i
        print(ind)

# my_forth_function()

# Exercise 5: Write a function to print a factorial of a number.

def my_fifth_function(input):
    ind = 1
    for i in range(1, input + 1):
        ind = ind * i
    print(ind)

# my_fifth_function(5)

# Exercise 6: Write a function that takes a string as a parameter and returns a sting that is made up of the
# first two characters and the last two characters. If the string has a length less than 4 the program prints a
# message on the screen.For example: “hello there” will result in “here”

def my_sixth_function(input):
    print(input[0:2] + input[-2:])

my_sixth_function("lolailola")

