def download(inventory):
    file_obj = open("library_inventory.txt", "w")
    for i in inventory:
        isbn = []
        isbn.append(i)
        file_obj.write(";;".join(isbn+inventory[i]) + "\n")
    file_obj.close()