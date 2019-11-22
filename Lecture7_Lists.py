# Exercise 1:Write a Python function to sum all numbers in a list.

def sum_list_numbers(input):
    if type(input) == list:
        ind = False
        for i in input:
            if type(i) == int or type(i) == float:
                ind = False
            else:
                ind = True
                break
        if ind:
            print("There are values in the list that cannot be summed")
        else:
            print(sum(input))
    else:
        print("The input is not a list, please change it")

# sum_list_numbers([1,2,3,4,5])

# Exercise 2:Write a Python function to get the largest number from a list.

def largest_list_number(input):
    if type(input) == list:
        ind = False
        for i in input:
            if type(i) == int or type(i) == float:
                ind = False
            else:
                ind = True
                break
        if ind:
            print("There are values in the list that are not numeric")
        else:
            print(max(input))
    else:
        print("The input is not a list, please change it")

# largest_list_number([1,2,3.3,3.4])

# Exercise 3: Write a Python function that takes a list of words and counts how many of them begin with ‘a’.

def a_counter(input):
    if type(input) == list:
        if all(isinstance(x, str) for x in input):
            count = 0
            for i in input:
                if i[0].lower() == "a":
                    count += 1
            print(count)
        else:
            print("not all elements are strings")
    else:
        print("The input is not a list, please change it")

# a_counter(["Alvaro","Sarria","James","Andrea","albert"])

# Exercise 4: (modify Ex3) Write a Python function that takes a list of words and a character, and counts
# how many of the words in the list begin with that character.

def a_counter(input,input2):
    if type(input) == list:
        if type(input2) == str and len(input2) == 1:
            if all(isinstance(x, str) for x in input):
                count = 0
                for i in input:
                    if i[0].lower() == input2.lower():
                        count += 1
                print(count)
            else:
                print("not all elements are strings")
        else:
            print("Second input element must be a string of length 1")
    else:
        print("The input is not a list, please change it")

# a_counter(["Alvaro","Sarria","James","Andrea","albert"],"s")

# Exercise 5:Write a Python function that takes a list of numbers and returns a new list containing
# only the even numbers from the first list.

def even_elements_list(input):
    if type(input) == list:
        list2 = []
        if any(isinstance(x,bool) for x in input):
            print("Not all the elements are integers")
        elif all(isinstance(x,int) for x in input):
            for i in input:
                if i % 2 == 0:
                    list2.append(i)
            print(list2)
        else:
            print("Not all the elements are integers")
    else:
        print("The input is not a list, please change it")

# even_elements_list([1,2,3,4,5,6])