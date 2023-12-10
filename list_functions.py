#import list_page_tk_code as list
import home_tk_code as home

def go_back():
    try:
        #close the other page
        list.list_page.destroy()
        print("the list page was closed")
    except:
        print("the list page didnt fucking close like a lil bitch")
    try:
        #set page to user page
        home.home_page.mainloop()
        print("The back button works")
    except:
        print("the home page didnt open, like a lil bitch")