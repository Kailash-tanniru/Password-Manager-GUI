from email import message
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkmacosx import Button
from backend import DB
class DeleteRecord:
    def __init__(self,root,tab_name):
        self.root = root
        self.tab_name = tab_name
        self.deleterecord_frame = Toplevel(root)
        self.deleterecord_frame.geometry("500x200")
        self.deleterecord_frame.title("Delete Record")
        self.deleterecord_frame.resizable(False,False)
        self.field_frame()



        self.deleterecord_frame.mainloop()
    
    def field_frame(self):
        deletion_profilename = StringVar()
        self.window_frame = Frame(self.deleterecord_frame,width=500,height=200,bg='white')
        self.window_frame.propagate(0)
        self.window_frame.pack()

        #Name

        self.delete_name = Label(self.window_frame,text='Enter Website Name',font=("Impact",25,"bold"))
        self.delete_name.place(x=40,y=20)

        self.delete_name_entry = Entry(self.window_frame,font=("Courier",20,),textvariable=deletion_profilename,bg="black",fg="green")
        self.delete_name_entry.place(x=40,y=70,width=400,height=30)

        self.delete_button = Button(self.window_frame,text='Delete',bg='#FFCCD2',fg='white',font=("Impact",20,"bold"),command=lambda:self.delete_record(deletion_profilename.get()))
        self.delete_button.place(x=180,y=130,width=100,height=40)
    
    def delete_record(self,web):
        try:
           obj = DB()
           
           
           obj.del_record(self.tab_name,web)
           self.root.destroy()
           messagebox.showinfo("Security","Logging out!")

        except Exception:
            messagebox.showwarning('CONNECTION',"Connection Failed")
        