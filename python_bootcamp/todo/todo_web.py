import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    todo_to_add = st.session_state["new_todo"] + "\n"
    todos.append(todo_to_add)
    write_todos(todos)


st.title("My To-Do App")
st.write("This is my to-do app to increase my productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add To-Do",
              label_visibility="hidden",
              placeholder="Enter a new to-do here...",
              on_change=add_todo,
              key="new_todo")
