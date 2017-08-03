import dbmgr
from functools import partial
import tkinter as tk
from tkinter import *

class Application:
    def __init__(self,ApplicationTitle):
        self.root = tk.Tk()
        self.root.title(ApplicationTitle)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.script = StringVar(self.root)
        self.content = tk.Frame(self.root)
        self.database_path = StringVar(self.root)
        self.create_widgets()

    def create_widgets(self):

        # widgets and parents
        self.content = tk.Frame(self.root)
        self.frame_main = tk.Frame(self.content, width=200, height=200)
        self.lbl_databasename = tk.Label(self.frame_main, text="Current database: ")
        self.entry_databasepath = tk.Entry(self.frame_main, textvariable=self.database_path)
        self.button_setdb = tk.Button(self.frame_main, text="Connect", command=partial(self.connect_db, self.database_path))
        self.text_script = tk.Text(self.frame_main, width=50, height=10, wrap="word")
        self.text_output = tk.Text(self.frame_main, width=50, height=10, wrap="word")
        self.frame_buttons = tk.Frame(self.content, width=200, height=200)
        self.button_cancel = tk.Button(self.frame_buttons, text="Close", command=self.close_app)
        self.button_execscript = tk.Button(self.frame_buttons, text="Run Script", command=self.get_query_results)

        # grid management

        self.content.grid(column=0, row=0)
        self.frame_main.grid(column=0, row=0, sticky=("N", "S", "E", "W"))
        self.lbl_databasename.grid(column=0, row=0, sticky=("N", "S", "E", "W"))
        self.entry_databasepath.grid(column=1, row=0, sticky=("N", "S", "E", "W"))
        self.button_setdb.grid(column=3, row=0)
        self.text_script.grid(column=0, row=1, columnspan=2)
        self.text_output.grid(column=0, row=2, columnspan=2)
        self.frame_buttons.grid(column=0, row=3, sticky=("N", "S", "E", "W"))
        self.button_cancel.grid(column=1, row=0, sticky=("N", "S", "E", "W"))
        self.button_execscript.grid(column=0, row=0)

    def connect_db(self,dbpath):
        db_manager.connect_db(dbpath.get())

    def get_query_results(self):
        query = self.text_script.get("1.0", END)
        for line in db_manager.process_script(query):
            self.text_output.insert(INSERT,line)

    def close_app(self):

        try:
            self.conn.close()
            exit()
        except:
            exit()

    def display_app(self):
        self.root.mainloop()

db_manager = dbmgr.Database()
app = Application("SQL command line")
app.display_app()