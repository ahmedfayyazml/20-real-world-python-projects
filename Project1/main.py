while True:
    user_input = input("Select Your Action 'add','edit','completed','show'")
    match user_input:
        case 'add':
            todo = input("Enter your todo : ")+"\n"
            file = open("todos.txt",'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open("todos.txt",'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open("todos.txt",'r')
            todos = file.readlines()
            for index,todo in enumerate(todos):
                print(f"{index+1}-> {todo}")
            file.close()
        case 'edit':
            file = open("todos.txt",'r')
            todos = file.readlines()
            for index,todo in enumerate(todos):
                print(f"{index+1}-> {todo}")
            file.close()
        case 'completed':
            file = open("todos.txt",'r')
            todos = file.readlines()
            for index,todo in enumerate(todos):
                print(f"{index+1}-> {todo}")
            file.close()
        case 'exit':
            break
print("GoodBye")