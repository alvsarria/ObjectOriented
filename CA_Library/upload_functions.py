# function to upload the inventory information stored in our external .txt database
def upload_inventory():
    library_inventory = {}
    try:
        file_obj = open("DBs/library_inventory.txt", "r")
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
        file_obj = open("DBs/checkout_books_log_file.txt", "r")
    except FileNotFoundError:
        print("The file you are trying to read does not exist")
    else:
        for line in file_obj:
            row = line.strip()
            user_log_file.append(row)
        file_obj.close()
    return user_log_file