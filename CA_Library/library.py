from status_functions import *
from add_book import add
from search_book import search
from checkout_book import checkout
from return_book import return_book

status_inventory()
status_log_file()

isbn = search()
if str(isbn).isdigit():
    checkout(isbn)

status_inventory()
status_log_file()

return_book()

status_inventory()
status_log_file()
