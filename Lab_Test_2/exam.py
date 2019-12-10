# Question 1:
# Write a Python function that takes a list of numbers and returns a new list that contains only the numbers
# greater than 20 and divisibly by 3.

def first_function_exam(input_list):
    output_list = []
    for i in input_list:
        if i > 20 and i % 3 == 0:
            output_list.append(i)
    return output_list

print(first_function_exam([12,1,34,26,39,44,30,27,44,3]))

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
            # Controling that punctuation is not reversed
            if input_line_list[i][-1].isalpha():
                output_line.append(input_line_list[i][::-1])
            else:
                output_line.append(input_line_list[i][:-1][::-1]+input_line_list[i][-1])
        else:
            output_line.append(input_line_list[i])
    return " ".join(output_line)

try:
    file_obj = open("input_files/input_file","r")
except FileNotFoundError:
    print("The file does not exist or the path is incorrect, please review")
else:
    print("LOL")
    file_obj.close()