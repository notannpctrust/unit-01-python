with open("to_do_list.txt", "r") as file:
    to_do_list = file.readlines()


while True:#Using a True statement for my while loop to let me keep the loop go on forever
    print()
    print()
    print("This is your current to to-do list:")
    print()
    for x in to_do_list:
        print(x)
    print()
    print("These are your current options:")#Using many print() statements for organization
    print()
    print("Option1:add")
    print()
    print("Option2:delete")
    print()
    print("Option3:edit")
    print()
    print("Option4:Clear all")
    choice = input("What would you like to do?:")
    print()
    if choice == 'add':
        new_item = input("Enter a new todo list item:")
        to_do_list.append(new_item)#Using append will add the new_item to the bottom of the current list
    
    elif choice == 'delete':
        deleted_item = int(input("Enter your # deleted item(dont type the # just the number):"))#Using # for numbered deletes
        del to_do_list[deleted_item -1]#Using the same layout as the "add" choice for simplicity

    elif choice == "exit":
        with open("to_do_list.txt", "w") as file: 
