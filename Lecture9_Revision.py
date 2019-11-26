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
    file_obj = open("Files_4_Exercises/Lecture9_Ex1_1","r")
except FileNotFoundError:
    print("File not found")
else:
    i = 1
    for line in file_obj:
        if line.strip() != " "*len(line.strip()):
            word_counter(line,i)
            i += 1

# Exercise 2: Write a Python function to read a sentence and reverse every word that starts with ‘a’. Use the function
# to read text from a file, reverse each word that start with ‘a’ and save the result into another file.
#
# Exercise 3: Write a Python function replace_all(list, l_out, l_in) that takes three parameters: a list of numbers,
# a list of numbers to be replaced and a list of numbers to use as replacements.For example
# replace_all([1,2,5,6,2,7,1,2], [2,4],[200,400]) will replace all occurrences of 2 with 200 and all occurrences of
# 4 with 400 in the list [1,2,5,6,2,7,1,2], so should return [1,200,5,6,200,7,1,200]
#
# Exercise 4: Write a Python function to replace every third word in a sentence with “hello”. Use the function to read
# a text from a file, replace every third word with ‘hello’ and write the output in another file.
#
# Exercise 5: Write a Python function to replace every word in a sentence which is longer than 6 characters with
# “blah”. Use the function to read a text from a file, replace every long word with ‘blah and write the output in
# another file.
#
# Exercise 6: Write a Python program that reads text from a file and generates a dictionary – a list of unique words.
# Save those words in a new file, one word per line.
