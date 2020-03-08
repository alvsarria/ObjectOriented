# function to upload the inventory information stored in our external .txt database
def upload_inventory():
    library_inventory = {}
    try:
        file_obj = open("dbs/library_inventory.txt", "r")
    except FileNotFoundError:
        print("The file you are trying to read does not exist")
    else:
        for line in file_obj:
            row = (line.strip()).split(";;")
            library_inventory[row[0]] = [row[1], row[2], row[3], row[4]]
        file_obj.close()
    return library_inventory

# function to upload the user logfile for checked out books, .txt external database
def upload_log():
    user_log_file = []
    try:
        file_obj = open("dbs/checkout_books_log_file.txt", "r")
    except FileNotFoundError:
        print("The file you are trying to read does not exist")
    else:
        for line in file_obj:
            row = line.strip()
            user_log_file.append(row)
        file_obj.close()
    return user_log_file

# function to bulk the inventory into our .txt database
def download_inventory(inventory):
    file_obj = open("dbs/library_inventory.txt", "w")
    for i in inventory:
        element = [i, inventory[i][0], inventory[i][1], inventory[i][2], inventory[i][3]]
        file_obj.write(";;".join(element) + "\n")
    file_obj.close()

def download_log_file(user_log_file):
    file_obj = open("dbs/checkout_books_log_file.txt", "w")
    for i in user_log_file:
        element = i.strip()
        file_obj.write(element + "\n")
    file_obj.close()

# function to print all the details of all the books in the library
def status_inventory():
    print("")
    print("[CONSOLE] - Please see all the details of the books in this library:")
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

def status_log_file():
    log_file = upload_log()
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

def add():
    inventory = upload_inventory()
    # introduce user inputs for isbn and introducing quality input checks
    print("")
    isbn = input("[CONSOLE] - Please enter the ISBN number of the book you want to add to the library: ")
    while len(isbn) != 13 or not isbn.isdigit():
        print("")
        isbn = input("[CONSOLE][ERROR] - Remember the isbn has to be numerical and it has to have 13 numbers, "
                     "please try again:  ")
    # add book to the library inventory only if ISBN is not included
    if isbn in inventory.keys():
        print("")
        print("[CONSOLE][ALERT] - This book is already in the library")
        # if ISBN is already in the library give the choice to increase the number of copies
        print("")
        add_book_ind = input("[CONSOLE] - Do you want to add more copies to the library? (Y/N)")
        while add_book_ind.lower() not in ["y","n"]:
            print("")
            add_book_ind = input( "[CONSOLE][ERROR] - I do not understand your command please use Y for yes or N for "
                                  "no, please try again: ")
        if add_book_ind.lower() == "y":
            print("")
            new_amount = input("[CONSOLE] - Please enter the amount of books you want to add: ")
            while int(new_amount) >= 10 or not new_amount.isdigit():
                print("")
                new_amount = input("[CONSOLE][ERROR] - Remember the amount has to be numerical and we cannot add more "
                                   "than 10 copies at a time, please try again:  ")
            inventory[isbn][2] = str(int(inventory[isbn][2]) + int(new_amount))
            inventory[isbn][3] = str(int(inventory[isbn][3]) + int(new_amount))
            print("")
            print("[CONSOLE] - " + new_amount + " copies added to the existing library, thanks.")
            download_inventory(inventory)
        else:
            print("")
            print("[CONSOLE] - Not adding more books, thanks.")
    else:
        # introduce user inputs for title, author and amount. And introducing quality input checks
        print("")
        title = input("[CONSOLE] - Please enter the title of the book you want to add to the library: ")
        while len(title) == 0 or len(title.strip()) >= 45:
            print("")
            title = input("[CONSOLE][ERROR] - Remember the title cannot be an empty value or needs to be shorter, "
                          "please try again: ")
        print("")
        author = input("Please enter the author of the book you want to add to the library: ")
        while len(author) == 0 or len(author.strip()) >= 20:
            print("")
            author = input("[CONSOLE][ERROR] - Remember the author cannot be an empty value or needs to be shorter, "
                           "please try again: ")
        print("")
        amount = input("[CONSOLE] - Please enter the amount of purchased books you want to add to the library: ")
        while int(amount) >= 10 or not amount.isdigit():
            print("")
            amount = input("[CONSOLE][ERROR] - Remember the amount has to be numerical and we cannot add more than "
                           "10 copies at a time, please try again:  ")
        inventory[isbn] = [title.strip(), author.strip(), amount, amount]
        print("")
        print("[CONSOLE] - Book added with " + amount + " new copies, thanks.")
        download_inventory(inventory)
    return inventory

def cleaner(input):
    for i in [",", ".", ";", ":", "!", "?","'s","s'"]:
        input = input.replace(i,"")
    input = (input.lower()).split(" ")
    output = []
    for i in input:
        if i not in ["a","of","the","and"]:
            output.append(i)
    output = " ".join(output)
    return output

def search():
    inventory = upload_inventory()
    print("")
    key_word = input("[CONSOLE] - Please introduce the name of the book (or similar) that you are looking for: ")
    titles = []
    titles_real = []
    key_word = cleaner(key_word)
    search_keywords = key_word.split(" ")
    # designing an intelligent search future based on a score ranking system driven by word by word found on title
    for key in inventory:
        titles.append(cleaner(inventory[key][0]))
        titles_real.append(inventory[key][0])
    scores = []
    for i in titles:
        count = 0
        title_keywoards = i.split(" ")
        for j in title_keywoards:
            for n in search_keywords:
                if j == n:
                    count += 1
        scores.append(count)
    shell_scores = []
    for i in range(len(titles_real)):
        shell_scores.append([scores[i],titles_real[i]])
    shell_scores.sort(reverse = True)
    if sum(scores) == 0:
        print("")
        print("[CONSOLE] - The book you are looking for does not exist or it is not in this library")
        return False
    else:
        # Printing initial search
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
                postitions_list.append(count)
                titles_post_search.append(i[1])
                print("| " + str(count) + " " * (10-len(str(count))) +  "| " + i[1] + " " * (50-len(str(i[1]))) + "|")
        print((3 + len("REFERENCE")) * "#" + (4 + 49) * "#")
        print("")
        select_index = input("[CONSOLE] - Please select the reference number of the"
                             " book you are looking for or N to terminate the search: ")
        if select_index.lower() == "n":
            print("")
            print("[CONSOLE] - Search terminated")
            isbn = ""
            return  isbn
        else:
            while len(select_index) == 0 or not select_index.isdigit() or int(select_index) not in postitions_list:
                print("")
                select_index = input("[CONSOLE] - Reference number selected invalid, please try again: ")
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
            return isbn

def checkout(isbn):
    print("")
    check_out_ind = input("[CONSOLE] - Do you want to check out this book? (Y/N)")
    while check_out_ind.lower() not in ["y", "n"]:
        print("")
        check_out_ind = input("[CONSOLE][ERROR] - I do not understand your command please use Y for yes or N for "
                             "no, please try again: ")
    if check_out_ind.lower() == "y":
        inventory = upload_inventory()
        if int(inventory[isbn][2]) == 0:
            print("")
            print("[CONSOLE][ALERT] - There are no more copies available for this book, apologies")
        else:
            log_file = upload_log()
            if inventory[isbn][0] in log_file:
                print("")
                print( "[CONSOLE][ALERT] - "
                       "You have already checked out this book in the past, you cannot check it out again.")
            else:
                print("")
                print("[CONSOLE] - Checking out... Thanks")
                inventory[isbn][2] = str(int(inventory[isbn][2]) - 1)
                download_inventory(inventory)
                log_file.append(inventory[isbn][0])
                download_log_file(log_file)
    else:
        print("")
        print("[CONSOLE] - Terminating search")

def return_book():
    log_file = upload_log()
    if len(log_file) == 0:
        print("")
        print("[CONSOLE][ALERT] - No books checked out, no books to return")
    else:
        inventory = upload_inventory()
        print("")
        print((3 + len("REFERENCE")) * "#" + (4 + 49) * "#")
        print("| REFERENCE |" + " " * 22 + "TITLE" + " " * 24 + "|")
        print((3 + len("REFERENCE")) * "#" + (4 + 49) * "#")
        postitions_list = []
        count = 0
        for i in log_file:
            count += 1
            postitions_list.append(count)
            print("| " + str(count) + " " * (10 - len(str(count))) + "| " + i + " " * (50 - len(str(i))) + "|")
        print((3 + len("REFERENCE")) * "#" + (4 + 49) * "#")
        print("")
        select_index = input("[CONSOLE] - Please select the reference number of the"
                             " book you want to return or N to terminate this process: ")
        if select_index.lower() == "n":
            print("")
            print("[CONSOLE] - Return process terminated")
            return True
        else:
            while len(select_index) == 0 or not select_index.isdigit() or int(select_index) not in postitions_list:
                print("")
                select_index = input("[CONSOLE] - Reference number selected invalid, please try again: ")
            for key in inventory:
                count += 1
                if inventory[key][0] == log_file[int(select_index) - 1]:
                    isbn = key
            inventory[isbn][2] = str(int(inventory[isbn][2]) + 1)
            download_inventory(inventory)
            log_file.remove(log_file[int(select_index) - 1])
            download_log_file(log_file)
            print("")
            print("[CONSOLE] - Book returned")