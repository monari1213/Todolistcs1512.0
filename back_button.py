#import list_page_tk_code as list
import user_tk_code as user

def go_back():
    #close the other page
    #list.list_page.destroy()
    #set page to user page
    user.user_page.mainloop()
    print("The back button works")