from print_details import status
from add_book import add
from search_book import search
from checkout_book import checkout

isbn = search()
if str(isbn).isdigit():
    checkout(isbn)

