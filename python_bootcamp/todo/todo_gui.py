from functions import get_todos, write_todos
import FreeSimpleGUI as fsg

# add to-do elements
label = fsg.Text('Type in a to-do')
input_box = fsg.InputText(tooltip='Enter to-do', key='todo')
add_button = fsg.Button('Add')

# edit to-do elements
list_todos = fsg.Listbox(values=get_todos(),
                         key='todos',
                         enable_events=True,
                         size=[45, 10])
edit_button = fsg.Button('Edit')

# Complete and exit buttons
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")

window_layout = [[label], [input_box, add_button],
                 [list_todos, edit_button, complete_button],
                 [exit_button]]

window = fsg.Window('My To-Do App',
                    layout=window_layout,
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window['todos'].update(values=todos)
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = get_todos()
            todos.remove(todo_to_complete)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case fsg.WIN_CLOSED:
            break
window.close()
