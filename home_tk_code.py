import tkinter as tk
from tkinter import ttk
import list_page_tk_code as list

def read_user_lists(file_name):
    new_file = open(f"{file_name}.txt", "r")
    lines = new_file.readlines()
    return lines

lists = read_user_lists("user_lists")

def open_home():
    #creates the window
    global home_page
    home_page = tk.Tk()
    
    def open_list(list_name):
        lines = read_user_lists(list_name)
        home_page.destroy()
        list.open_list(list_name, lines)     
        
    def create_new_list():
        new_file = open("new_list.txt", "a+")
        
        with open("user_lists.txt", "a") as lists:
            lists.write("\nnew_list\n")
        
        new_list_button = tk.Button(home_page, text= "new_list", relief="raised", font=("times new roman", 20), background= "#B8B6D8" , command= lambda: open_list("new_list"))
        new_list_button.pack()

    list_num_list = []
    task_num_list = []

    #sets the size of the page and title
    home_page.geometry("1440x1024")
    home_page.title(" home_page")
    home_page.config(background= "white")

    #creates the new list button and places it
    new_list_button = tk.Button(home_page, text="+", relief="raised" , background= "#B8B6D8",font=("times new roman", 60, "bold"), command = create_new_list).pack(side="left", anchor="nw")
    
    #labels the window 
    user_title = tk.Label(home_page, text="To-do List", font=("times new roman", 69, "bold"), background= "#F7B97D").pack(side="top", anchor="center", padx= 50)
        
    lists_frame = tk.Frame(home_page)
    lists_frame.pack(fill="both", expand=1)
    lists_canvas = tk.Canvas(lists_frame)
    lists_canvas.pack(side="left", fill="both", expand=1)
    
    scrollbar = tk.Scrollbar(lists_frame, orient="vertical", command=lists_canvas.yview)
    scrollbar.pack(side="right", fill="y")
    lists_canvas.configure(yscrollcommand=scrollbar.set)
    lists_canvas.bind("<Configure>", lambda e: lists_canvas.configure(scrollregion = lists_canvas.bbox("all")))
    extra_frame = tk.Frame(lists_canvas)
    lists_canvas.create_window((0,0), window = extra_frame, anchor = "nw")
    
    lists = read_user_lists("user_lists")
    
    for i in range(len(lists)):
        list_num_list.append(f"{lists[i]}")
        list_num_list[-1] = tk.Button(extra_frame, text= list_num_list[-1 ], relief="raised", background= "#B8B6D8",font=("times new roman", 20), command= lambda x=i: open_list(lists[x].strip("\n")))
        list_num_list[-1].pack(anchor="center", padx=10, pady= 10)

    #opens the page
    home_page.mainloop()