import tkinter as tk
from functools import partial
from subprocess import *
import sys
import dbmgr


class Application:

    def __init__(self, ApplicationTitle):
        self.dbpath = "LabTools.db"
        self.root = tk.Tk()
        self.root.title(ApplicationTitle)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.content = tk.Frame(self.root)
        self.connect_db(self.dbpath)
        self.create_widgets()
        self.create_tools()


    def create_widgets(self):

        #widgets and parents

        self.frame_header = tk.Frame(self.content, padx=10, pady=10)
        self.lbl_header = tk.Label(self.frame_header)
        self.frame_tools = tk.Frame(self.content)
        self.lbl_header["text"] = "LabTools is a central database for all the custom tools made by the members of the PSFRU"


        #grid management

        self.content.grid(column=0, row=0)
        self.frame_header.grid(column=0, row=0, sticky=("N", "S", "E", "W"))
        self.lbl_header.grid(column=3, row=0, columnspan=2, sticky=("N", "W"), padx=5)
        self.frame_tools.grid(column=0, row=3,sticky=("N", "S", "E", "W"))

    def create_tools(self):

        tool_name_list = list()
        tool_name_list = self.get_tool_info()

        i = 0

        for entry in tool_name_list:
            tk.Button(self.frame_tools,text=entry[1],command=partial(self.run_tool,entry[2])).grid(column=0,row=i)
            tk.Label(self.frame_tools,text=entry[3]).grid(column=1,row=i)
            i+=1

    def connect_db(self,dbpath):
        db_manager.connect_db(dbpath)

    def get_tool_info(self):
        query = "SELECT * FROM Tools;"
        return db_manager.process_script(query)

    def run_tool(self,tool_path):
        try:
            check_call([sys.executable or 'python3'or 'sh', tool_path])
        except:
            call([tool_path])

    def display_app(self):
        self.root.mainloop()



db_manager = dbmgr.Database()
app = Application("LabTools v1.0")
app.display_app()
