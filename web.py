import streamlit as st
import functions # Backend adds get todos and write todos

todos = functions.get_todos() # Has default argument; Creates list from todos.txt file

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")


st.checkbox("Buy the groceries")
st.checkbox("Throw away trash")

for todo in todos:
	st.checkbox(todo)


st.text_input(label="", placeholder="Add a new todo. . . ")