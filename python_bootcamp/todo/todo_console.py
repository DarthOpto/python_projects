while True:
    # Get user input and strip space characters from it
    user_action = input('To-Do list options, add, edit, complete, show, exit: ')
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:] + '\n'
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo)
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number -= 1
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input('Enter new to-do: ')
        todos[number] = new_todo + '\n'
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
        number = int(user_action[9:])
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
        message = f'Todo {todo_to_remove} was removed from the list.'
        print(message)
    elif 'show' in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f'{index + 1} - {item}')
    elif 'exit' in user_action:
        break
    else:
        print("Command was not valid.")
