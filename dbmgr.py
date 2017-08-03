import sqlite3
from tkinter import messagebox

class Database:

    def connect_db(self, dbpath):

        try:
            self.conn = sqlite3.connect(dbpath)
            self.cursor = self.conn.cursor()
            messagebox.showinfo("Database Manager", "Connected to DB")
        except:
            messagebox.showinfo("Database Manager","Can't connect to DB/ no DB of that name found")

    def process_script(self,query):

        buffer = ""

        for line in query:
            buffer += line

        if sqlite3.complete_statement(buffer):
            try:
                buffer = buffer.strip()
                self.cursor.execute(buffer)
                self.conn.commit()
                return self.query_output()
                messagebox.showinfo("SQL query", "Successful")
            except sqlite3.Error as e:
                messagebox.showinfo("Error",e.args[0])
        else:
            messagebox.showinfo("Error","No SQL query detected")

    def query_output(self):
        try:
          return  self.cursor.fetchall()
        except:
           return  "Nothing to return"


