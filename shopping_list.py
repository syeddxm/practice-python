#Run the script, to start using it.
#Put new things into the list one thing at a time.
#Enter the word done, in all caps, to quit the program.
#And once I quit, I want the app to show me everything that's on my list.

shopping_list = []

while True:
    item = str(input("what do you have to buy? "))

    if item == "DONE":
        break

    shopping_list.append(item)

print("Here's your list")

for items in shopping_list:
    print(items)
