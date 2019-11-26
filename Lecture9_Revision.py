# Exercise 1: Write a Python function to read a sentence (text) and return a list of the length of each word in the
# sentence.Use the function to read text from a file and calculate the length of each word in each line.

def word_counter(first_input,second_input):
    output = first_input.split(" ")
    for i in output:
        if i == output[0]:
            print("The length fo the words for the",second_input,"sentence are:",len(i), end=", ")
        elif i == output[-1]:
            print(len(i))
        else:
            print(len(i), end = ", ")

try:
    file_obj = open("Files_4_Exercises/Lecture9_Ex1","r")
except FileNotFoundError:
    print("File not found")
else:
    i = 1
    for line in file_obj:
        if line.strip() != " "*len(line.strip()):
            word_counter(line,i)
            i += 1
    file_obj.close()

# Exercise 2: Write a Python function to read a sentence and reverse every word that starts with ‘a’. Use the function
# to read text from a file, reverse each word that start with ‘a’ and save the result into another file.

def a_word_reverser(input):
    output = input.split(" ")
    for i in output:
        if output == [""]:
            output == " "
        elif i[0].lower() == "a":
            # in case a word ends with interrogation or exlamation mark
            if i[-1].isalpha():
                output[output.index(i)] = i[::-1]
            else:
                output[output.index(i)] = i[:-1][::-1]+i[-1]
    print(" ".join(output))

try:
    file_obj = open("Files_4_Exercises/Lecture9_Ex2", "r")
except FileNotFoundError:
    print("File not found")
else:
    for line in file_obj:
        a_word_reverser(line.strip())
    file_obj.close()

# Exercise 3: Write a Python function replace_all(list, l_out, l_in) that takes three parameters: a list of numbers,
# a list of numbers to be replaced and a list of numbers to use as replacements.For example
# replace_all([1,2,5,6,2,7,1,2], [2,4],[200,400]) will replace all occurrences of 2 with 200 and all occurrences of
# 4 with 400 in the list [1,2,5,6,2,7,1,2], so should return [1,200,5,6,200,7,1,200]

def replace_all(list_init, l_out, l_in):
    # copy method to create an independent object which does not point to the value of the object copied (in memory)
    # list_to_check = list_init.copy()
    if len(l_out) != len(l_in):
        print("l_out needs to have the same length as l_in")
    else:
        list_final = []
        for i in range(0,len(list_init)):
            list_final.append(list_init[i])
            for j in range(0,len(l_out)):
                if l_out[j] == list_init[i]:
                    list_init[i] = l_in[j]
        if list_init == list_final:
            print("There is no ocurrence therefore the output list is the same:")
            print(list_init)
        else:
            print(list_init)

replace_all([1,2,5,6,2,7,1,2],[2,4],[200,400])

# Exercise 4: Write a Python function to replace every third word in a sentence with “hello”. Use the function to read
# a text from a file, replace every third word with ‘hello’ and write the output in another file.

try:
    file_obj = open("Files_4_Exercises/Lecture9_Ex3","r")
except FileNotFoundError:
    print("File not found")
else:
    file_obj_2 = open("Files_4_Exercises/Lecture9_Ex3_output","w")
    counter = 0
    for line in file_obj:
        new_line = line.strip().split(" ")
        for i in range(0,len(new_line)):
            counter += 1
            if new_line == [""]:
                counter += -1
            if counter % 3 == 0 and new_line != [""]:
                if not new_line[i][-1].isalpha():
                    new_line[i] = "hello"+new_line[i][-1]
                else:
                    new_line[i] = "hello"
        file_obj_2.write(" ".join(new_line))
        file_obj_2.write("\n")
    file_obj.close()
    file_obj_2.close()



# Exercise 5: Write a Python function to replace every word in a sentence which is longer than 6 characters with
# “blah”. Use the function to read a text from a file, replace every long word with ‘blah and write the output in
# another file.
#
# Exercise 6: Write a Python program that reads text from a file and generates a dictionary – a list of unique words.
# Save those words in a new file, one word per line.
