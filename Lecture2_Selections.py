# Exercise 1: Prompt the user to enter a mark between 0 and 100 and to print “This is a pass”
# if the mark is 40 or over, and “This is a fail” if the mark is below 40. Hint: use >=

def exam_corrector():
    exam_mark = input("Insert the your exam mark: ")
    if exam_mark.isdigit():
        if int(exam_mark) < 40:
            print("This is fail")
        else:
            print("This is a pass")
    else:
        print("You did not enter a number, please try again")
        exam_corrector()

# uncomment the function caller to get the output
# exam_corrector()

# Exercise 2:
# Prompt the user to enter an integer number, and output if the number is even or odd
# (Hint: use % to get the remainder of a division, e.g. 5%2 will return 1)

def even_odd():
    number = input("Insert a number: ")
    if number.isdigit():
        if int(number) % 2 == 0:
            print("This is an even number")
        else:
            print("This is a n odd number")
    else:
        print("This is not a number, please introduce a number")
        even_odd()

# uncomment the function caller to get the output
# even_odd()

# Exercise 3:
# Prompt the user to enter two integer numbers, and output if the first is larger,
# smaller or equal to the second one. Use if-elif-else.

def numb_comparer():
    # TODO: As to the teacher howe to do this try trick
    try:
        numb1 = float(input("Please introduce the first number: "))
    except:
        print("Invalid number, restarting program from the beginning")
        numb_comparer()
    try:
        numb2 = float(input("Please introduce the second number: "))
    except:
        print("Invalid number, restarting program from the beginning")
        numb_comparer()
    if numb1 > numb2:
        print("{0} is higher than {1}".format(numb1,numb2))
    elif numb1 < numb2:
        print("{0} is lower than {1}".format(numb1,numb2))
    else:
        print("Number 1 is equal to Number 2 ({0},{1})".format(numb1,numb2))

# uncomment the function caller to get the output
# numb_comparer()

# Exercise 4:
# It costs €1 to post a letter to Ireland, €1.70 to Europe and €2.00 to the rest of the world.
# Write a program that asks the user where do they want to post the letter to and prints the correct postage.

def mailpost_office():
    region = input("Where do you want to send the letter? ")
    while region.lower() not in ('ireland','europe','rest of the world'):
        region = input("Sorry I do not recognize that destination. please choose between: Ireland, "
                        "Europe or rest of the world? ")
    if region.lower() == 'ireland':
        print("This letter will cost you 1€")
    elif region.lower() == 'europe':
        print("This letter will cost you 1.70€")
    else:
        print("This letter will cost you 2€")

# uncomment the function caller to get the output
# mailpost_office()

# Exercise 5:
# Parking at a specific area costs €2 per hour, with the first two hours free.
# Ask the user for how long will they park for and calculate the amount they need to pay.

def parking_counter():
    # TODO: As to the teacher howe to do this try trick
    try:
        time = float(input("Introduce, in hours, how much time your car is going to be parked: "))
    except:
        print("Invalid number, restarting program from the beginning")
        parking_counter()
    if time <= 2:
        print("Free parking")
    elif time % 1 == 0:
        time_2_pay = int((time - 2))
        price = time_2_pay * 2
        print("Your car will be here for {0} hours and the first 2 hours are for free...you will have to pay for {1}"
              " hour/s which is a total of {2} euros.".format(str(time),str(time_2_pay),str(price)))
    else:
        time_2_pay = int((time - 2) // 1 + 1)
        price = time_2_pay * 2
        print("Your car will be here for {0} hours and the first 2 hours are for free...you will have to pay for {1}"
              " hour/s which is a total of {2} euros.".format(str(time),str(time_2_pay),str(price)))

# uncomment the function caller to get the output
# parking_counter()

# Exercise 6
# Write a small calculator simulator – ask the user to enter two numbers and an operation (+, -, *, /), and either add,
# subtract, multiply or divide the numbers, and print the result.

def calculator():
    float_1 = float(input("insert integer number 1:"))
    float_2 = float(input("insert integer number 2:"))
    operation = input("Select the operation you want")

    if operation == '+':
        print(float_1 + float_2)
    elif operation == '-':
        print(float_1 - float_2)
    elif operation == '*':
        print(float_1 * float_2)
    elif operation == '/':
        print(round(float_1 / float_2, 2))
    else:
        print("I do not know what you want to do")

# uncomment the function caller to get the output
# calculator()

# Exercise 7
# Write a Python program to calculate a dog's age in dog's years.
# Note: For the first two years, a dog year is equal to 10.5 human years.
# After that, each dog year equals 4 human years.

def dog_age():
    dogs_age = float(input("whats your dog's age?:"))

    if dogs_age <= 2:
        print("your dog's age is:", round(dogs_age * 10.5, 0), "human years")
    else:
        print("your dog's age is:", round(2 * 10.5 + (dogs_age - 2) * 4, 2), "human years")

# uncomment the function caller to get the output
# dog_age()

# Exercise 8
# Write a Python program to convert month name to a number of days.

def month_days():
    # TODO: check februaries for "años bisiestos"
    month_name_selected = input("insert month name")
    month_names = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                   "November", "December")

    if month_name_selected in month_names:
        if month_name_selected == 'February':
            print("N. days = 28/29")
        elif month_name_selected in ("January", "March", "May", "July", "August", "October", "December"):
            print("N. days = 31")
        else:
            print("N. days = 30")
    else:
        print("that month does not exist!")

# uncomment the function caller to get the output
# month_days()