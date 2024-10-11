from datetime import datetime

# add function
App_list = ["To-Do List Application",
        "1. Add Task",
        "2. Remove Task",
        "3. View Tasks",
        "4. Exit"]

# list of tasks, initialize an empty list
agenda_list = []
#deadline = ""


def app_function(num):

    if num == 1:
        # add def
        adding()

    elif num == 2:
        # remove
        print("remove agenda")
    else:
        #view
        print("view agenda")

def adding():
    # adding task
    add_task = input("Enter the task: ")
    # adding priority
    while True:
        priority = input("Enter the priority (high, medium, low): ")
        if priority == 'high' or priority == 'medium' or priority == 'low':
            break
        else:
            print("you should choose one of them (high, medium, low).")
    # adding deadline
    while True:
        try:
            deadline = input("Enter the deadline (YYYY-MM-DD): ")
            # date() : only pick date
            date_object = datetime.strptime(deadline, "%Y-%m-%d").date()
            date_object = str(date_object).split("-")
            break
        except ValueError:
            print("You should follow this format using number(YYYY-MM-DD).")

    agenda_list.append([add_task, priority, date_object])
    print(f"\'{add_task}\' with priority \'{priority}\' and deadline \'{date_object[0]}-{date_object[1]}-{date_object[2]}\' has been added to the list.")
    print(agenda_list)



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

