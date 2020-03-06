from upload_functions import *
from download_functions import *

def checkout(isbn):
    print("")
    check_out_ind = input("Do you want to check out this book? (Y/N)")
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

