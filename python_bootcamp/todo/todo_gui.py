from functions import get_todos, write_todos
import FreeSimpleGUI as fsg

label = fsg.Text('Type in a to-do')
input_box = fsg.InputText(tooltip='Enter to-do', key='todo')
add_button = fsg.Button('Add')

window = fsg.Window('My To-Do App',
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            write_todos(todos)
        case fsg.WIN_CLOSED:
            break
window.close()


