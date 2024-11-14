def get_todos(filepath):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(filepath, todos_to_write):
    with open(filepath, 'w') as file:
        file.writelines(todos_to_write)


while True:
    # Get user input and strip space characters from it
    user_action = input('To-Do list options, add, edit, complete, show, exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = get_todos('files/todos.txt')
        todos.append(todo)
        write_todos('files/todos.txt', todos)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1
            todos = get_todos('files/todos.txt')
            new_todo = input('Enter new to-do: ')
            todos[number] = new_todo + '\n'
            write_todos('files/todos.txt', todos)
        except ValueError:
            print('Your command is not valid. Enter the number of the to-do to edit')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos('files/todos.txt')
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos('files/todos.txt', todos)
            message = f'Todo {todo_to_remove} was removed from the list.'
            print(message)
        except IndexError:
            print('Your command is not valid. Enter the number of the to-do to complete')
            continue
    elif user_action.startswith('show'):
        todos = get_todos('files/todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f'{index + 1} - {item}')
    elif 'exit' in user_action:
        break
    else:
        print("Command was not valid.")
