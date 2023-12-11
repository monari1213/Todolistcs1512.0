import tkinter as tk
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
        
        new_list_button = tk.Button(home_page, text= "new_list", relief="raised", font=("times new roman", 20), command= lambda: open_list("new_list"))
        new_list_button.pack()

    list_num_list = []
    task_num_list = []

    #sets the size of the page and title
    home_page.geometry("1440x1024")
    home_page.title(" home_page")
    home_page.config(background= "white")

    #creates the new list button and places it
    new_list_button = tk.Button(home_page, text="+", relief="raised" , background= "#B8B6D8",font=("times new roman", 30, "bold"), command = create_new_list).pack(side="left", anchor="nw")
    
    #labels the window 
    user_title = tk.Label(home_page, text="To-do List", font=("times new roman", 30, "bold"), background= "#F7B97D").pack(side="top", anchor="center", padx= 50)
        
    lists = read_user_lists("user_lists")
    for i in range(len(lists)):
        list_num_list.append(f"{lists[i]}")
        list_num_list[-1] = tk.Button(home_page, text= list_num_list[-1 ], relief="raised", background= "#B8B6D8",font=("times new roman", 20), command= lambda x=i: open_list(lists[x].strip("\n")))
        list_num_list[-1].pack(anchor="center", padx=10, pady= 10)

    #opens the page
    home_page.mainloop()