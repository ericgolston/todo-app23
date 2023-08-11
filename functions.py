FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
	"""Get todos from todos.txt file and
    return list of items"""
	with open(filepath, 'r') as file_local:
		todos_local = file_local.readlines()  # Creating list in .py file
	return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
	"""Write todos item list in the text file.
    Overwrites."""
	with open(filepath, 'w') as file:
		file.writelines(todos_arg)  # Write items in list to the file


if __name__ == '__main__':  # Directly or Indirectly run below.
	print("Hello")
	print(get_todos())
