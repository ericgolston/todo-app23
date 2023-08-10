# from functions import get_todos, write_todos
import functions
import time

print("Time is below")
now = time.strftime("%b %d %Y %H %M %S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]  # Written at same time as user action

        todos = functions.get_todos()  # List from function

        todos.append(todo)  # Appending input to that newly created list
        todos.append('\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()  # List f

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item.title()}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from list"
            print(message)
        except SyntaxError:
            print("No item with that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Hey, you have entered an unknown command")

print("Bye!")

