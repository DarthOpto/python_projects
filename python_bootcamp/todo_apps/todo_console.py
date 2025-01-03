import datetime

from functions import get_todos, write_todos
import time

today = time.strftime("%A %d-%m-%Y %H:%M:%S")
while True:
    print(f'It is {today}')
    # Get user input and strip space characters from it
    user_action = input('To-Do list options, add, edit, complete, show, exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1
            todos = get_todos()
            new_todo = input('Enter new to-do: ')
            todos[number] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print('Your command is not valid. Enter the number of the to-do to edit')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)
            message = f'Todo {todo_to_remove} was removed from the list.'
            print(message)
        except IndexError:
            print('Your command is not valid. Enter the number of the to-do to complete')
            continue
    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f'{index + 1} - {item}')
    elif 'exit' in user_action:
        break
    else:
        print("Command was not valid.")
