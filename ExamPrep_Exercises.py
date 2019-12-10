##
## First Lecture
##

# Exercise 1:
# Write a Python program to ask the user for their name
# (e.g. John) and print "Hello John" on the screen

name = input("Please insert your name: ")
print("Hello {0}".format(name))

# Exercise 2:
# Write a Python program to ask the user for their name and age,
# and print them on the screen in the format "Hello John, you are 20 years old"

name = input("Please insert your name: ")
age = input("Please insert your age: ")
print("Hello {name}, you are {age} years old".format(name=name, age=age))

# Exercise 3:
# Write a Python program to ask the user for width and height of a rectangle and print the area.

width = float(input("Please insert width of rectangle (m): "))
height = float(input("Please insert height of rectangle (m): "))
print("The area of the rectangle is:", round(width * height, 4), "m^2")


##
## Second Lecture
##

# Exercise 1: Prompt the user to enter a mark between 0 and 100 and to print “This is a pass”
# if the mark is 40 or over, and “This is a fail” if the mark is below 40. Hint: use >=

mark = int(input("Insert your mark (0-100)"))
if mark >= 40:
    print("This is a pass")
else:
    print("This is a fail")

# Exercise 2:
# Prompt the user to enter an integer number, and output if the number is even or odd
# (Hint: use % to get the remainder of a division, e.g. 5%2 will return 1)

number = int(input("Please insert a number (integer): "))
if number % 2 == 0:
    print("Number is even!")
else:
    print("Number is odd!")

# Exercise 3:
# Prompt the user to enter two integer numbers, and output if the first is larger,
# smaller or equal to the second one. Use if-elif-else.

n1 = float(input("Insert one number: "))
n2 = float(input("Insert another number "))
if n1 > n2:
    print("{0} is bigger than {1}".format(n1,n2))
elif n1 == n2:
    print("{0} is equal than {1}".format(n1, n2))
else:
    print("{0} is smaller than {1}".format(n1, n2))

# Exercise 4:
# It costs €1 to post a letter to Ireland, €1.70 to Europe and €2.00 to the rest of the world.
# Write a program that asks the user where do they want to post the letter to and prints the correct postage.

destination = input("Please insert where you want to send this letter (Ireland, Europe, rest of the world): ")
if destination.lower() == "ireland":
    print("cost is 1€")
elif destination.lower() == "europe":
    print("cost is 1.70€")
else:
    print("cost is 2.00€")

# Exercise 5:
# Parking at a specific area costs €2 per hour, with the first two hours free.
# Ask the user for how long will they park for and calculate the amount they need to pay.

time_parked = int(input("Please introduce how many hours you will have the car parked"))
if time_parked <= 2:
    print("Parking is free!")
else:
    print("Total amount is",(time_parked-2)*2,"€")

# Exercise 6
# Write a small calculator simulator – ask the user to enter two numbers and an operation (+, -, *, /), and either add,
# subtract, multiply or divide the numbers, and print the result.

n1 = float(input("input first number: "))
n2 = float(input("input second number: "))
operation = input("input the operation: ")
if operation.strip() == '+':
    print(n1 + n2)
elif operation.strip() == '-':
    print(n1 - n2)
elif operation.strip() == '*':
    print(n1 * n2)
elif operation.strip() == '/':
    print(n1 / n2)
else:
    print("operation unknown")

# Exercise 7
# Write a Python program to calculate a dog's age in dog's years.
# Note: For the first two years, a dog year is equal to 10.5 human years.
# After that, each dog year equals 4 human years.

age = int(input("Insert dog's age: "))
if age <= 2:
    print("Dog's age is",10.5*age,"years")
else:
    print("Dog's age is",10.5*2+4*(age-2),"years")

# Exercise 8
# Write a Python program to convert month name to a number of days.

month_name_selected = input("insert month name")
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                "November", "December"]
if month_name_selected.lower() in [x.lower() for x in month_names]:
    if month_name_selected == 'February':
        print("N. days = 28/29")
    elif month_name_selected in ("January", "March", "May", "July", "August", "October", "December"):
        print("N. days = 31")
    else:
        print("N. days = 30")
else:
    print("that month does not exist!")


##
## Third Lecture
##

# Exercise 1:
# Write a WHILEloop that will print the numbers from 1 to 10 on the screen.

n = 1
while n <= 10:
    print(n)
    n += 1

# Exercise 2:
# Write a FOR loop that will print the numbers from 1 to 10 on the screen.

for i in range(1,10+1):
    print(i)

# Exercise 3:
# Write a FOR loop that will iterate from 0 to 20. For each iteration, it will check if the current number
# is even or odd, and report that to the screen (e.g. "1 is odd, 2 is even").

for i in range(0,20+1):
    if i % 2 == 0:
        print("{0} is even".format(i))
    else:
        print("{0} is odd".format(i))

# Exercise 4:
# Write a FOR loop that will iterate from 0 to 10. For each iteration of the loop, it will
# multiply the number by 9 and print the result (e.g. "2 * 9 = 18").
# Bonus (complete at the end of the class once you are comfortable with loops):Use a nested loop to show
# the tables for every multiplier from 1 to 10 (100 results total).

for i in range(0,10+1):
    for j in range(0,10+1):
        print(i,"*",j,"=",i*j)

# Exercise 5:
# Write a program that asks the user for a number and prints the sum of all numbers from 1 to the number they enter.

number = int(input("Insert a number: "))
count = 0
for i in range(1,number + 1):
    count += i
print(count)

# Exercise 6:
# Write a program to calculate and print the factorial of a number using a FOR loop. The factorial of a number is
# the product of all integers up to and including that number, so the factorial of 4 is 4*3*2*1= 24

number = int(input("Insert a number: "))
count = 1
for i in range(1,number + 1):
    count *= i
print(count)

# Exercise 7:
# Ask the user to enter a number and print it back on the screen. Keep asking for a new number
# until they enter a negative number.

n = 0
while not n < 0:
    n = int(input("Please introduce a number: "))

# Exercise 8:
# Write a program that uses loops to print the triangle below
# Hint 1: you will need to use nested loops.
# Hint 2: on line 1 we print 1 *, on line 2 we print 2 stars... on line x we print x stars...)

for i in range(1,5+1):
    print("* "*i)

# Exercise 9:
# Write a program that uses loops to print the triangle below (hint: you will need to use nested loop)

for i in range(1,5+1):
    for j in range(1,i+1):
        print(j, end = " ")
    print(end = "\n")


##
## Fourth Lecture
##

# Exercise 1:
# Write a program which will finds and prints all numbers between 2000 and 3200 (both included)
# which are divisible by 7 but are not a multiple of 5.

for i in range(2000,3200+1):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

# Exercise 2:
# Write a Python program that will count how many digits (0-9) are in a string entered by the user.
# Hint: To check if a string c represents a digit you can check if c is between ‘0’ and ‘9’Alternative way would be
# to use c.isdigit() which returns True if c represents a digit and False otherwise. You’ll need to use a loop to get
# every character of the string.

user_string = input("Insert string with digits")
count_1 = 0
count_2 = 0
for i in user_string:
    if i.isdigit():
        count_1 += 1
    elif i.isalpha():
        count_2 += 1
print("Total number of digits is {0}, total number of letters is {1}".format(count_1,count_2))

# Exercise 3:
# Extend your program from Exercise 2 and write a program to count how many digits (0-9) and how many letters
# (a-z or A-Z) are in a sentence entered by the user.

# Solution is the same as in exercise 2

# Exercise 4:
# Write a Python program to find and print the sum of digits of a number entered by the user.
# Hint: There are different ways of approaching this problem. One way would be to read the number as a
# string and use a loop to iterate over it to get each digit.

# option 1
number = input("Insert a number: ")
print(sum(int(digit) for digit in str(number)))

# option 2
number = int(input("Insert a number: "))
s = 0
while number:
    s += number % 10
    number //= 10
print(s)


# Exercise 5:
# Write a Python program to keep asking the user to enter positive numbers and terminates when they
# enter a negative. When the program terminates, print how many positive numbers were entered and what
# was the smallest number.
# Hint: You can use a while-loop to keep asking the user to enter a number, the loop will keep going while
# they enter a value >0. Once the loop is working correctly see how you’d add a condition to keep track of
# the current smallest value and update it when a smaller value is found

n = 0
counter = 0
min = float("inf")
while not n < 0:
    n = int(input("Insert a number"))
    if n > 0:
        counter += 1
    if n < min and not n < 0:
        min = n
print("Negative number introduced {0}, the count of total positive numbers is {1} and the minimum number was {2}"
      .format(str(n),str(counter),str(min)))


##
## Fifth Lecture
##

# Exercose 1:
# Write a Python program to print each character of a string on single line.

string_input = input("Please insert a string: ")
for i in string_input:
    print(i, end = " ")

# Exercise 2:
# Write a Python program that will calculate the length of a string

string_input = input("Please insert a string: ")
counter = 0
for i in string_input:
    counter += 1
print(counter)

# Exercise 3:
# Write a Python program that reads a string and prints a string that is made up
# of the first two characters and the last two characters. If the string has a length
# less than 4 the program prints a message on the screen.

string_input = input("Please insert a string: ")
if len(string_input) < 4:
    print("String length less than 4")
else:
    print(string_input[:2]+string_input[-2:])

# Exercise 4:
# Write a Python program that will reverse a string (using a loop, not using slicing)

#option 1
string_input = input("Please insert a string: ")
new_string = ""
for i in range(len(string_input)-1,-1, -1):
    new_string += string_input[i]
print(new_string)

#option 2
string_input = input("Please insert a string: ")
new_string = ""
for i in range(0,len(string_input)):
    new_string += string_input[(len(string_input)-1)-i]
print(new_string)

#option 3
string_input = input("Please insert a string: ")
new_string = ""
for i in range(1,len(string_input)+1):
    new_string += string_input[-i]
print(new_string)

# Exercise 5:
# Write a Python program that will “encrypt” a string. The encryption algorithm we’ll use is add 1 to
# the ASCII code, so ‘a’ becomes ‘b’, ‘b’ becomes ‘c’, etc. The string ‘abc’ becomes ‘bcd’You’ll need to use the
# functions ord() and chr() discussed in class.
# Hint: To encrypt the letter ‘a’ take the ASCII code of ‘a’ 97, add 1 (98)
# and find the character with ASCII code 98 (‘b’). So ‘a’ encrypted becomes ‘b’

string_input = input("Please insert a string: ")
encrypted_output = ""
for i in string_input:
    encrypted_output += chr(ord(i)+1)
print(encrypted_output)

# Exercise 6:
# Write a Python program that will swap two random letters in a string.
# Hint: Random letters means “letters with random index”random.randint(x,y) will return a randomnumber in
# the range fromx to y inclusive. You need to import random at the top of your program.
# You’ll also need to use slicing –splitting your string into substrings.

from random import randint
string_input = input("Please insert a string: ")
if len(string_input) <= 1:
    print("impossible to computate due to string length")
elif len(string_input) == 2:
    print(string_input[::-1])
else:
    first_rand_index = randint(0, len(string_input) - 1)
    while first_rand_index == len(string_input) - 1:
        first_rand_index = randint(0, len(string_input) - 1)
    second_rand_index = randint(0, len(string_input) - 1)
    while second_rand_index == first_rand_index:
        second_rand_index = randint(0, len(string_input) - 1)
    if first_rand_index < second_rand_index:
        print(string_input[0:first_rand_index] + string_input[second_rand_index] +
              string_input[first_rand_index + 1:second_rand_index] + string_input[first_rand_index] +
              string_input[second_rand_index + 1:])
    else:
        print(string_input[0:second_rand_index] + string_input[first_rand_index] +
              string_input[second_rand_index + 1:first_rand_index] + string_input[second_rand_index] +
              string_input[first_rand_index + 1:])

# Exercise NA: Speed control test.

##
## Sixth Lecture
##

# Exercise 1: Write a function that takes a number as a parameter and prints the numbers from 1
# to that number on the screen.

def first_function(inp1):
    for i in range(1,inp1+1):
        print(i)

first_function(5)

# Exercise 2: Write a function that takes a number as a parameter and iterates from 0 to that number.
# For each iteration, it will check if the current number is even or odd, and report that to the screen
# (e.g. "1 is odd, 2 is even").

def second_function(inp1):
    for i in range(0,inp1+1):
        if i % 2 == 0:
            print("{0} is even".format(i))
        else:
            print("{0} is odd".format(i))

second_function(6)

# Exercise 3: Write a function that takes a number as a parameter, iterates from 0 to that number,
# and for each iteration of the loop, multiplies the current number by 9 and prints the result (e.g. "2 * 9 = 18").

def third_function(inp1):
    for i in range(0,inp1+1):
        print(i,"* 9 =",i*9)

third_function(10)

# Exercise 4: Write a function that asks the user for a number and prints the sum of all numbers from 1 to the number
# they enter.

def fourth_function(inp1):
    counter = 0
    for i in range(0,inp1+1):
        counter += i
    return counter

print(fourth_function(5))

# Exercise 5: Write a function to print a factorial of a number.

def fifth_function(inp1):
    counter = 1
    for i in range(1, inp1 + 1):
        counter *= i
    return counter

print(fifth_function(4))

# my_fifth_function(5)

# Exercise 6: Write a function that takes a string as a parameter and returns a sting that is made up of the
# first two characters and the last two characters. If the string has a length less than 4 the program prints a
# message on the screen.For example: “hello there” will result in “here”

def sixth_function(inp1):
    return inp1[0:2] + inp1[-2:]

print(sixth_function("hello there"))

# Exercise 7: Write a Python program to remove the characters which have odd index values of a given string.
# The function should return the new string.

def seventh_function(inp1):
    return inp1[1:len(inp1):2]

print(seventh_function("HelloWorld"))

# Exercise 8: Write a Python function to get the first half of a specified string of even lengthSample function and
# result:string_first_half('Python') should return Pyt

def eigth_function(input):
    if not len(input) % 2 == 0:
        return "String length not even"
    else:
        return input[0:int(len(input)/2)]

print(eigth_function("Alvaro"))

# Exercise 9: Write a Python function to insert a string in the middle of a string. Sample function
# and result:insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def nineth_function(wrapper, input):
    if not len(wrapper) % 2 == 0:
        return "Wrapper string is not even"
    else:
        return wrapper[0:int(len(wrapper)/2)] + input + (wrapper[int(len(wrapper)/2):])

print(nineth_function("{{}}", "PHP"))

# Exercise 10: Write a Python function that takes a string and two indices, and returnsa
# string with the part between the indices removed.For example: remove_substring(“Hellothere”, 2, 6) -> “Hehere”

def tenth_function(input,ind1,ind2):
    if ind1 < 0 or ind2 < 0 or ind2 <= ind1:
        return "negative indexes not allowed or second index needs to be higher than first index"
    else:
        return input[:ind1]+input[ind2:]

print(tenth_function("Hellothere", 2, 6))

##
## Seventh Lecture
##
