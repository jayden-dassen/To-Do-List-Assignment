def to_do_list():
    added_items = {}
    name = input("Hello, what is your name?")
    print("\nWelcome to your virtual to do list " + name.title() + "!")


    list_active = True
    while list_active:
        try:
            added = input("\nWhat would you like to add to your list?")
            response = input("\nWhen will you have it done?")
            added_items[added] = response
        except ValueError:
            print("You cannot add numbers onto this list.")
    
        repeat = input("Would you like to add anything else? (yes/no)")
        if repeat == 'no':
            list_active = False
        elif repeat == 'quit':
            list_active = False

    view_list = input("\nType (view) to view your list.")

    for added, response in added_items.items():
        print("I need to " + added.title() + " and I will have it done by " + response)

    remove_active = True
    while remove_active:
        remove_item = input("\nWould you like to remove anything from your list? (yes/no)")
        if remove_item == 'no':
            remove_active = False
    
        for added, response in added_items.items():
            print(added.title())
            
        which_item = input("Which item would you like to remove? (type exactly how it's shown in list.)")
        if which_item in added_items:
            removed_items = added_items
            del removed_items[which_item]
            for key, value in removed_items.items():
                print(key.title())
        elif which_item == 'quit':
            remove_active = False
        else:
            print("You cannot remove an item that isn't in your list.")
        
to_do_list()