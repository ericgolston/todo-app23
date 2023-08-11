import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
				   layout=[[label], [input_box, add_button]],
				   font=('Helvetica', "20"))

while True:
	event, values_dict = window.read()
	print(event)
	print(values_dict)
	match event:
		case "Add":
			todos = functions.get_todos()  # Creates list from text file after reading
			new_todo = values_dict['todo'] + '\n'
			todos.append(new_todo)
			functions.write_todos(todos)

		case sg.WIN_CLOSED:
			break



window.close()

