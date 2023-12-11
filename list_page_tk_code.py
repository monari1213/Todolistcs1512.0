import tkinter as tk
import home_tk_code as home
import os

def open_list(list_name, read_lines):
    list_page = tk.Tk()
    list_page.geometry("1440x1024")
    list_page.title(f"list page_{list_name}")
    list_page.config(background= "white")
        
    list_back_button = tk.Button(list_page, text="Back", 
                                    relief="raised" ,
                                    font=("times new roman", 60), background= "#B8B6D8")
    list_back_button.pack(side="top", anchor="w" )

    global user_list
    user_list = tk.Entry(list_page, font=("times new roman", 69, "bold"), justify= "center", background= "#F7B97D")
    user_list.pack()
    user_list.insert(tk.END ,list_name)
    old_name = user_list.get()
    user_list.pack(side="top",anchor="center")

    global text_box
    text_box = tk.Text(list_page, background= "#B8B6D8", font=("times new roman", 25))
    text_box.pack()
    for i in range(len(read_lines)):
        text_box.insert(tk.END, read_lines[i])
        
    def save():
        written = text_box.get("1.0", tk.END)
        name = user_list.get()
        with open(f"{name}.txt", "w") as file:
            file.write(written)
        with open("user_lists.txt", "r") as user:
            lines = user.readlines()
        if old_name != name:
            os.remove(f"{old_name}.txt")
            with open("user_lists.txt", "w") as user:
                for line in lines:
                    if line.strip("\n") != old_name:
                        user.write(line)
            with open("user_lists.txt", "a") as user:
                user.write(f"\n{name}")
            
    def back():
        save()
        list_page.destroy()
        home.open_home()
      
    list_back_button.config(command=back)  

    list_page.mainloop()
    