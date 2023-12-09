import tkinter as tk
import back_button as back
import read_lists as read

#import back_button as back
#import read_lists as read

#creates the window
user_page = tk.Tk()

list_num_list = []
task_num_list = []

#sets the size of the page and title
user_page.geometry("1440x1024")
user_page.title("user page")

#labels the window 
user_title = tk.Label(user_page, text="To-do List", font=("times new roman", 50, "bold"))

#creates the new list button and places it
new_list_button = tk.Button(user_page, text="+", relief="sunken" ,font=("times new roman", 50, "bold"))

#create back button
user_back_button = tk.Button(user_page, text="Back", relief="sunken" ,font=("times new roman", 30), command= back.go_back)

#the lists buttons and their corresponding tasks need to be adjusted for all the different possible files

lists = read.read_user_lists("user")
    
for i in range(len(lists)):
    list_num_list.append(f"{lists[i]}")
    list_num_list[-1] = tk.Button(user_page, text= list_num_list[-1 ], relief="sunken", font=("times new roman", 30))
    tasks = ["task1", "task2"]#read.read_user_listsread_user_lists(list_num_list[-1])
    for j in range(len(tasks)):
        task_num_list.append(f"{tasks[j]}")
        task_num_list[-1] = tk.Label(user_page, text=(task_num_list[-1]), relief="ridge", font=("times new roman", 25)) 
        

#opens the page
user_page.mainloop()