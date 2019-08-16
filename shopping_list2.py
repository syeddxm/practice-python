import os


def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')


def show_help():
#print instructions
    clear_screen()
    print("What should we pick up at the store")
    print("""
Type 'DONE' to stop adding items
Type 'HELP' for this help.
Type 'SHOW' to see your current list.
Type 'REMOVE' to remove item from the list
""")

def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

def show_list():
    clear_screen()
    print("Here's your list")

    index = 1
    for items in shopping_list:
        print("{}. {}".format(index,items))
        index += 1

    print('-'*10)

def add_to_list(new_item):
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}\n"
                        "Press Enter to add to the end of the lsit \n"
                        "> ".format(item))
    else:
        position=0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)
    show_list()

shopping_list = []
print("what do you have to buy? ")
while True:
    item = str(input('> '))

    if item.upper() == "DONE" or item.upper()=="QUIT":
        break
    elif item.upper()=="HELP":
        show_help()
        continue
    elif item.upper()=="SHOW":
        show_list()
        continue
    elif item.upper()=="REMOVE":
        remove_from_list()
    else:
        add_to_list(item)
