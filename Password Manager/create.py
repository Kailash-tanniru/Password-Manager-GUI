from tkinter import *
from tkinter import font
from tkmacosx import Button
from tkinter import ttk
from PIL import ImageTk

class Create:
    def __init__(self,root):
        self.create_window = Toplevel(root)
        self.create_window.geometry("700x700")
        self.create_window.title("Create Records")
        self.create_window.resizable(False,False)
        self.Create_page()

        self.create_window.mainloop()

      
    
    def Create_page(self):
        self.page_frame = Frame(self.create_window,width=700,height=700,bg='lightgrey')
        self.page_frame.propagate(0)
        self.page_frame.pack()
        self.bg = ImageTk.PhotoImage(file="bg1.jpg")
        self.bg_image = Label(self.page_frame,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

        self.form()
    def form(self):
        profile_name = StringVar()
        website_name = StringVar()
        password_name = StringVar()
        note = StringVar()

        self.profile_name_label = Label(self.page_frame,text='PROFILE NAME',font=("Courier",20,),fg='black',bg='#FE7E6D')
        self.profile_name_label.place(x=70,y=100)

        self.profile_name_entry = ttk.Entry(self.page_frame,textvariable=profile_name)
        self.profile_name_entry.place(x=70,y=150,width=500,height=30)

        self.web_name_label = Label(self.page_frame,text='WEBSITE NAME',font=("Courier",20,),fg='black',bg='#FE7E6D')
        self.web_name_label.place(x=70,y=200)

        self.web_name_entry = ttk.Entry(self.page_frame,textvariable=website_name)
        self.web_name_entry.place(x=70,y=250,width=500,height=30)

        self.passw_name_label = Label(self.page_frame,text='PASSWORD',font=("Courier",20,),fg='black',bg='#FE7E6D')
        self.passw_name_label.place(x=70,y=300)

        self.passw_name_entry = ttk.Entry(self.page_frame,textvariable=password_name)
        self.passw_name_entry.place(x=70,y=350,width=500,height=30)

        self.note_name_label = Label(self.page_frame,text='NOTE',font=("Courier",20,),fg='black',bg='#FE7E6D')
        self.note_name_label.place(x=70,y=400)

        self.note_name_entry = ttk.Entry(self.page_frame,textvariable=note)
        self.note_name_entry.place(x=70,y=450,width=500,height=70)

        self.create_button = Button(self.page_frame,command=None,text="Create",bg='black',fg='white',font=("Impact",20,"bold"))
        self.create_button.place(x=230,y=600,width=200)