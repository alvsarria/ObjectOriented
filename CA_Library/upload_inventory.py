def upload():
    library_inventory = {}
    try:
        file_obj = open("library_inventory.txt", "r")
    except FileNotFoundError:
        print("The file you are trying to read does not exist")
    else:
        for line in file_obj:
            row = (line.strip()).split(";;")
            library_inventory[row[0]] = (row[1], row[2], row[3])
        file_obj.close()
    return library_inventory