# function to upload the inventory information stored in our external .txt database into our program.
# reads information from a .txt external file and converts the information in a dictionary data type element
def upload_inventory():
    library_inventory = {}
    # error handling in case .txt file cannot be found in the directory
    try:
        file_obj = open("dbs/library_inventory.txt", "r")
    except FileNotFoundError:
        print("The external library database does not exist or cannot be found")
    else:
        # every row in the .txt file contains information segmented by ";;" - splitting row string by ";;" after
        # reading it from file to build our library dictionary
        for line in file_obj:
            row = (line.strip()).split(";;")
            library_inventory[row[0]] = [row[1], row[2], row[3], row[4]]
        file_obj.close()
    return library_inventory

# function to upload the user information for checked out books into our program, .txt external database
# reads information from a .txt external file and converts the information in a list data type element
def upload_log():
    user_log_file = []
    # error handling in case .txt file cannot be found in the directory
    try:
        file_obj = open("dbs/checkout_books_log_file.txt", "r")
    except FileNotFoundError:
        print("The external user log file database does not exist or cannot be found")
    else:
        # every row in the .txt file has a title checked out by the user, passing this information to a list
        for line in file_obj:
            row = line.strip()
            user_log_file.append(row)
        file_obj.close()
    return user_log_file

# function to bulk the inventory information from our program into the external .txt database
# writes information coming from a dictionary data type element into a .txt file
def download_inventory(inventory):
    file_obj = open("dbs/library_inventory.txt", "w")
    # same logic used for the upload functions but in the other way around, from dictionary data type to .txt file
    for i in inventory:
        element = [i, inventory[i][0], inventory[i][1], inventory[i][2], inventory[i][3]]
        file_obj.write(";;".join(element) + "\n")
    file_obj.close()

# function to bulk the user log information from our program into the external .txt database
# writes information coming from a list data type element into a .txt file
def download_log_file(user_log_file):
    file_obj = open("dbs/checkout_books_log_file.txt", "w")
    # same logic used for the upload functions but in the other way around, from list data type to .txt file
    for i in user_log_file:
        element = i.strip()
        file_obj.write(element + "\n")
    file_obj.close()

# function to print all the details of all the books in the library
# prints all the information in a friendly way in relation of the number of strings of all the elements
def status_inventory():
    print("")
    print("[CONSOLE] - Please see all the details of the books in this library:")
    # uploading inventory information from the external database
    inventory = upload_inventory()
    # crearing empty lists to store lengths of strings
    isbn = []
    title = []
    author = []
    amount = []
    # appending string lengths into lists
    for i in inventory:
        isbn.append(len(i))
        title.append(len(inventory[i][0]))
        author.append(len(inventory[i][1]))
        amount.append(len(inventory[i][2]))
    # selecting maximum lengths per string contained in list
    isbn.sort(reverse = True)
    max_len_isbn = isbn[0]
    author.sort(reverse=True)
    max_len_author = author[0]
    title.sort(reverse=True)
    max_len_title = title[0]
    amount.sort(reverse=True)
    max_len_amount = amount[0]
    # in case filed name is longer than the longest string contained in the list, switch values
    if max_len_isbn < len("ISBN"):
        max_len_isbn_diff = len("ISBN")
    else:
        max_len_isbn_diff = max_len_isbn
    if max_len_title < len("TITLE"):
        max_len_title_diff = len("TITLE")
    else:
        max_len_title_diff = max_len_title
    if max_len_author < len("AUTHOR"):
        max_len_author_diff = len("AUTHOR")
    else:
        max_len_author_diff = max_len_author
    if max_len_amount < len("AMOUNT"):
        max_len_amount_diff = len("AMOUNT")
    else:
        max_len_amount_diff = max_len_amount
    # printing inventory status in a nice way
    print("")
    print((3 + max_len_isbn_diff) * "#" + (3 + max_len_title_diff) * "#" +
          (3 + max_len_author_diff) * "#" + (4 + max_len_amount_diff) * "#")
    print("|" + " " * (int(round((3 + max_len_isbn_diff) / 2,0)) - int(round(4 / 2,0)) - 1) + "ISBN" +
          ((3 + max_len_isbn_diff) - (int(round((3 + max_len_isbn_diff) / 2,0)) + int(round(4 / 2,0)))) * " " +
          "|" + " " * (int(round((3 + max_len_title_diff) / 2, 0)) - int(round(5 / 2, 0)) - 1) + "TITLE" +
          ((3 + max_len_title_diff) - (int(round((3 + max_len_title_diff) / 2,0)) + int(round(5 / 2,0))) - 1) * " " +
          "|" + " " * (int(round((3 + max_len_author_diff) / 2, 0)) - int(round(6 / 2, 0)) - 1) + "AUTHOR" +
          ((3 + max_len_author_diff) - (int(round((3 + max_len_author_diff) / 2, 0)) + int(round(6 / 2, 0)))) * " " +
          "| AMOUNT |")
    print((3 + max_len_isbn) * "#" + (3 + max_len_title) * "#" +
          (3 + max_len_author) * "#" + (4 + max_len_amount_diff) * "#")
    for i in inventory:
        print(("| " + i + " " * ((3 + max_len_isbn_diff)-len(i)-2)) +
              ("| " + inventory[i][0] + " " * ((3 + max_len_title_diff)-len(inventory[i][0])-2)) +
              ("| " + inventory[i][1] + " " * ((3 + max_len_author_diff)-len(inventory[i][1])-2)) +
              ("| " + inventory[i][2] + "/" + inventory[i][3]  + " " *
               ((3 + max_len_amount_diff)-(len(inventory[i][2]) + len(inventory[i][3]) + 1)-2)) + "|")
    print((3 + max_len_isbn) * "#" + (3 + max_len_title) * "#" +
          (3 + max_len_author) * "#" + (4 + max_len_amount_diff) * "#")

# function to print all the books borrowed by the user
def status_log_file():
    # uploading user log information from the external database
    log_file = upload_log()
    # flow control to avoid errors coming from empy user log files (i.e. user w/o any book borrowed)
    if len(log_file) == 0:
        print("")
        print("[CONSOLE] - No books checked out")
    else:
        print("")
        print("[CONSOLE] - The books you have checked out are: ")
        print("")
        print((4 + 49) * "#")
        print("|" + " " * 22 + "TITLE/S" + " " * 22 + "|")
        print((4 + 49) * "#")
        for i in log_file:
            print("| " + i + " " * (50 - len(str(i))) + "|")
        print((4 + 49) * "#")

# function to add books to the library, even if they already exist in the library (add more copies)
# asks for a ISBN code to the user: if exists asks whether the user wants to add more copies or not, if it does not
# exist includes the new information into the inventory existing one and updates the external data base
def add():
    # uploading inventory information from the external database
    inventory = upload_inventory()
    # introduce user inputs for isbn and introducing quality input checks
    print("")
    isbn = input("[CONSOLE] - Please enter the ISBN number of the book you want to add to the library: ")
    # flow control to avoid users inserting non numeric values or values which a length different than 13
    while len(isbn) != 13 or not isbn.isdigit():
        print("")
        isbn = input("[CONSOLE][ERROR] - Remember the isbn has to be numerical and it has to have 13 numbers, "
                     "please try again:  ")
    # if the book already exists in our library, provide option to increase number of copies
    if isbn in inventory.keys():
        print("")
        print("[CONSOLE][ALERT] - This book is already in the library")
        # if ISBN is already in the library give the choice to increase the number of copies
        print("")
        add_book_ind = input("[CONSOLE] - Do you want to add more copies to the library? (Y/N)")
        # flow control to guide user and avoid computation errors
        while add_book_ind.lower() not in ["y","n"]:
            print("")
            add_book_ind = input( "[CONSOLE][ERROR] - I do not understand your command please use Y for yes or N for "
                                  "no, please try again: ")
        if add_book_ind.lower() == "y":
            print("")
            new_amount = input("[CONSOLE] - Please enter the amount of books you want to add: ")
            # flow control to avoid user adding more than 9 copies at a time (this is a personal requirement) or not
            # inserting a numeric value
            while int(new_amount) >= 10 or not new_amount.isdigit():
                print("")
                new_amount = input("[CONSOLE][ERROR] - Remember the amount has to be numerical and we cannot add more "
                                   "than 9 copies at a time, please try again:  ")
            # updating dictionary with the new values
            inventory[isbn][2] = str(int(inventory[isbn][2]) + int(new_amount))
            inventory[isbn][3] = str(int(inventory[isbn][3]) + int(new_amount))
            print("")
            print("[CONSOLE] - " + new_amount + " copies added to the existing library, thanks.")
            # update new information of the external database of the library from program
            download_inventory(inventory)
        else:
            print("")
            print("[CONSOLE] - Not adding more books, thanks.")
    # if ISBN does not exist in our library then add the book
    else:
        # introduce user inputs for title, author and amount. And introducing quality input checks
        print("")
        title = input("[CONSOLE] - Please enter the title of the book you want to add to the library: ")
        # flow control to avoid user not inserting any title value or inserting a title value with more than 45
        # characters (this is a personal requirement)
        while len(title) == 0 or len(title.strip()) >= 45:
            print("")
            title = input("[CONSOLE][ERROR] - Remember the title cannot be an empty value or needs to be shorter, "
                          "please try again: ")
        print("")
        author = input("Please enter the author of the book you want to add to the library: ")
        # flow control to avoid user not inserting any title value or inserting a title value with more than 20
        # characters (this is a personal requirement)
        while len(author) == 0 or len(author.strip()) >= 20:
            print("")
            author = input("[CONSOLE][ERROR] - Remember the author cannot be an empty value or needs to be shorter, "
                           "please try again: ")
        print("")
        amount = input("[CONSOLE] - Please enter the amount of purchased books you want to add to the library: ")
        # flow control to avoid user adding more than 9 copies at a time (this is a personal requirement) or not
        # inserting a numeric value
        while int(amount) >= 10 or not amount.isdigit():
            print("")
            amount = input("[CONSOLE][ERROR] - Remember the amount has to be numerical and we cannot add more than "
                           "0 copies at a time, please try again:  ")
        # upadting dictionary with new values
        inventory[isbn] = [title.strip(), author.strip(), amount, amount]
        print("")
        print("[CONSOLE] - Book added with " + amount + " new copies, thanks.")
        # update new information of the external database of the library from program
        download_inventory(inventory)

# string cleaning function used in search function (below)
def cleaner(input):
    # remove the following characters from user search keywords
    for i in [",", ".", ";", ":", "!", "?","'s","s'"]:
        input = input.replace(i,"")
    # building a list with all the words (lower case) from the search sentence of the user
    input = (input.lower()).split(" ")
    output = []
    # remove from input list the following words
    for i in input:
        if i not in ["a","of","the","and"]:
            output.append(i)
    output = " ".join(output)
    return output

# function to search for a book in the library from its complete title or words composing the title
# creates a ranked result list ruled by coincidences found between search key words and title key words
# Asks the user to specify for the title one the search has been narrowed down and displays ISBN code for the book
def search():
    # uploading inventory information from the external database
    inventory = upload_inventory()
    print("")
    key_word = input("[CONSOLE] - Please introduce the name of the book (or similar) that you are looking for: ")
    titles = []
    titles_real = []
    # calling cleaner function to extract from user's search keywords the most important words
    key_word = cleaner(key_word)
    search_keywords = key_word.split(" ")
    # designing an intelligent search feature based on a score ranking system defined by the amount of words from the
    # user search keywords contained in the book titles
    for key in inventory:
        titles.append(cleaner(inventory[key][0]))
        titles_real.append(inventory[key][0])
    scores = []
    # every word coinciding between the two lists is a point for the book title
    for i in titles:
        count = 0
        title_keywoards = i.split(" ")
        for j in title_keywoards:
            for n in search_keywords:
                if j == n:
                    count += 1
        scores.append(count)
    shell_scores = []
    # unifying results for scores and titles using a list containing both values in another list
    for i in range(len(titles_real)):
        shell_scores.append([scores[i],titles_real[i]])
    # ordering titles according to its punctuation
    shell_scores.sort(reverse = True)
    # if no coincidences alert the user
    if sum(scores) == 0:
        print("")
        print("[CONSOLE][ALERT] - The book you are looking for does not exist or it is not in this library")
        # return false for checkout function indicator (see library_logic.py)
        return False
    # if coincidences display the books with at least 1 point in the ranking system (this part of the logic should be
    # improved if the database was bigger)
    else:
        # Printing search results and adding a reference number so the user can choose the book she or he was looking
        # for if the search results displays more than one title
        print("")
        print("[CONSOLE] - The books found from your search keywords were:")
        print("")
        print((3 + len("REFERENCE")) * "#"  + (4 + 49) * "#")
        print("| REFERENCE |" + " " * 22 + "TITLE" + " " * 24 + "|")
        print((3 + len("REFERENCE")) * "#" + (4 + 49) * "#")
        titles_post_search = []
        postitions_list = []
        count = 0
        for i in shell_scores:
            if i[0] != 0:
                count += 1
                postitions_list.append(str(count))
                titles_post_search.append(i[1])
                print("| " + str(count) + " " * (10-len(str(count))) +  "| " + i[1] + " " * (50-len(str(i[1]))) + "|")
        print((3 + len("REFERENCE")) * "#" + (4 + 49) * "#")
        print("")
        # user selects the book that she or he wanted to find
        select_index = input("[CONSOLE] - Please select the reference number of the"
                             " book you are looking for or N to terminate the search: ")
        # terminating search if user does not want to continuate
        if select_index.lower() == "n":
            print("")
            print("[CONSOLE] - Search terminated")
        # if user wants to continue the function will print the details of the book + the ISBN number
        else:
            # flow control to avoid user inserting a number that is not referenced in the search results
            while select_index not in postitions_list:
                print("")
                select_index = input("[CONSOLE][ERROR] - Reference number selected invalid, please try again: ")
            for key in inventory:
                count += 1
                if inventory[key][0] == titles_post_search[int(select_index) - 1]:
                    isbn = key
            print("")
            print("[CONSOLE] - Details: ")
            print("")
            # printing inventory status in a nice way
            print((3 + 13) * "#" + (3 + 49) * "#" +
                  (3 + 19) * "#" + (4 + 6) * "#")
            print("|" + " " * (int(round((3 + 13) / 2, 0)) - int(round(4 / 2, 0)) - 1) + "ISBN" +
                  ((3 + 13) - (int(round((3 + 13) / 2, 0)) + int(round(4 / 2, 0)))) * " " +
                  "|" + " " * (int(round((3 + 49) / 2, 0)) - int(round(5 / 2, 0)) - 1) + "TITLE" +
                  ((3 + 49) - (
                          int(round((3 + 49) / 2, 0)) + int(round(5 / 2, 0))) - 1) * " " +
                  "|" + " " * (int(round((3 + 19) / 2, 0)) - int(round(6 / 2, 0)) - 1) + "AUTHOR" +
                  ((3 + 19) - (
                          int(round((3 + 19) / 2, 0)) + int(round(6 / 2, 0)))) * " " +
                  "| AMOUNT |")
            print((3 + 13) * "#" + (3 + 49) * "#" +
                  (3 + 19) * "#" + (4 + 6) * "#")
            print(("| " + isbn + " " * ((3 + 13) - len(isbn) - 2)) +
                  ("| " + inventory[isbn][0] + " " * ((3 + 49) - len(inventory[isbn][0]) - 2)) +
                  ("| " + inventory[isbn][1] + " " * ((3 + 19) - len(inventory[isbn][1]) - 2)) +
                  ("| " + inventory[isbn][2] + "/" + inventory[isbn][3] + " " *
                   ((3 + 6) - (len(inventory[isbn][2]) + len(inventory[isbn][2]) +1) - 2)) + "|")
            print((3 + 13) * "#" + (3 + 49) * "#" +
                  (3 + 19) * "#" + (4 + 6) * "#")
            print("")
            print("[CONSOLE] - ISBN: " + isbn)
            # returning isbn for checkout function
            return isbn

# function to borrow a book title from the library, function input is the book's ISBN code
# uses search function first and after book has been found asks the user if she or he wants to borrow the book
# if the user wants checks whether the user has been previously borrowed by the user or not. If not, book is borrowed
# and program updates user log and inventory information both internally and externally
def checkout(isbn):
    print("")
    check_out_ind = input("[CONSOLE] - Do you want to check out this book? (Y/N)")
    # flow control to guide user and avoid computation errors
    while check_out_ind.lower() not in ["y", "n"]:
        print("")
        check_out_ind = input("[CONSOLE][ERROR] - I do not understand your command please use Y for yes or N for "
                             "no, please try again: ")
    # if "Y" then the function looks for the book title by using the ISBN code
    if check_out_ind.lower() == "y":
        # uploading inventory information from the external database
        inventory = upload_inventory()
        # alert the user if there are no more copies available for that title
        if int(inventory[isbn][2]) == 0:
            print("")
            print("[CONSOLE][ALERT] - There are no more copies available for this book, apologies")
        else:
            # uploading user log information from the external database
            log_file = upload_log()
            # if title has already been borrowed by user throw alert message (this is a personal requirement)
            if inventory[isbn][0] in log_file:
                print("")
                print( "[CONSOLE][ALERT] - "
                       "You have already checked out this book in the past, you cannot check it out again.")
            # if not, update log and inventory information + the external databases
            else:
                print("")
                print("[CONSOLE] - Checking out... Thanks")
                inventory[isbn][2] = str(int(inventory[isbn][2]) - 1)
                download_inventory(inventory)
                log_file.append(inventory[isbn][0])
                download_log_file(log_file)
    # stop process if user does not want to proceed
    else:
        print("")
        print("[CONSOLE] - Terminating search")

# function to return a book borrowed by the user
# asks user to choose which book to return among all the books that have been checked out by the user
# after selection the program updates the internal and external information of the user and the inventory
def return_book():
    # uploading user log information from the external database
    log_file = upload_log()
    # if no books borrowed stop
    if len(log_file) == 0:
        print("")
        print("[CONSOLE][ALERT] - No books checked out, no books to return")
    # if there are books borrowed, display the whole list and ask user to select which one is for return
    else:
        # uploading inventory information from the external database
        inventory = upload_inventory()
        print("")
        print((3 + len("REFERENCE")) * "#" + (4 + 49) * "#")
        print("| REFERENCE |" + " " * 22 + "TITLE" + " " * 24 + "|")
        print((3 + len("REFERENCE")) * "#" + (4 + 49) * "#")
        postitions_list = []
        count = 0
        # prints list of books borrwed by the user, with a reference field
        for i in log_file:
            count += 1
            postitions_list.append(str(count))
            print("| " + str(count) + " " * (10 - len(str(count))) + "| " + i + " " * (50 - len(str(i))) + "|")
        print((3 + len("REFERENCE")) * "#" + (4 + 49) * "#")
        print("")
        select_index = input("[CONSOLE] - Please select the reference number of the"
                             " book you want to return or N to terminate this process: ")
        # user stops process
        if select_index.lower() == "n":
            print("")
            print("[CONSOLE] - Return process terminated")
            return True
        # if user does not stop process book is returned
        else:
            # flow control to ensure user selects a reference field stated in the result options
            while select_index not in postitions_list:
                print("")
                select_index = input("[CONSOLE] - Reference number selected invalid, please try again: ")
            # find the isbn code of the book we are returning to update inventory and user log file information
            for key in inventory:
                count += 1
                if inventory[key][0] == log_file[int(select_index) - 1]:
                    isbn = key
            # updating internal and external inventory information
            inventory[isbn][2] = str(int(inventory[isbn][2]) + 1)
            download_inventory(inventory)
            # updating internal and external user log information
            log_file.remove(log_file[int(select_index) - 1])
            download_log_file(log_file)
            print("")
            print("[CONSOLE] - Book returned")