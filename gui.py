import functions
import PySimpleGUI as sg
import time

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",  # Creates list from text file after reading
					  enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
				   layout=[[clock],
						   [label],
						   [input_box, add_button],
						   [list_box, edit_button, complete_button],
						   [exit_button]],
				   font=('Helvetica', "20"))

while True:
	event, values_dict = window.read(timeout=10)
	window['clock'].update(value=time.strftime("%b %d %Y %H:%M:%S"))
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
			try:
				todo_to_edit = values_dict['todos'][0]  # Different dictionary
				new_todo = values_dict['todo']

				todos = functions.get_todos()
				index = todos.index((todo_to_edit))  # Index of line clicked
				todos[index] = new_todo
				functions.write_todos(todos)
				window['todos'].update(values=todos)
			except IndexError:
				sg.Popup("Please select an item first.")

		case "Complete":
			try:
				todo_to_complete = values_dict['todos'][0]
				todos = functions.get_todos()
				todos.remove(todo_to_complete)
				functions.write_todos(todos)
				window['todos'].update(values=todos)
				window['todo'].update(value='')
			except IndexError:
				sg.Popup("Please select an item first.")

		case 'todos':
			window['todo'].update(value=values_dict['todos'][0])

		case 'Exit':
			break
		case sg.WIN_CLOSED:
			break

window.close()
