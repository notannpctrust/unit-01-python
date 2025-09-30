to_do_list = []#Making a list named to do list

while True:#Using a True statement for my while loop seems to let me keep the loop go on forever
    print()
    print()
    print("This is your current to to-do list:")
    print()
    for x in to_do_list:
        print(x)
    print()
    print("These are your current options:")
    print()
    print("Option1:add")
    print()
    print("Option2:delete")
    print()
    print("Option3:edit")
    print()
    choice = input("What would you like to do?:")
    print()
    if choice == 'add':
        new_item = input("Enter a new todo list item:")
        to_do_list.append(new_item)
    
    elif choice == 'delete':
        
    
    

    