from tkinter import *
import sqlite3
from tkinter import messagebox
import os
class DB:
    def create_db(self):
        path = os.path.dirname(os.path.abspath(__file__))
        
        self.db = os.path.join(path,'app.db')
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
        print(x,y)
        try:
            self.con = sqlite3.connect(self.db)
            self.cur = self.con.cursor()
            sql_query = "SELECT username,password FROM usercred;"
            self.cur.execute(sql_query)
            records = self.cur.fetchall()
            for i,j in records:
                if(i==x and j==y):
                    return True
                else:
                    return False
        except EXCEPTION as es:
            messagebox.showerror("Error","Error")