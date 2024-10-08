# add function
App_list = ["To-Do List Application",
        "1. Add Task",
        "2. Remove Task",
        "3. View Tasks",
        "4. Exit"]

def app_function(num):
    agenda_list = [] # list of tasks
    if num == 1:
        # add
        print("add agenda")
    elif num == 2:
        # remove
        print("remove agenda")
    else:
        #view
        print("view agenda")

while True :
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
