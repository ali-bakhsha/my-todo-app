FILEPATH = 'todos.txt'
def get_todos(filepath =FILEPATH):
    """
    return a list that read
    from a file
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
        return todos_local

def write_todos( todos_arg=[],filepath = FILEPATH ):
    """"Write the to-do list to a text file
    arguments are .. , a...
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())