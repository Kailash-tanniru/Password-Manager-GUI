from tkinter import *



from tkmacosx import Button
from create import Create
from delete import DeleteRecord
from backend import DB
import os
from tkinter import messagebox
import sqlite3
import sys
class App:
    def __init__(self,x,y,root,menuroot):
        self.user = x
        self.passw = y
       
        self.root = root
        self.menuroot = menuroot
        self.app_frame = Frame(self.root,width=1000,height=750,bg='#EEF2FF')
        self.app_frame.propagate(0)
        self.app_frame.pack()
        self.database = DB()
        self.add_menubar()
        
        self.main_window()
        self.labels()
        
     

    
    def add_menubar(self):
        self.menubar = Menu(self.menuroot)
        self.menuroot.config(menu=self.menubar)
        
    

        

        #Creating File Menu
        self.filemenu = Menu(self.app_frame,tearoff=0)

        self.filemenu.add_command(label='Save',command=None)
        self.filemenu.add_command(label='Download',command=None)
        
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit',command=None)
        self.menubar.add_cascade(label='File',menu = self.filemenu)

        #edit menu

        self.editmenu = Menu(self.app_frame,tearoff=0)

        self.editmenu.add_command(label='Info',command=None)
        self.editmenu.add_command(label='About',command=None)

        self.editmenu.add_separator()
        self.editmenu.add_command(label='Author',command=None)
        self.menubar.add_cascade(label='Edit',menu = self.editmenu)

        #creating Details

        
    def main_window(self):
        self.top_frame = Frame(self.app_frame,width=1000,height=650,bg='white',borderwidth=2,relief=SUNKEN)
        self.top_frame.pack()
        self.sno_frame=Frame(self.top_frame,bg='#EEEEEE',width=60,height=650,relief=SUNKEN,borderwidth=1)
        self.profile_name=Frame(self.top_frame,bg='pink',width=400,height=650,relief=SUNKEN,borderwidth=1)
        self.profile_name.propagate(0)

        self.web_frame = Frame(self.top_frame,bg='#AEFEFF',width=240,height=650,relief=SUNKEN,borderwidth=1)
        
        self.password_frame = Frame(self.top_frame,bg='#FFF89A',width=300,height=650,relief=SUNKEN,borderwidth=1)

        self.sno_frame.pack(side=LEFT,expand="yes",fill=Y)
        self.profile_name.pack(side=LEFT,expand="yes",fill=Y)
        self.web_frame.pack(side=LEFT,fill=Y,expand=YES)
        self.password_frame.pack(side=LEFT,expand="yes",fill=Y)

        self.bottom_frame = Frame(self.app_frame,width=1000,height=100,bg='red',borderwidth=1,relief=SUNKEN)
        self.bottom_frame.pack(fill=BOTH,side=BOTTOM)

        self.add_columns()

        

    def add_columns(self):
        self.sno_column = Frame(self.sno_frame,width=60,height=50,bg='white',)
        self.sno_column.propagate(0)
        self.sno_column.pack()
        self.profile_column = Frame(self.profile_name,width=400,height=50,bg='white')
        self.profile_column.propagate(0)
        self.profile_column.pack()
        self.web_column = Frame(self.web_frame,width=240,height=50,bg='white')
        self.web_column.propagate(0)
        self.web_column.pack()
       
        self.passw_column = Frame(self.password_frame,width=300,height=50,bg='white')
        self.passw_column.propagate(0)
        self.passw_column.pack()

        self.sno_text = Label(self.sno_column,text='S.No',bg='white',pady=50)
        self.sno_text.pack()
       
        self.web_text = Label(self.web_column,text='Web Name',bg='white',pady=50)
        self.web_text.pack()

        self.profile_text = Label(self.profile_column,text='Profile',bg='white',pady=50)
        self.profile_text.pack()

        self.passw_text = Label(self.passw_column,text='Password',bg='white',pady=50)
        self.passw_text.pack()
       
        self.operation_buttons()
       
    

    def labels(self):
        
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            self.user = self.user.replace(' ','_')
        
            self.db = os.path.join(path,'project.db')
            self.con = sqlite3.connect(self.db)
            self.cur = self.con.cursor()
            self.cur.execute(f'SELECT firstname,websitename,password FROM {self.user}')
            records = self.cur.fetchall()
            inc = 1
            for i,j,l in records:
               
                id_label = Label(self.sno_frame,text = inc,bg='#EEEEEE',relief=RIDGE,pady=20).pack(fill=X)
                name  = Label( self.profile_name,text=i,bg='pink',relief=RIDGE,pady=20).pack(fill=X)
                web = Label(self.web_frame,text=j,bg='#AEFEFF',relief=RIDGE,pady=20).pack(fill=X)
                passwor = Label(self.password_frame,text =l,bg='#FFF89A',relief=RIDGE,pady=20,font=("Courier",15)).pack(fill=X)
                inc+=1
            
        except EXCEPTION :
             sys.exc_clear()

    def operation_buttons(self):
        self.operation_frame = Frame(self.bottom_frame,width=600,height=100,bg='yellow',)
        self.operation_frame.propagate(0)
        self.operation_frame.grid(row=0,column=0)


        self.holder_panel = Frame(self.bottom_frame,width=400,height=100,bg='#35589A')
        self.holder_panel.grid(row=0,column=1)


        self.create = Button(self.operation_frame,text='Create',bg='green',fg='white',command=lambda:Create(self.app_frame,self.user,self.passw))
        self.create.pack(side=LEFT,expand=YES,fill=BOTH)
        

        self.update = Button(self.operation_frame,text='Update',bg='white',command=None)
        self.update.pack(side=LEFT,expand=YES,fill=BOTH)

        self.delete = Button(self.operation_frame,text="Delete",bg='white',command=lambda:DeleteRecord(self.app_frame,self.user))
        self.delete.pack(side=LEFT,expand=YES,fill=BOTH)

        self.logout = Button(self.operation_frame,text='Logout',bg='red',fg='white',command=lambda:self.app_frame.destroy())
        self.logout.pack(side=LEFT,expand=YES,fill=BOTH)


        