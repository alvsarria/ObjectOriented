def download(inventory):
    file_obj = open("library_inventory.txt", "w")
    for i in inventory:
        element = [i, inventory[i][0], inventory[i][1], inventory[i][2]]
        file_obj.write(";;".join(element) + "\n")
    file_obj.close()