import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",  # Creates list from text file after reading
					  enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
				   layout=[[label], [input_box, add_button], [list_box, edit_button]],
				   font=('Helvetica', "20"))

while True:
	event, values_dict = window.read()
	print(1, event)
	print(2, values_dict)
	print(3, values_dict['todos'])
	match event:
		case "Add":
			todos = functions.get_todos()  # Creates list from text file after reading
			new_todo = values_dict['todo'] + '\n'
			todos.append(new_todo)
			functions.write_todos(todos)
			window['todos'].update(values=todos)  # Everything on screen is in Windows dict/ look at keys
			window['todo'].update(value="")

		case "Edit":
			todo_to_edit = values_dict['todos'][0]  # Different dictionary
			new_todo = values_dict['todo']


			todos = functions.get_todos()
			index = todos.index((todo_to_edit)) # Index of line clicked
			todos[index] = new_todo
			functions.write_todos(todos)
			window['todos'].update(values=todos)


		case 'todos':
			window['todo'].update(value=values_dict['todos'][0])


		case sg.WIN_CLOSED:
			break

window.close()
