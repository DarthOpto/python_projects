from functions import get_todos, write_todos
import FreeSimpleGUI as fsg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

fsg.theme("DarkAmber")
# add to-do elements
clock = fsg.Text('', key='clock')
label = fsg.Text('Type in a to-do')
input_box = fsg.InputText(tooltip='Enter to-do', key='todo')
add_button = fsg.Button(image_source='add.png',
                        mouseover_colors='LightBlue2', tooltip='Add To-Do',
                        key='Add')

# edit to-do elements
list_todos = fsg.Listbox(values=get_todos(),
                         key='todos',
                         enable_events=True,
                         size=(45, 10))
edit_button = fsg.Button('Edit')

# Complete and exit buttons
complete_button = fsg.Button(size=20, image_source='complete.png', tooltip='Complete To-Do', key='Complete')
exit_button = fsg.Button("Exit")

window_layout = [[clock],
                 [label], [input_box, add_button],
                 [list_todos, edit_button, complete_button],
                 [exit_button]]

window = fsg.Window('My To-Do App',
                    layout=window_layout,
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%A %d-%m-%Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item before editing", font=("Helvetica", 20))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                fsg.popup("Please select an item before editing", font=("Helvetica", 20))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case fsg.WIN_CLOSED:
            break
window.close()
