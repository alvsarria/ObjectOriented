from upload_inventory import upload
from download_inventory import download
from print_details import status

inventory = upload()

download(inventory)

status(inventory)

