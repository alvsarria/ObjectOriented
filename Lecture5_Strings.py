# Exercose 1:
# Write a Python program to print each character of a string on single line.

def printing_inline():
    your_string = input("Please insert the string you want to be printed inline:")
    for i in your_string:
        print(i, end=" ")

# uncomment the function caller to get the output
# printing_inline()

# Exercise 2:
# Write a Python program that will calculate the length of a string

def length_calculator():
    your_string = input("Please insert the string you want to get length from:")
    n_len = 0
    for i in your_string:
        n_len = n_len + 1

    print("The length of your string is: \n" + str(n_len))

# uncomment the function caller to get the output
# length_calculator()

# Exercise 3:
# Write a Python program that reads a string and prints a string that is made up
# of the first two characters and the last two characters. If the string has a length
# less than 4 the program prints a message on the screen.

def word_juggler():
    your_string = input("Please insert the string you want to get length from:")
    if len(your_string) < 4:
        print("number of characters of the string less than 4")
    else:
        print(your_string[:2] + your_string[-2:])

# uncomment the function caller to get the output
# word_juggler()

# Exercise 4:
# Write a Python program that will reverse a string (using a loop, not using slicing)

def word_reverser():
    your_string = input("Please insert the string you want to get reversed:")
    new_string = ""
    for i in range(1, len(your_string) + 1):
        new_string = new_string + your_string[-i]

    print(new_string)

# uncomment the function caller to get the output
# word_reverser()

# Exercise 5:
# Write a Python program that will “encrypt” a string. The encryption algorithm we’ll use is add 1 to
# the ASCII code, so ‘a’ becomes ‘b’, ‘b’ becomes ‘c’, etc. The string ‘abc’ becomes ‘bcd’You’ll need to use the
# functions ord() and chr() discussed in class.
# Hint: To encrypt the letter ‘a’ take the ASCII code of ‘a’ 97, add 1 (98)
# and find the character with ASCII code 98 (‘b’). So ‘a’ encrypted becomes ‘b’

def word_encryptor():
    your_string = input("Please insert the string you want to encrypt:")
    new_string = ""
    for i in range(0, len(your_string)):
        new_string = new_string + chr(ord(your_string[i]) + 1)

    print(new_string)

# uncomment the function caller to get the output
# word_encryptor()

# Exercise 6:
# Write a Python program that will swap two random letters in a string.
# Hint: Random letters means “letters with random index”random.randint(x,y) will return a randomnumber in
# the range fromx to y inclusive. You need to import random at the top of your program.
# You’ll also need to use slicing –splitting your string into substrings.

from random import randint

def word_messer():
    your_string = input("Please insert the string you want to mess with:")

    if len(your_string) <= 1:
        print("impossible to mess around")
        word_messer()
    elif your_string == len(your_string) * your_string[0]:
        print("impossible to mess around")
        word_messer()
    elif (len(your_string) - your_string.count(" ")) < 2:
        print("impossible to mess around")
        word_messer()
    else:
        first_letter_indx = randint(0, len(your_string) - 1)
        if your_string[first_letter_indx] == " ":
            while your_string[first_letter_indx] == " ":
                first_letter_indx = randint(0, len(your_string) - 1)

        second_letter_indx = first_letter_indx
        while first_letter_indx == second_letter_indx or your_string[second_letter_indx] == " " or \
                your_string[first_letter_indx] == your_string[second_letter_indx]:
            second_letter_indx = randint(0, len(your_string) - 1)

        for i in range(0, len(your_string)):
            if i == first_letter_indx:
                print(your_string[second_letter_indx], end="")
            elif i == second_letter_indx:
                print(your_string[first_letter_indx], end="")
            else:
                print(your_string[i], end="")

# uncomment the function caller to get the output
# word_messer()

# Exercise NA: Speed control test.

def speed_control():
    pts = 12
    while pts != 0:
        sp = int(input("insert speed here: "))
        if sp <= 70:
            print("Under speed limit, good to go")
        else:
            pts = pts - (sp - 70) // 5
            print("Above speed limit, you get", (sp - 70) // 5, "point less")
            if pts == 0 or pts < 0:
                pts = 0
                print("That was your last points, driving license revoked")

# uncomment the function caller to get the output
#speed_control()

# playing around
from math import pi as lol

def some_maths(x, y, z):
    a = round((x + y) * lol, 2)
    b = y + z
    c = round((z + x) / lol, 2)
    print(a, b, c)

# uncomment the function caller to get the output
#some_maths(3,3,3)