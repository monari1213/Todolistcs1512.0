import tkinter as tk

# import back_button as back
#import open_popup as pop

list_page = tk.Tk()
list_page.geometry("1440x1024")
list_page.title("list page")

list_back_button = tk.Button(list_page, text="Back", 
                             relief="sunken" ,
                             font=("times new roman", 60)) # command=back.go_back)
list_back_button.pack(side="top", anchor="w" )

user_list = tk.Label(list_page, 
                     text="List 1 Name", 
                     font=("times new roman", 69, "bold"))
user_list.pack(side="left",anchor="nw",padx=(100,0), pady=(75,0))



edit_button = tk.Button(user_list, 
                        text="E", 
                        relief="sunken" ,
                        font=("times new roman", 30))
#edit_button.pack(side="right", anchor = "ne", padx = 50, pady=100)

add_button = tk.Button(user_list, 
                       text="A", 
                       relief="sunken" ,
                       font=("times new roman", 30))

#create back button
list_back_button = tk.Button(list_page, text="Back", relief="sunken" ,font=("times new roman", 30)) # command=back.go_back)
#list_back_button.grid(column=0, row=0, sticky= "wens")

# place all the way to the left
# also need an arrow

#commented out arrow code cause its pissng me off - Kristina
# arrow = tk.Canvas(user_list, width = 400, height = 400)
# arrow.pack()
# # draw an arrow from (50,50) to (200,200)
# arrow.create_line(50,50,200,200, arrow=tk.LAST)
# code creds for the arrow: https://www.codeease.net/programming/python/drawing-arrows-in-tkinter
# NONE OF THESE NUMBER PLACEMENTS ARE RIGHT BECAUSE I CANT RUN MY CODE
# THEY ARE PLACEHOLDERS


checkbox_var1 = tk.StringVar()
checkbox1 = tk.Checkbutton(list_page,
                text='<checkbox_label_1>',
                #command=check_changed,
                variable=checkbox_var1,
                font=("times new roman", 30),
                onvalue='<value_when_checked>',
                offvalue='<value_when_unchecked>')
# https://www.pythontutorial.net/tkinter/tkinter-checkbox/
checkbox1.pack(side="top",anchor="w",padx=(100,0), pady=(100,0))

edit_button = tk.Button(list_page, 
                        text="E", 
                        relief="sunken" ,
                        font=("times new roman", 90))
edit_button.pack(side="right", anchor = "n", padx = (0,20))

add_button = tk.Button(list_page, 
                       text="A", 
                       relief="sunken" ,
                       font=("times new roman", 90))
add_button.pack(side="right", anchor = "n", padx =(0,20))

checkbox_var2 = tk.StringVar()
checkbox2 = tk.Checkbutton(list_page,
                text='<checkbox_label_2>',
                #command=check_changed,
                variable=checkbox_var1,
                font=("times new roman", 30),
                onvalue='<value_when_checked>',
                offvalue='<value_when_unchecked>')
# https://www.pythontutorial.net/tkinter/tkinter-checkbox/
checkbox2.pack(side="top",anchor="w",padx=(100,0), pady=(100,0))

checkbox_var3 = tk.StringVar()
checkbox3 = tk.Checkbutton(list_page,
                text='<checkbox_label_3>',
                #command=check_changed,
                variable=checkbox_var1,
                font=("times new roman", 30),
                onvalue='<value_when_checked>',
                offvalue='<value_when_unchecked>')
# https://www.pythontutorial.net/tkinter/tkinter-checkbox/
checkbox3.pack(side="top",anchor="w",padx=(100,0), pady=(100,0))

checkbox_var4 = tk.StringVar()
checkbox4 = tk.Checkbutton(list_page,
                text='<checkbox_label_4>',
                #command=check_changed,
                variable=checkbox_var1,
                font=("times new roman", 30),
                onvalue='<value_when_checked>',
                offvalue='<value_when_unchecked>')
# https://www.pythontutorial.net/tkinter/tkinter-checkbox/
checkbox4.pack(side="top",anchor="w",padx=(100,0), pady=(100,0))


#opens the page
list_page.mainloop()