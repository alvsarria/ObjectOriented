# Question 1:
# Write a Python function that takes a list of numbers and returns a new list that contains only the numbers
# greater than 20 and divisibly by 3.

def first_function_exam(input_list):
    if type(input_list) == list:
        print("Input list is:",input_list)
        output_list = []
        for i in input_list:
            # Handling cases in where the element of the list is not a number
            try:
                i > 20 and i % 3 == 0
            except TypeError:
                print("'{0}' is a non numeric value, deprecating...".format(i))
            else:
                if i > 20 and i % 3 == 0:
                    output_list.append(i)
        if len(output_list) == 0:
            return "None of the numbers in the list fulfills the criteria"
        else:
            return "Final list is: {0}".format(output_list)
    else:
        return "Input is not a list, please change it"

print("Question 1:")

print(first_function_exam([12,1,"c",34,26,"!",39,44,30,27,44,3,"a"]))
# Uncomment below to see different behavior with different inputs
# print("-----")
# print(first_function_exam([1]))
# print("-----")
# print(first_function_exam(1))

# Question 2:
# a) Write a Python function that will take a text (sentence) and will reverse every second word.
# You can ignore punctuation (consider it part of the word)
# b) Use the function from part (a) in a program, that reads text from a file and reverses every second word in each
# line. Save the "reversed" text in a second file.

def second_function_exam(input_line):
    input_line_list = input_line.split(" ")
    output_line = []
    for i in range(0,len(input_line_list)):
        if (i+1) % 2 == 0:
            # Controlling that punctuation is not reversed
            if input_line_list[i][-1].isalpha():
                output_line.append(input_line_list[i][::-1])
            else:
                output_line.append(input_line_list[i][:-1][::-1]+input_line_list[i][-1])
        else:
            output_line.append(input_line_list[i])
    return " ".join(output_line)

print("\n")
print("Question 2:")

# Important: I am using a relative path please if this does not work use the absoulte path to the folders and file
# downloaded in your local machine along this script file
try:
    file_obj = open("Input/text_file","r")
except FileNotFoundError:
    print("File does not exist or the file path is incorrect, please review this")
else:
    file_obj_2 = open("Output/text_file_result","w")
    for line in file_obj:
        file_obj_2.write(second_function_exam(line.strip()))
        file_obj_2.write("\n")
    file_obj.close()
    file_obj_2.close()
    print("File successfully reversed and copied")