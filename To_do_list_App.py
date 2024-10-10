# add function
App_list = ["To-Do List Application",
        "1. Add Task",
        "2. Remove Task",
        "3. View Tasks",
        "4. Exit"]
agenda_list = [] # list of tasks, initialize an empty list
def app_function(num):

    if num == 1:
        # add
        add_task = input("Enter the task: ")
        agenda_list.append(add_task)
        print(f"\'{add_task}\' has been added to the list.")
        print()

    elif num == 2:
        # remove
        remove_task = input("Enter the task to remove: ")
        if remove_task in agenda_list:
            agenda_list.remove(remove_task)
            print(f"{remove_task} removed from agenda")
        else:
            print("Task no founded")

    elif num == 3:
        print(agenda_list)



        #view



while True :
    # show the application list
    for i in App_list:
        print(i)
    try :
        num = int(input("Enter your choice: "))
    except ValueError:
        print("you put the wrong number. you need to put the number(1 to 4).")

    if num == 4:
        print("Exiting the application. Goodbye!")
        break
    elif num > 4 or num < 1:
        print("you put the wrong number. you need to put the number(1 to 4).")
    else:
        app_function(num)
