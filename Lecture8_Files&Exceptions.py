file_path = "C://Users//alvar//Documents//DT265C - Fundamentals of Computing//Object Oriented SW - GitHub//" \
            "Lecture8_Files&Exceptions//"

# Exercise 1: Write a Python program that opens a text file, reads the contents line by line and saves it
# into a second file. Make sure you use try/except to handle and possible problems with incorrect filenames.

def open_ex1():
    try:
        file_obj = open(file_path + "twinkle.txt", "r")
        file_obj_2 = open(file_path + "twinkle_ex1.txt", "w")
    except FileNotFoundError:
        print("The file you are trying to read does not exist")
    else:
        for line in file_obj:
            print(line.strip())
            # print(line.strip(), file=file_obj_2)
            file_obj_2.write(line.strip() + "\n")

        print("Second file created correctly")
        file_obj.close()
        file_obj_2.close()

# open_ex1()

# Exercise 2: Write a Python program that opens a text file, reads the contents line
# by line and prints each line in reverse.

def open_ex2():
    try:
        file_obj = open(file_path + "twinkle.txt", "r")
        file_obj_2 = open(file_path + "twinkle_ex2.txt", "w")
    except FileNotFoundError:
        print("The file you are trying to read does not exist")
    else:
        for line in file_obj:
            my_line = list(line.strip())
            my_line.reverse()
            # print("".join(my_line), file=file_obj_2)
            file_obj_2.write("".join(my_line) + "\n")

        print("Second file created correctly")
        file_obj.close()
        file_obj_2.close()

# open_ex2()

# Exercise 3: Write a Python program that reads a text file and prints only the lines that start with 'When'.

def open_ex3():
    try:
        file_obj = open(file_path + "twinkle.txt", "r")
    except FileNotFoundError:
        print("The file you are trying to read does not exist")
    else:
        for line in file_obj:
            if line.strip()[0:4] == "When":
                print(line.strip())

        file_obj.close()

# open_ex3()

# Exercise 4: Write a Python program that reads a text file and prints the length of each line.

def open_ex4():
    try:
        file_obj = open(file_path + "twinkle.txt", "r")
    except FileNotFoundError:
        print("The file you are trying to read does not exist")
    else:
        for line in file_obj:
            # Count by characters
            print(len(list(line.strip())))
            # Count by words
            # print(len(line.strip().split(" ")))

        file_obj.close()

# open_ex4()