from re import I
from tkinter import *
import sqlite3
from tkinter import messagebox
import os
class DB:
    def create_db(self):
        path = os.path.dirname(os.path.abspath(__file__))
        
        self.db = os.path.join(path,'project.db')
        self.con   = sqlite3.connect(self.db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS usercred (username text PRIMARY KEY NOT NULL,profession text NOT NULL,age text NOT NULL,gender text NOT NULL,password text NOT NULL)")
        self.con.commit()
    
        

    def insert_into_db(self,x,y,z,g,p):
        try:
            self.con = sqlite3.connect(self.db)
            self.cur  = self.con.cursor()
            sql_query = 'INSERT INTO usercred (username,profession,age,gender,password) VALUES(?,?,?,?,?);'
            self.cur.execute(sql_query,(x,y,z,g,p))
            self.con.commit()
            messagebox.showinfo("Account","Account Created Successfully")
            
            self.con.close()
            
        except Exception as es:
            messagebox.showerror("Error","Incorrect Entry")
    
    def retrive(self,x,y):
        try:
            self.con = sqlite3.connect(self.db)
            self.cur = self.con.cursor()
            sql_query = "SELECT username,password FROM usercred;"
            self.cur.execute(sql_query)
            records = self.cur.fetchall()
           
            flag = 0
            for i,j in records:
               
                if(i==x and j==y):
                    self.user = i  
                    self.passw = j
                    flag= 1
                    return True
            if(flag==0):
                return False
        except EXCEPTION:
            messagebox.showerror("Error","Error")
            
            
        

    def createdb_app_data(self,user):
        path = os.path.dirname(os.path.abspath(__file__))
        self.user = user.replace(' ','_')
        self.db = os.path.join(path,'project.db')
        self.con = sqlite3.connect(self.db)
        self.cur  = self.con.cursor()
        sql_query = "CREATE TABLE IF NOT EXISTS application(name text,pass text,firstname text PRIMARY KEY NOT NULL,websitename text NOT NULL,password text NOT NULL,note text,FOREIGN KEY(name,pass) REFERENCES usercred(username,password))"
        self.cur.execute(f'CREATE TABLE IF NOT EXISTS {self.user}(name text,pass text,firstname text PRIMARY KEY NOT NULL,websitename text NOT NULL,password text NOT NULL,note text,FOREIGN KEY(name,pass) REFERENCES usercred(username,password))')
        self.con.commit()
        self.con.close()
    
    def insert_app_data(self,u,p,x,y,z,n):
        try:
            u = self.user
            print(u)
            self.con = sqlite3.connect(self.db)
            self.cur = self.con.cursor()
            sql_query ='''INSERT INTO application (name,pass,firstname,websitename,password,note) VALUES(?,?,?,?,?,?);'''
            self.cur.execute(f'INSERT INTO {u}(name,pass,firstname,websitename,password,note) VALUES(?,?,?,?,?,?);',(u,p,x,y,z,n))
            messagebox.showinfo("DATA","Data Inserted Successfully")
            self.con.commit()
            return u
        except Exception as es:
            messagebox.showerror("Error","Incorrect Entry")
        


    def del_record(self,tab_name,webname):
         try:
            del_fac = webname
            path = os.path.dirname(os.path.abspath(__file__))
        
            self.db = os.path.join(path,'project.db')

            self.con = sqlite3.connect(self.db)
            self.cur = self.con.cursor()
            


            self.cur.execute(f'DELETE FROM {tab_name} WHERE websitename ="{webname}"')
         
           
            self.con.commit()
        
            messagebox.showinfo("Delete","Record Deleted")
        
         except Exception as es:
             messagebox.showwarning("Warning","Record Doesn't Exist")


        


        