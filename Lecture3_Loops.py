# Exercise 1:
# Write a WHILEloop that will print the numbers from 1 to 10 on the screen.

def printer():
    i = 1
    while i <= 10:
        print(i)
        i = i + 1

# uncomment the function caller to get the output
# printer()

# Exercise 2:
# Write a FOR loop that will print the numbers from 1 to 10 on the screen.

def printer2():
    for i in range(1,10+1):
        print(i)

# uncomment the function caller to get the output
# printer2()

# Exercise 3:
# Write a FOR loop that will iterate from 0 to 20. For each iteration, it will check if the current number
# is even or odd, and report that to the screen (e.g. "1 is odd, 2 is even").

def odd_even():
    for i in range(0,20+1):
        if i == 0 or i % 2 == 0:
            print("{0} is an even number".format(str(i)))
        else:
            print("{0} is an odd number".format(str(i)))

# uncomment the function caller to get the output
# odd_even()

# Exercise 4:
# Write a FOR loop that will iterate from 0 to 10. For each iteration of the loop, it will
# multiply the number by 9 and print the result (e.g. "2 * 9 = 18").
# Bonus (complete at the end of the class once you are comfortable with loops):Use a nested loop to show
# the tables for every multiplier from 1 to 10 (100 results total).

def muiltiplier():
    for i in range(0, 10+1):
        for j in range(0, 10+1):
            print(str(i) + " * " + str(j) + " = " + str(i*j))

# uncomment the function caller to get the output
# muiltiplier()

# Exercise 5:
# Write a program that asks the user for a number and prints the sum of all numbers from 1 to the number they enter.

def summing():
    number_threshold = int(input("Introduce a number: "))
    count = 0
    for i in range(1, number_threshold + 1):
        count = count + i
    print(count)

# uncomment the function caller to get the output
# summing()

# Exercise 6:
# Write a program to calculate and print the factorial of a number using a FOR loop. The factorial of a number is
# the product of all integers up to and including that number, so the factorial of 4 is 4*3*2*1= 24

def factorial():
    number_threshold = int(input("Introduce a number: "))
    count = 1
    for i in range(1, number_threshold + 1):
        count = count * i
    print(count)

# uncomment the function caller to get the output
# factorial()

# Exercise 7:
# Ask the user to enter a number and print it back on the screen. Keep asking for a new number
# until they enter a negative number.

def negativism():
    number = int(input("Introduce a number: "))
    while number > 0:
        print(number)
        number = int(input("Introduce a number: "))
    print(number)

# uncomment the function caller to get the output
# negativism()

# Exercise 8:
# Write a program that uses loops to print the triangle below
# Hint 1: you will need to use nested loops.
# Hint 2: on line 1 we print 1 *, on line 2 we print 2 stars... on line x we print x stars...)

def tirangle():
    # for i in range(1, 6):
    #     print(" *" * i)
    #
    for i in range(1,6):
        str = ""
        for j in range(1,i+1):
            str = str + " *"
        print(str)

# uncomment the function caller to get the output
# tirangle()

# Exercise 9:
# Write a program that uses loops to print the triangle below (hint: you will need to use nested loop)

def numeric_triangle():
    for i in range(1,6):
        num = ""
        for j in range(1,i+1):
            num = num + " " +str(j)
        print(num)

# uncomment the function caller to get the output
# numeric_triangle()