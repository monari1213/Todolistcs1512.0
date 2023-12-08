import tkinter as tk

def read_user_lists(user_input):
    with open(f"{user_input}_lists.txt", "a") as new_file:
        lines = new_file.readlines()
    return lines