while True:
    user_action = input('To-Do list options, add, edit, complete, show, exit: ')
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('What task would you like to add? ') + "\n"
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'edit':
            number = int(input('Enter the number of the todo to edit: '))
            number -= 1
            new_todo = input('Enter new to-do: ')
            todos[number] = new_todo
        case 'complete':
            number = int(input('Enter the number of the todo to complete: '))
            todos.pop(number - 1)
        case 'show':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                item = item.title()
                print(f'{index + 1} - {item}')
        case 'exit':
            break
