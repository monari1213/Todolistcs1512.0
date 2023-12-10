def read_user_lists(file_name):
    new_file = open(f"{file_name}", "a+")
    # with open(f"{user_input}_lists.txt", "a") as new_file:
    lines = new_file.readlines()
    return lines