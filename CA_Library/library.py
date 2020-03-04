from upload_inventory import upload
from download_inventory import download
from print_details import status
from add_book import add

inventory = upload()

status(inventory)

inventory = add(inventory)


