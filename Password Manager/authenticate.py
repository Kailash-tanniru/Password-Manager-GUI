
from tkinter import *
from tkinter.tix import Tree

from PIL import ImageTk
from tkinter import ttk
from tkinter import font
from aem import app
from tkmacosx import Button #if macos
from PasswordManager import App

from backend import DB
from tkinter import messagebox


class Authenticate:
    def __init__(self,root,w,h):
        self.root = root
        
        self.frame = Frame(self.root,width=w,height=h,bg='#FFCCD2')
        self.frame.propagate(0)
        self.frame.pack()

        #Create Database
        self.database = DB()
        self.database.create_db()
        # self.bg = ImageTk.PhotoImage(file="bg.jpg")
        # self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0)
        self.login()        
        
    def login(self):
        username = StringVar()
        password = StringVar()
        #===LOGIN FRAME===#
        self.login_frame = Frame(self.frame,width=500,height=600,bg='white')
        self.login_frame.propagate(0)
        self.login_frame.place(x=250,y=80)

       
    

        # #----LOGIN TITLE---#
        self.login_title_frame = Frame(self.login_frame,width=500,height=100,bg='#EEEEEE')
        self.login_title_frame.propagate(0)
        self.login_title_frame.pack()

        self.login_title = Label(self.login_title_frame,text='SIGNIN-HERE',font=("Impact",35,"bold"),fg='#0F0E0E',bg='#EEEEEE',)
        self.login_title.place(x=150,y=25)
        

        #===USERNAME===#
        self.username_label = Label(self.login_frame,text='username',font=("Courier",20,),fg='black',bg='white')
        self.username_label.place(x=60,y=150)
        #USERNAME LABEL
        self.username_entry = Entry(self.login_frame,textvariable=username,font=("Script",20),bg='#EEEEEE',fg='#0F0E0E',relief='flat',justify='center')
        
        self.username_entry.place(x=65,y=190,width=350,height=35)

        #====Password label====#
        self.password_label = Label(self.login_frame,text='Password',font=("Courier",20),fg='black',bg='white')
        self.password_label.place(x=60,y=270)

        self.password_entry = Entry(self.login_frame,textvariable=password,font=("Script",15,"bold"),bg='#EEEEEE',fg='#0F0E0E',relief='flat',show='X',justify='center')
        self.password_entry.place(x=65,y=310,width=350,height=35)

        #===LOGIN BUTTON===#
        #command=lambda:App(self.frame,self.root)
        self.submit_button = Button(self.login_frame,text='LOGIN',command=lambda:self.open_app(username.get(),password.get()),background='#D6E5FA',foreground='black',font=('Roman',20,'bold'),relief=SUNKEN,borderwidth=0,)
        self.submit_button.place(x=160,y=400,height=50,width=150)


        self.signup_link = Label(self.login_frame,text="Haven't Registered?",font=("calibre",15),fg='black',bg='white')
        self.signup_link.place(x=60,y=500)
        
        self.signup_link_button = Button(self.login_frame,text="SIGNUP",command=lambda:self.signup_window())
        self.signup_link_button.place(x=70,y=530,height=30)

        self.forgot_password = Button(self.login_frame,text='Forgot Password?',command=None)
        self.forgot_password.place(x=300,y=530,height=30)

    def open_app(self,x,y):
        flag = self.database.retrive(x,y)
        if flag==True:
            App(self.frame,self.root)
        else:
            messagebox.showerror("Error","Credentials Error")

    
    def signup_window(self):
        w = 1200
        h=800

        self.signup_frame = Toplevel(self.login_frame)
        self.signup_frame.geometry(f"{w}x{h}")
        self.signup_frame.title("Signup Page")
        self.signup_frame.resizable(False,False)

        
        self.bg = ImageTk.PhotoImage(file="bg.jpg")
        self.bg_image = Label(self.signup_frame,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

        self.signin_register_frame = Frame(self.signup_frame,width=700,height=670)
        self.signin_register_frame.propagate(0)
        self.signin_register_frame.place(x=250,y=80)
        self.signup_form()

        self.signup_frame.mainloop()

    def signup_form(self):
        self.form_title_frame = Frame(self.signin_register_frame,width=700,height=70,bg='#FFF8F3')
        self.form_title_frame.propagate(0)
        self.form_title_frame.pack()
        
        self.form_title = Label(self.form_title_frame,text='REGISTER PAGE',font=("Impact",35,"bold"),fg='#0F0E0E',bg='#FFF8F3',)
        self.form_title.place(x=240,y=10)

        self.form_body_frame = Frame(self.signin_register_frame,width = 700,height=600,bg='white')
        self.form_body_frame.pack()

        #===PROFILE NAME==#

        #String variables 
        first_name = StringVar()
        last_name = StringVar()
        
        first_name.set("")
        last_name.set("")

        #First name
        self.first_name = Label(self.form_body_frame,text="FIRST NAME",font=("Courier",20,),fg='black',bg='white')
        self.first_name.place(x=40,y=30)

        #First name entry
        self.firstname_entry  = Entry(self.form_body_frame,textvariable=first_name,)
        self.firstname_entry.place(x=40,y=70,width=250,height=30)
        

        self.last_name = Label(self.form_body_frame,text="LAST NAME",font=("Courier",20,),fg='black',bg='white')
        self.last_name.place(x=360,y=30)

        #Last Name Entry
        self.lastname_entry  = Entry(self.form_body_frame,textvariable=last_name,)
        self.lastname_entry.place(x=360,y=70,width=250,height=30)


        #=====PROFESSION=====#
        profession = StringVar()
        profession.set("")
       

        self.prof_detail = Label(self.form_body_frame,text="COMPANY/ORGANIZATION",font=("Courier",20,),fg='black',bg='white')
        self.prof_detail.place(x=40,y=130)

        self.prof_detail_entry = Entry(self.form_body_frame,textvariable=profession,justify=CENTER)
        self.prof_detail_entry.place(x=40,y=170,width=580,height=35)

        #=====Age====#
        Age  = StringVar()
        Age.set("")
        

        self.age = Label(self.form_body_frame,text="AGE",font=("Courier",20,),fg='black',bg='white')
        self.age.place(x=40,y=230)
        self.age_spinbox = Spinbox(self.form_body_frame,from_=18,to_=60,textvariable=Age)
        self.age_spinbox.place(x=40,y=270)

        #===Gender==#
        gender = StringVar()
        gender.set("")
        self.gender_label = Label(self.form_body_frame,text="GENDER",font=("Courier",20,),fg='black',bg='white')
        self.gender_label.place(x=360,y=230)

        self.male = Radiobutton(self.form_body_frame,text='MALE',variable=gender,value=1,font=("Roman",15,),bg='white')
        self.male.place(x=360,y=270)

        self.female = Radiobutton(self.form_body_frame,text='FEMALE',variable=gender,value=2,font=("Roman",15,),bg='white')
        self.female.place(x=460,y=270)

        self.others = Radiobutton(self.form_body_frame,text='OTHERS',variable=gender,value=3,font=("Roman",15,),bg='white')
        self.others.place(x=560,y=270)

        #Password
        signin_password = StringVar()
        signin_password.set("")

        self.register_password = Label(self.form_body_frame,text="*PASSWORD",font=("Courier",20,),fg='black',bg='white')
        self.register_password.place(x=40,y=310)

        self.registerpassword_entry = Entry(self.form_body_frame,textvariable=signin_password,show='*',font=("Script",25,"bold"))
        self.registerpassword_entry.place(x=40,y=350,width=580,height=35)

        #CONFIRM PASSWORD
        confirm_password = StringVar()
        confirm_password.set("")

        self.register_confirm_password = Label(self.form_body_frame,text="CONFIRM PASSWORD",font=("Courier",20,),fg='black',bg='white')
        self.register_confirm_password.place(x=40,y=390)

        self.register_confirmpassword_entry = Entry(self.form_body_frame,textvariable=confirm_password,show='*',font=("Script",25,"bold"))
        self.register_confirmpassword_entry.place(x=40,y=430,width=580,height=35)


        #===SIGUP BUTTON===#
        self.signup_button = Button(self.form_body_frame,text="SIGN-UP",command=lambda:self.check_credentials(first_name,last_name,profession,Age,gender,signin_password,confirm_password),bg='black',fg='white',font=("Impact",20,"bold"))
        self.signup_button.place(x=250,y=500,height=50,width=150)


    def check_credentials(self,a,b,c,d,e,f,g):
        if f.get()!= g.get():
            messagebox.showwarning('Password',"Password Doesn't Match!Please Confirm Password")
        elif f.get()==g.get():
            name = a.get()+' '+b.get()
            if(e.get()==1):
                gender  = 'male'
            elif(e.get()==2):
                gender = 'female'
            else:
                gender = 'Others'
            
    
            
            self.database.insert_into_db(name,c.get(),d.get(),gender,f.get())
            





        













        
