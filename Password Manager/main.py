from cProfile import label
from tkinter import *
from tkinter import ttk
from authenticate import Authenticate





if __name__ == "__main__":
    root = Tk()

    width = 1000
    height = 750 #For MacBookAir 13.3 inch Height should not exceed greater than 800
    root.geometry(f"{width}x{height}")
    root.title("LOGIN PAGE-Kailash")
    root.configure(bg="yellow")
    # screen_width = root.winfo_screenwidth()
    # screen_height = root.winfo_screenheight()
    obj =  Authenticate(root,width,height)
    obj.login()
   
    
    
    
    root.resizable(False,False)
   
    root.mainloop()
