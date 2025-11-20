def get_todos(filepath):
    """Get a TextFile and return the Todo-List of that item"""
    with open(filepath,'r')as file :
        todos = file.readlines()
    return todos
print(help(get_todos))
def add_todos(filepath,todos):
    """Write the Todo-List in the text file"""
    with open(filepath,'w')as file:
        file.writelines(todos)
def show_todos(todos):
    for index,todo in enumerate(todos):
        print(f"{index+1}-> {todo.strip("\n")}")
