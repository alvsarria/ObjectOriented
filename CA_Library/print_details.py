def status(inventory):
    # Crearing empty lists to store lengths of strings
    isbn = []
    title = []
    author = []
    amount = []
    # Appending string lengths into lists
    for i in inventory:
        isbn.append(len(i))
        title.append(len(inventory[i][0]))
        author.append(len(inventory[i][1]))
        amount.append(len(inventory[i][2]))
    # Selecting maximum lengths per string contained in list
    isbn.sort(reverse = True)
    max_len_isbn = isbn[0]
    author.sort(reverse=True)
    max_len_author = author[0]
    title.sort(reverse=True)
    max_len_title = title[0]
    amount.sort(reverse=True)
    max_len_amount = amount[0]
    # In case filed name is longer than the longest string contained in the list, switch values
    if max_len_isbn < len("ISBN"):
        max_len_isbn_diff = len("ISBN")
    else:
        max_len_isbn_diff = max_len_isbn
    if max_len_title < len("TITLE"):
        max_len_title_diff = len("TITLE")
    else:
        max_len_title_diff = max_len_title
    if max_len_author < len("AUTHOR"):
        max_len_author_diff = len("AUTHOR")
    else:
        max_len_author_diff = max_len_author
    if max_len_amount < len("AMOUNT"):
        max_len_amount_diff = len("AMOUNT")
    else:
        max_len_amount_diff = max_len_amount
    # Printing inventory status in a nice way
    print((3 + max_len_isbn_diff) * "#" + (3 + max_len_title_diff) * "#" +
          (3 + max_len_author_diff) * "#" + (4 + max_len_amount_diff) * "#")
    print("|" + " " * (int(round((3 + max_len_isbn_diff) / 2,0)) - int(round(4 / 2,0)) - 1) + "ISBN" +
          ((3 + max_len_isbn_diff) - (int(round((3 + max_len_isbn_diff) / 2,0)) + int(round(4 / 2,0)))) * " " +
          "|" + " " * (int(round((3 + max_len_title_diff) / 2, 0)) - int(round(5 / 2, 0)) - 1) + "TITLE" +
          ((3 + max_len_title_diff) - (int(round((3 + max_len_title_diff) / 2,0)) + int(round(5 / 2,0))) - 1) * " " +
          "|" + " " * (int(round((3 + max_len_author_diff) / 2, 0)) - int(round(6 / 2, 0)) - 1) + "AUTHOR" +
          ((3 + max_len_author_diff) - (int(round((3 + max_len_author_diff) / 2, 0)) + int(round(6 / 2, 0)))) * " " +
          "| AMOUNT |")
    print((3 + max_len_isbn) * "#" + (3 + max_len_title) * "#" +
          (3 + max_len_author) * "#" + (4 + max_len_amount_diff) * "#")
    for i in inventory:
        print(("| " + i + " " * ((3 + max_len_isbn_diff)-len(i)-2)) +
              ("| " + inventory[i][0] + " " * ((3 + max_len_title_diff)-len(inventory[i][0])-2)) +
              ("| " + inventory[i][1] + " " * ((3 + max_len_author_diff)-len(inventory[i][1])-2)) +
              ("| " + inventory[i][2] + " " * ((3 + max_len_amount_diff)-len(inventory[i][2])-2)) + "|")
    print((3 + max_len_isbn) * "#" + (3 + max_len_title) * "#" +
          (3 + max_len_author) * "#" + (4 + max_len_amount_diff) * "#")