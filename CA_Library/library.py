from upload_inventory import upload
from download_inventory import download

inventory = upload()

for i in inventory:
    print(inventory[i])
