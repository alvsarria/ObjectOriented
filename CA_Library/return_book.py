from upload_functions import *
from download_functions import *

def return_book():
    log_file = upload_log()
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