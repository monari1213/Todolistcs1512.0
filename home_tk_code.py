import tkinter as tk
import many_page as many
import home_functions as home

#import back_button as back
#import read_lists as read

#creates the window
home_page = tk.Tk()

list_num_list = []
task_num_list = []

#sets the size of the page and title
home_page.geometry("1440x1024")
home_page.title(" home_page")

#labels the window 
user_title = tk.Label(home_page, text="To-do List", font=("times new roman", 30, "bold")).pack()

#creates the new list button and places it
new_list_button = tk.Button(home_page, text="+", relief="raised" ,font=("times new roman", 30, "bold"), command = home.create_new_list).pack()

#the lists buttons and their corresponding tasks need to be adjusted for all the different possible files

lists = many.read_user_lists("user_lists.txt")
    
for i in range(len(lists)):
    list_num_list.append(f"{lists[i]}")
    list_num_list[-1] = tk.Button(home_page, text= list_num_list[-1 ], relief="raised", font=("times new roman", 20)).pack()
    # tasks = ["task1", "task2"]#read.read_user_listsread_user_lists(list_num_list[-1])
    # for j in range(len(tasks)):
    #     task_num_list.append(f"{tasks[j]}")
    #     task_num_list[-1] = tk.Label(user_page, text=(task_num_list[-1]), relief="ridge", font=("times new roman", 25)) 
        

#opens the page
# user_page.mainloop()