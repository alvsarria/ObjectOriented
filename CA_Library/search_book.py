from upload_functions import upload_inventory

def cleaner(input):
    for i in [",", ".", ";", ":", "!", "?","'s","s'"]:
        input = input.replace(i,"")
    input = (input.lower()).split(" ")
    output = []
    for i in input:
        if i not in ["a","of","the","and"]:
            output.append(i)
    output = " ".join(output)
    return output


def search():
    inventory = upload_inventory()
    print("")
    key_word = input("[CONSOLE] - Please introduce the name of the book (or similar) that you are looking for: ")
    titles = []
    titles_real = []
    key_word = cleaner(key_word)
    search_keywords = key_word.split(" ")
    # designing an intelligent search future based on a score ranking system driven by word by word found on title
    for key in inventory:
        titles.append(cleaner(inventory[key][0]))
        titles_real.append(inventory[key][0])
    scores = []
    for i in titles:
        count = 0
        title_keywoards = i.split(" ")
        for j in title_keywoards:
            for n in search_keywords:
                if j == n:
                    count += 1
        scores.append(count)
    shell_scores = []
    for i in range(len(titles_real)):
        shell_scores.append([scores[i],titles_real[i]])
    shell_scores.sort(reverse = True)
    if sum(scores) == 0:
        print("")
        print("[CONSOLE] - The book you are looking for does not exist or it is not in this library")
        return False
    else:
        # Printing initial search
        print("")
        print("[CONSOLE] - The books found from your search keywords were:")
        print("")
        print((3 + len("REFERENCE")) * "#"  + (4 + 49) * "#")
        print("| REFERENCE |" + " " * 22 + "TITLE" + " " * 24 + "|")
        print((3 + len("REFERENCE")) * "#" + (4 + 49) * "#")
        titles_post_search = []
        postitions_list = []
        count = 0
        for i in shell_scores:
            if i[0] != 0:
                count += 1
                postitions_list.append(count)
                titles_post_search.append(i[1])
                print("| " + str(count) + " " * (10-len(str(count))) +  "| " + i[1] + " " * (50-len(str(i[1]))) + "|")
        print((3 + len("REFERENCE")) * "#" + (4 + 49) * "#")
        print("")
        select_index = input("[CONSOLE] - Please select the reference number of the"
                             " book you are looking for or N to terminate the search: ")
        print("")
        if select_index.lower() == "n":
            print("[CONSOLE] - Search terminated")
            return  True
        else:
            while len(select_index) == 0 or not select_index.isdigit() or int(select_index) not in postitions_list:
                print("")
                select_index = input("[CONSOLE] - Reference number selected invalid, please try again: ")
            for key in inventory:
                count += 1
                if inventory[key][0] == titles_post_search[int(select_index) - 1]:
                    isbn = key
            print("[CONSOLE] - Details: ")
            print("")
            # printing inventory status in a nice way
            print((3 + 13) * "#" + (3 + 49) * "#" +
                  (3 + 19) * "#" + (4 + 6) * "#")
            print("|" + " " * (int(round((3 + 13) / 2, 0)) - int(round(4 / 2, 0)) - 1) + "ISBN" +
                  ((3 + 13) - (int(round((3 + 13) / 2, 0)) + int(round(4 / 2, 0)))) * " " +
                  "|" + " " * (int(round((3 + 49) / 2, 0)) - int(round(5 / 2, 0)) - 1) + "TITLE" +
                  ((3 + 49) - (
                          int(round((3 + 49) / 2, 0)) + int(round(5 / 2, 0))) - 1) * " " +
                  "|" + " " * (int(round((3 + 19) / 2, 0)) - int(round(6 / 2, 0)) - 1) + "AUTHOR" +
                  ((3 + 19) - (
                          int(round((3 + 19) / 2, 0)) + int(round(6 / 2, 0)))) * " " +
                  "| AMOUNT |")
            print((3 + 13) * "#" + (3 + 49) * "#" +
                  (3 + 19) * "#" + (4 + 6) * "#")
            print(("| " + isbn + " " * ((3 + 13) - len(isbn) - 2)) +
                  ("| " + inventory[isbn][0] + " " * ((3 + 49) - len(inventory[isbn][0]) - 2)) +
                  ("| " + inventory[isbn][1] + " " * ((3 + 19) - len(inventory[isbn][1]) - 2)) +
                  ("| " + inventory[isbn][2] + "/" + inventory[isbn][3] + " " *
                   ((3 + 6) - (len(inventory[isbn][2]) + len(inventory[isbn][2]) +1) - 2)) + "|")
            print((3 + 13) * "#" + (3 + 49) * "#" +
                  (3 + 19) * "#" + (4 + 6) * "#")
            print("")
            print("[CONSOLE] - ISBN: " + isbn)
            return isbn
