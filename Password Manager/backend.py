from tkinter import *
import sqlite3
from tkinter import messagebox

class DB:
    def create_db(self):
        self.con   = sqlite3.connect('GIT/Password-Manager-GUI/Password Manager/app.db')
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS userdcred (username text,profession text,age int,gender text,password text,)")
        self.con.commit()
        self.con.close()

    def insert_into_db(self,x,y,z,g,p):
        try:
            self.con = sqlite3.connect("GIT/Password-Manager-GUI/Password Manager/app.db")
            self.cur  = self.con.cursor()
            sql_query = 'INSERT INTO usercred (username,profession,age,gender,password) VALUES(?,?);'
            self.cur.execute(sql_query,(x,y,z,g,p))
            self.con.commit()
            self.con.close()
        except Exception as es:
            messagebox.showerror("Error,Error")

