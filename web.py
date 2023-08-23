import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    functions.write_todos(todos)

st.set_page_config(layout="wide")

st.title("My Todo App")
st.subheader("this is my todo app")
st.write("This app is to increase your <b>productivity</b>" , unsafe_allow_html=True)

st.text_input(label='', placeholder='Life of Brian',
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        print(todos)
        todos.pop(index)
        print(todos)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


