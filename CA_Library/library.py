from upload_inventory import upload
from download_inventory import download
from print_details import status
from add_book import add
from search_book import search

inventory = upload()

add(inventory)

status(inventory)

download(inventory)

search(inventory)


