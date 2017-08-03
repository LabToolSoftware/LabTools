import tkinter as tk
from functools import partial
from tkinter import filedialog
from tkinter import *
import dbmgr


class Form:
    def __init__(self):
        self.root= tk.Tk()
        self.root.title("Tool Manager")
        self.path = StringVar(self.root)
        self.toolName = StringVar(self.root)
        self.toolPath = StringVar(self.root)
        self.tablelist = ['']
        self.selectedtable = StringVar(self.root)
        self.create_widgets()

    def create_widgets(self):

        #Instantiation
        self.frame_content = tk.Frame(self.root)
        self.frame_main = tk.Frame(self.frame_content)

        self.lbl_databasename = tk.Label(self.frame_main,text="Current tool DB: ")
        self.entry_databasepath = tk.Entry(self.frame_main, textvariable=self.path)
        self.button_dbbrowse = tk.Button(self.frame_main,text="Browse",command=partial(self.get_path,self.path))
        self.button_dbconn = tk.Button(self.frame_main,text="Connect",command=partial(self.connect_db,self.path))
        self.lbl_table = tk.Label(self.frame_main,text="Table: ")
        self.option_tables = tk.OptionMenu(self.frame_main,self.selectedtable,*self.tablelist)

        self.lbl_toolname = tk.Label(self.frame_main,text="New tool name: ")
        self.entry_toolname = tk.Entry(self.frame_main,textvariable=self.toolName)

        self.lbl_toolpath = tk.Label(self.frame_main,text="Tool path: ")
        self.entry_toolpath = tk.Entry(self.frame_main,textvariable=self.toolPath)
        self.button_toolpath = tk.Button(self.frame_main,text="Browse",command=partial(self.get_path,self.toolPath))

        self.lbl_tooldescription = tk.Label(self.frame_main,text="Enter a short description for new tool below: ")
        self.text_tooldescription = tk.Text(self.frame_main,width=50,height=10)

        self.button_accept = tk.Button(self.frame_main,text="Accept",command=self.add_tool)
        self.button_cancel = tk.Button(self.frame_main,text="Cancel",command=self.close_app)

        #Grid management

        self.frame_content.grid(column=0,row=0)
        self.frame_main.grid(column=0,row=0)
        self.lbl_databasename.grid(column=0,row=0,sticky=("W"))
        self.entry_databasepath.grid(column=1,row=0,sticky=("W"))
        self.button_dbbrowse.grid(column=2,row=0,sticky=("W"))
        self.button_dbconn.grid(column=4,row=0,sticky=("W"))
        self.lbl_table.grid(column=0, row=1,sticky=("W"))
        self.option_tables.grid(column=1,row=1,sticky=("W"))
        self.lbl_toolname.grid(column=0,row=2,sticky=("W"))
        self.entry_toolname.grid(column=1,row=2,sticky=("W"))
        self.lbl_toolpath.grid(column=0,row=3,sticky=("W"))
        self.entry_toolpath.grid(column=1,row=3,sticky=("W"))
        self.button_toolpath.grid(column=3,row=3,sticky=("W"))
        self.lbl_tooldescription.grid(column=0,row=4,sticky=("W"))
        self.text_tooldescription.grid(column=0,row=5,columnspan=2,sticky=("W"))
        self.button_accept.grid(column=1,row=6,sticky=("W"))
        self.button_cancel.grid(column=2,row=6,sticky=("W"))

    def connect_db(self, dbpath):
        db_manager.connect_db(dbpath.get())
        self.get_dbtables()

    def get_dbtables(self):

        table_list = "SELECT name FROM sqlite_master WHERE type=\'table\';"

        query_return = db_manager.process_script(table_list)

        self.option_tables['menu'].delete(0,'end')

        for item in query_return:
            self.option_tables['menu'].add_command(label=item,command=tk._setit(self.selectedtable,item))

    def get_path(self,path):

        path.set(filedialog.askopenfilename())

    def add_tool(self):
        tablename = self.selectedtable.get().lstrip('(\'').rstrip('\',)')
        toolname = self.entry_toolname.get()
        toolpath = self.toolPath.get()
        tooldescript = self.text_tooldescription.get("1.0",END)

        query = "INSERT INTO " + tablename + "(NAME,PATH,DESCRIPTION) VALUES(\"" + toolname + "\",\"" + toolpath + "\",\"" + tooldescript + "\");"

        query_output = db_manager.process_script(query)

        self.close_app()

    def close_app(self):
        try:
            self.conn.close()
            exit()
        except:
            exit()

    def display_app(self):
        self.root.mainloop()

db_manager = dbmgr.Database()
app = Form()
app.display_app()