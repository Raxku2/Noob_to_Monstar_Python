todoData = [
    {
        'title':"Bazaar jabo",
        'status' : "blocked",
        'time': '22nd aug 10:00 am'
    },
    {
        'title':"FastAPI porbo",
        'status' : "completed",
        'time': '22nd aug 11:30 am'
    },
    {
        'title':"FastAPI porbo",
        'status' : "pending",
        'time': '22nd aug 11:30 am'
    },
]

# user todo dekhbe
def showTodo():
    for index,todo in enumerate(todoData):
        color = ''
        if todo.get('status').lower() == 'blocked':
            color = '\033[91m'
        if todo.get('status').lower() == 'pending':
            color = '\033[93m'
        if todo.get('status').lower() == 'progress':
            color = '\033[93m'
        if todo.get('status').lower() == 'completed':
            color = '\033[92m'

        print(f"{index+1}. {todo['title']:<20} | {todo['time']:<20} | {color}{todo['status']}\033[0m")

# user kaj likhbe
def  addTodo():
    title = ''
    while True:
        title = input("Enter Todo Title: ")
        if len(title) > 2:
            break
        elif title == 'Q':
            exit()
        else:
            print("\033[91mInvalid Input!!\033[0m")

    while True:
        time = input("Enter time: ")
        if len(time) > 2:
            todoData.append({
                'title':title,
                'time': time,
                'status' : "pending",
            })
            break
        elif time == 'Q':
            exit()
        else:
            print("\033[91mInvalid Input!!\033[0m")

# mark as done
def setStatus():
    dataRange = len(todoData)
    serialNo = 0
    while True:
        serialNo = input("Enter Sl No.: ")

        if serialNo.isnumeric() and int(serialNo) <= dataRange:
            serialNo = int(serialNo)-1
            break
        elif serialNo == 'Q':
            exit()
        else:
            print("\033[91mInvalid Input!!\033[0m")


    while True:
        status = input("('c' for Completed), ('b' for block), ('p' for Progressing), ('Q' for quit): ")

        if status.lower() == 'c':
            status = 'Completed'
            todoData[serialNo]['status'] = status
            break
        elif status.lower() == 'b':
            status = 'Blocked'
            todoData[serialNo]['status'] = status
            break
        elif status.lower() == 'p':
            status = 'Progress'
            todoData[serialNo]['status'] = status
            break
        elif status == 'Q':
            exit()
        else:
            print("\033[91mInvalid Input!!\033[0m")

# todo delete korbe
def clearTodo():
    cleardTodo = []
    for todo in todoData:
        # print(type(todo['status']))
        if todo['status'].lower() == 'completed' or todo['status'].lower() == 'blocked':
            print(f"Todo Deleted!! {todo['title']:<20} | {todo['time']:<20} | {todo['status']}\033[0m ")
        else:
            cleardTodo.append(todo)
    
    todoData[:] = cleardTodo

# showTodo()
# addTodo()
# setStatus()
# clearTodo()
# showTodo()



def main():
    while True:
        showTodo() #todo dekhiye debe

        app = input("Enter ('a' for add Todo), ('s' for Set Status), ('d' for Clear Todo), ('Q' for Quit): ")

        if app.lower() == 'a':
            addTodo()
            # pass
        elif app.lower() == 's':
            setStatus()
            # pass
        elif app.lower() == 'd':
            clearTodo()
            # pass
        elif app.lower() == 'Q':
            print("Quiting...")
            exit()
            # pass
        else:
            print("Error...")


main()