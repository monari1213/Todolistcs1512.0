import tkinter as tk
import home_tk_code as home

def open_list(list_name, read_lines):
    list_page = tk.Tk()
    list_page.geometry("1440x1024")
    list_page.title("list page")
    
    #text_box.get("1.0", tk.END)

    def back():
        list_page.quit
        home.open_home()
        
    list_back_button = tk.Button(list_page, text="Back", 
                                    relief="raised" ,
                                    font=("times new roman", 60), command= back)
    list_back_button.pack()
    #list_back_button.pack(side="top", anchor="w" )

    user_list = tk.Label(list_page, 
                            text= list_name, 
                            font=("times new roman", 69, "bold"))
    user_list.pack()
    #user_list.pack(side="left",anchor="nw",padx=(100,0), pady=(75,0))

    text_box = tk.Text(list_page, text = read_lines)
    text_box.pack()

    list_page.mainloop()
    
open_list()