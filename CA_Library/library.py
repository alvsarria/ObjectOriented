from upload_inventory import upload
from download_inventory import download
from print_details import status
from add_book import add

inventory = upload()

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


def search(key_word,inventory):
    titles = []
    titles_real = []
    key_word = cleaner(key_word)
    search_keywords = key_word.split(" ")
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
    count = 0
    for i in shell_scores:
        if i[0] != 0:
            count += 1
            print(str(count) + ' || ' + i[1])

search("harry potter",inventory)


