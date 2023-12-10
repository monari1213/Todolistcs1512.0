def create_new_list():
    new_file = open("new_list.txt", "a+")
    
    with open("user_lists", "a") as lists:
        lists.write("new_list")