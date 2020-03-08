# RUN FILE

# import library functions from external module
from library_functions import add,search,checkout,return_book,status_inventory,status_log_file

# declaring variable to finish while loop depending on user actions
library_ind = True
print("")
print("[CONSOLE] - Logging in... Which operation would you like to proceed with?")
# launching while loop to call library functions depending on user's preferences
while library_ind:
    print("")
    print(114 * "#")
    print("| Library Status | Account - Books Checked Out | Search Book | Return Book | Check Out Book | Add Book"
          " | Log Out |")
    print(114 * "#")
    print("| " + " " * 6 + "1" + " " * 7 + " | " + " " * 13 + "2" + " " * 13 + " | " +  " " * 5 + "3" + " " * 5 + " | "
          +  " " * 5 + "4" + " " * 5 + " | " + " " * 6 + "5" + " " * 7 + " | " + " " * 3 + "6" + " " * 4 + " | "
          + " " * 3 + "7" + " " * 3 + " |")
    print(114 * "#")
    print("")
    library_operation = input("[CONSOLE] - Please select the operation number you want to perform: ")
    # flow control to guide user and avoid computation errors
    while library_operation.lower() not in ["1", "2", "3", "4", "5", "6","7"]:
        print("")
        library_operation = input(
            "[CONSOLE][ERROR] - Cannot recognize this operation please try again: ")
    # if 1 --> print library inventory details (status_inventory)
    if library_operation == "1":
        status_inventory()
        print("")
        user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
        # flow control to guide user and avoid computation errors
        while user_ind.lower() not in ["y", "n"]:
            print("")
            user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
        if user_ind.lower() == "n":
            print("")
            print("[CONSOLE] - Logging out... thanks")
            library_ind = False
    # if 2 --> print user log file for checked out library titles (status_log_file)
    if library_operation == "2":
        status_log_file()
        print("")
        user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
        # flow control to guide user and avoid computation errors
        while user_ind.lower() not in ["y", "n"]:
            print("")
            user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
        if user_ind.lower() == "n":
            print("")
            print("[CONSOLE] - Logging out... thanks")
            library_ind = False
    # if 3 --> call search function (search)
    if library_operation == "3":
        search()
        print("")
        user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
        # flow control to guide user and avoid computation errors
        while user_ind.lower() not in ["y", "n"]:
            print("")
            user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
        if user_ind.lower() == "n":
            print("")
            print("[CONSOLE] - Logging out... thanks")
            library_ind = False
    # if 4 --> call return book function depending on the titles already checked out (return_book)
    if library_operation == "4":
        return_book()
        print("")
        user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
        # flow control to guide user and avoid computation errors
        while user_ind.lower() not in ["y", "n"]:
            print("")
            user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
        if user_ind.lower() == "n":
            print("")
            print("[CONSOLE] - Logging out... thanks")
            library_ind = False
    # if 5 --> call checkout function to extract a book from library via using search function (checkout)
    if library_operation == "5":
        isbn = search()
        # in case search function is terminated by the user
        if isbn == True:
            print("")
            user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
            # flow control to guide user and avoid computation errors
            while user_ind.lower() not in ["y", "n"]:
                print("")
                user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
            if user_ind.lower() == "n":
                print("")
                print("[CONSOLE] - Logging out... thanks")
                library_ind = False
        else:
            # flow control to avoid user looking for some title without coincidences in the dictionary
            while isbn == False:
                isbn = search()
            checkout(isbn)
            print("")
            user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
            # flow control to guide user and avoid computation errors
            while user_ind.lower() not in ["y", "n"]:
                print("")
                user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
            if user_ind.lower() == "n":
                print("")
                print("[CONSOLE] - Logging out... thanks")
                library_ind = False
    # if 6 --> call add function to add new books to the library or increase the copies of the existing ones (checkout)
    if library_operation == "6":
        add()
        print("")
        user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
        # flow control to guide user and avoid computation errors
        while user_ind.lower() not in ["y", "n"]:
            print("")
            user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
        if user_ind.lower() == "n":
            print("")
            print("[CONSOLE] - Logging out... thanks")
            library_ind = False
    # if 7 --> finishing
    if library_operation == "7":
        print("")
        print("[CONSOLE] - Logging out... thanks")
        library_ind = False






