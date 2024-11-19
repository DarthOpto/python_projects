def get_todos(filepath='files/todos.txt'):
    """
    Read a text file and return the list of to-do items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_to_write, filepath='files/todos.txt'):
    """
    Writes the to-do  items list to the text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_to_write)