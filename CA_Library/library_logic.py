from library_functions import add,search,checkout,return_book,status_inventory,status_log_file

library_ind = True
print("")
print("[CONSOLE] - Logging in... Which operation would you like to proceed with?")
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
    while library_operation.lower() not in ["1", "2", "3", "4", "5", "6","7"]:
        print("")
        library_operation = input(
            "[CONSOLE][ERROR] - Cannot recognize this operation please try again: ")
    if library_operation == "1":
        status_inventory()
        print("")
        user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
        while user_ind.lower() not in ["y", "n"]:
            print("")
            user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
        if user_ind.lower() == "n":
            print("")
            print("[CONSOLE] - Logging out... thanks")
            library_ind = False
    if library_operation == "2":
        status_log_file()
        print("")
        user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
        while user_ind.lower() not in ["y", "n"]:
            print("")
            user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
        if user_ind.lower() == "n":
            print("")
            print("[CONSOLE] - Logging out... thanks")
            library_ind = False
    if library_operation == "3":
        search()
        print("")
        user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
        while user_ind.lower() not in ["y", "n"]:
            print("")
            user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
        if user_ind.lower() == "n":
            print("")
            print("[CONSOLE] - Logging out... thanks")
            library_ind = False
    if library_operation == "4":
        return_book()
        print("")
        user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
        while user_ind.lower() not in ["y", "n"]:
            print("")
            user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
        if user_ind.lower() == "n":
            print("")
            print("[CONSOLE] - Logging out... thanks")
            library_ind = False
    if library_operation == "5":
        isbn = search()
        if len(isbn) != 0:
            checkout(isbn)
        print("")
        user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
        while user_ind.lower() not in ["y", "n"]:
            print("")
            user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
        if user_ind.lower() == "n":
            print("")
            print("[CONSOLE] - Logging out... thanks")
            library_ind = False
    if library_operation == "6":
        add()
        print("")
        user_ind = input("[CONSOLE] - Would you like to perform another operation? (Y/N)")
        while user_ind.lower() not in ["y", "n"]:
            print("")
            user_ind = input("[CONSOLE][ERROR] - Please select 'Y' or 'N':")
        if user_ind.lower() == "n":
            print("")
            print("[CONSOLE] - Logging out... thanks")
            library_ind = False
    if library_operation == "7":
        print("")
        print("[CONSOLE] - Logging out... thanks")
        library_ind = False






