def download(inventory):
    file_obj = open("library_inventory.txt", "w")
    for i in inventory:
        element = []
        element.append(i)
        element.append(inventory[i][0])
        element.append(inventory[i][1])
        element.append(inventory[i][2])
        file_obj.write(";;".join(element) + "\n")
    file_obj.close()