# Exercise 1: Write a Python program to create a list of contact details – using name, phone number and office number
# as in the example in the class. Write a function that takes a dictionary and an office number, and prints the names
# of all people in that office.

dicitonary_1 = {"Marc Virgili":[123456,"BCN"], "Adrián Cacho":[234561,"BCN"], "Florenci Andres":[345612,"AMS"],
              "Alvaro Sarria":[456123,"DUB"], "Ferran Conillera":[561234,"BCN"], "JuanM Nuez":[612345,"BCN"],
              "Alex Guasch":[654321,"BCN"], "Gonzalo Zamperoni":[435621,"BCN"], "JoseM Melen":[123654,"BCN"]}

def office_finder(dict,office):
    for key in dict:
        if dict[key][1] == office:
            print(key)

office_finder(dicitonary_1,"BCN")
print("--------")

# Exercise 2: Using the contact list from Exercise 1 write a python function that prints all people whose name begins
# with a specific character.

def print_names_dict(dict,first_character):
    for key in dict:
        if key[0].lower() == first_character.lower():
            print(key)

print_names_dict(dicitonary_1,"a")
print("--------")

# Exercise3: Write a Python program to create a list of items and corresponding quantities,
# e.g. inventory = {‘apple’:20, ‘banana’:30, ‘orange’:10}
# Write functions in Python to:
#   a)returns the total number of items (in the example above 60)
#   b)add stock, for example stock_up(inventory, ‘apple’,10) should result in the inventory being updated with 10 extra
#   apples
#   inventory will be {‘apple’:30, ‘banana’:30, ‘orange’:10}
#   You have to search through the inventory first to see if item is availablea.
#       a. if available – update the quantity plus the new amountb.
#       b.if not available - add it with the specified quantity

dicitonary_2 = {"apple":20, "banana":30, "orange":10, "pear":10, "grape":40, "melon":5, "watermelon":15, "lemon":25}

def total_quantity(dict):
    cnt = 0
    for key in dict:
        cnt += dict[key]
    return cnt

print(total_quantity(dicitonary_2))

def stock_up(dict, item, qty):
    if item in dicitonary_2:
        dicitonary_2[item] = dict[item] + qty
    else:
        dicitonary_2.update({item:qty})
    return dicitonary_2

print(stock_up(dicitonary_2,"mandarina", 15))
print(stock_up(dicitonary_2,"orange", 25))
print("--------")