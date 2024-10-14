from datetime import datetime

# add function
App_list = ["To-Do List Application",
        "1. Add Task",
        "2. Remove Task",
        "3. View Tasks",
        "4. Exit"]

agenda_list = [] # list of tasks, initialize an empty list

def app_function(num):
    if num == 1:
        # add def
        add_task()
    elif num == 2:
        # remove
        remove_task()

    # view
    elif num == 3:
        view_tasks()


def add_task():
    # adding task
    adding = input("Enter the task: ")

    # adding priority
    while True:
        priority = input("Enter the priority (high, medium, low): ")
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("you should choose one of them (high, medium, low).")

    # adding deadline
    while True:
        try:
            deadline = input("Enter the deadline (YYYY-MM-DD): ")
            # date() : only pick date
            date_object = datetime.strptime(deadline, "%Y-%m-%d").date()
            break
        except ValueError:
            print("You should follow this format using number(YYYY-MM-DD).")

    agenda_list.append({
        'task': adding,
        'priority': priority,
        'deadline': str(date_object)
    })

    print(f"\'{adding}\' with priority \'{priority}\' and deadline \'{date_object}\' has been added to the list.")
    # print(agenda_list) for agenda_list what is inside


def remove_task():

    remove_task = input("Enter the task to remove: ")
    for key in agenda_list:
        if  remove_task == key["task"]:
            agenda_list.remove(key)
            print(f"\'{remove_task}\' has been remove from the list")
        else:
            print("Task no founded")


def view_tasks():
    # you can write the code in here
    print(f"{agenda_list}")
    # print("view")
    # if agenda_list:
    #     print("tasks in the to do list")
    #     for idx, agenda_list in enumerate(agenda_list, start=1):
    #         print(f"{idx}. {agenda_list}")
    # else:
    #     print("to do list is empty")

# main
while True :
    # show the application list
    for i in App_list:
        print(i)
    try :
        num = int(input("Enter your choice: "))
    except ValueError:
        print("you put the wrong number. you need to put the number(1 to 4).")
        continue

    if num == 4:
        print("Exiting the application. Goodbye!")
        break
    elif num > 4 or num < 1:
        print("you put the wrong number. you need to put the number(1 to 4).")
    else:
        app_function(num)

