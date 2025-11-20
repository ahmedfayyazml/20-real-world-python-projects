from modules.functions import get_todos,show_todos,add_todos    
while True:
    user_input = input("Select Your Action 'add','edit','completed','show' 'exit' : ").lower().strip()
    if(user_input.startswith('add')):
        try:
            todo = input("Enter your todo : ")+"\n"
            todos = get_todos("todos.txt")
            todos.append(todo)
            add_todos("todos.txt",todos)    
        except ValueError:
            print("Your command is invalid")        
    
    elif(user_input.startswith('show')):
        try:
            todos = get_todos("todos.txt")
            show_todos(todos)
        except ValueError:
            print("Your command is invalid")
    elif(user_input.startswith('edit')):
        try:
            todos = get_todos("todos.txt")
            show_todos(todos)
            number = int(input("Enter number of the todo"))
            number = number-1
            edited_todo = input("Enter new todo")
            todos[number] = edited_todo + "\n"
            add_todos("todos.txt",todos)
        except ValueError:
            print("Your command is invalid")
    elif(user_input.startswith('completed')):
        try:
            todos = get_todos("todos.txt")
            show_todos(todos)
            number = int(input("Write the number of todo that is completed"))
            todos.pop(number-1)
            add_todos("todos.txt",todos)
        except ValueError:
            print("Your command is invalid")        
    elif(user_input.startswith('exit')):
        break
    else:
        print(f"{user_input} dont exist")
print("GoodBye")