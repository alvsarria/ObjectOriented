from download_functions import download_inventory

# function to add book to the library or icnrease the amount of copies of an existing book
def add(inventory):
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
