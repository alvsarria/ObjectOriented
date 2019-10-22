# Exercise 1:
# Write a program which will finds and prints all numbers between 2000 and 3200 (both included)
# which are divisible by 7 but are not a multiple of 5.

def discover_numb():
    for i in range(2000, 3200 + 1):
        if (i % 7 == 0) and (i % 5 != 0):
            print(i)

# uncomment the function caller to get the output
# discover_numb()

# Exercise 2:
# Write a Python program that will count how many digits (0-9) are in a string entered by the user.
# Hint: To check if a string c represents a digit you can check if c is between ‘0’ and ‘9’Alternative way would be
# to use c.isdigit() which returns True if c represents a digit and False otherwise. You’ll need to use a loop to get
# every character of the string.

def string_breakdown():
    string = input("Introduce a string with digits and characters: ")
    digit_counter = 0
    chr_counter = 0
    for i in string:
        if i.isdigit():
            digit_counter += 1
        elif i.isalpha() and i != " ":
            chr_counter += 1
    print("The total number of digits is {0}".format(str(digit_counter)))
    print("The total number of characters is {0}".format(str(chr_counter)))

string_breakdown()

# Exercise 3:
# Extend your program from Exercise 2 and write a program to count how many digits (0-9) and how many letters
# (a-z or A-Z) are in a sentence entered by the user.

# Exercise 4:
# Write a Python program to find and print the sum of digits of a number entered by the user.
# Hint: There are different ways of approaching this problem. One way would be to read the number as a
# string and use a loop to iterate over it to get each digit.

# Exercise 5:
# Write a Python program to keep asking the user to enter positive numbers and terminates when they
# enter a negative. When the program terminates, print how many positive numbers were entered and what
# was the smallest number.
# Hint: You can use a while-loop to keep asking the user to enter a number, the loop will keep going while
# they enter a value >0. Once the loop is working correctly see how you’d add a condition to keep track of
# the current smallest value and update it when a smaller value is found