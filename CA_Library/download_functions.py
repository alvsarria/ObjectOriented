# function to bulk the inventory into our .txt database
def download_inventory(inventory):
    file_obj = open("DBs/library_inventory.txt", "w")
    for i in inventory:
        element = [i, inventory[i][0], inventory[i][1], inventory[i][2], inventory[i][3]]
        file_obj.write(";;".join(element) + "\n")
    file_obj.close()

def download_log_file(user_log_file):
    file_obj = open("DBs/checkout_books_log_file.txt", "w")
    for i in user_log_file:
        element = i.strip()
        file_obj.write(element + "\n")
    file_obj.close()