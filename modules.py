import tkinter as tk

add_item_open = False

def exit_add_item(self):
    global add_item_open
    add_item_open = False
    print("destorying")
    self.destroy
    
    def open_new_notepad (self):
        self.notepad_frame.forget
        self.notepad_frame_write.grid(row=0,column=0)
    


class flashcard_module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.title("Flashcard Module")
        self.geometry ("1000x700")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        self.flashcard_label = tk.Label(self,text="Flashcard ahh frame",borderwidth=3, relief="groove")
        self.flashcard_label.grid(row=0,column=0)





class notepad_module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.title("Notepad Module")
        self.geometry("675x375")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        self.notepad_frame = tk.Frame(self,borderwidth=3)
        self.notepad_frame.grid(row=0,column=0)

        for i in range(2):
            self.notepad_frame.rowconfigure(i,weight=1)
        
        self.notepad_frame.columnconfigure(0,weight=1)
        self.notepad_frame.columnconfigure(1,weight=1)


        global open_new_notepad
        self.new_text_btn = tk.Button(self.notepad_frame,text="Create a new text file new", command= lambda:open_new_notepad(self.notepad_frame,self.notepad_write_frame))
        self.new_text_btn.grid(row=0,column=0,padx=10)

        self.open_text_btn = tk.Button (self.notepad_frame,text="Open a text file")
        self.open_text_btn.grid (row=0, column=1,padx=10)

        
        
        self.notepad_write_frame = tk.Frame(self,borderwidth=3)


        for i in range(2):
            self.notepad_write_frame.rowconfigure(i,weight=1)
        
        self.notepad_write_frame.columnconfigure(0,weight=1)
        self.notepad_write_frame.columnconfigure(1,weight=1)

        self.notepad_title= tk.Entry (self.notepad_write_frame,textvariable= "Untitled Notepad")
        self.notepad_title.grid(row=0,column=0)

        def open_new_notepad (self):
            self.notepad_frame.forget
            self.notepad_frame_write.grid(row=0,column=0)

        #replace the notepad_frame with the notepad_write_frame
            


# class notepad (tk.Toplevel):
#     def __init__(self,master=None):
#         super().__init__(master)
#         self.title("Notepad")
#         self.geometry ("300x250")

#         self.notepad_write_frame = tk.Frame(self,borderwidth=3)

#         for i in range(2):
#             self.notepad_write_frame.rowconfigure(i,weight=1)
        
#         self.notepad_write_frame.columnconfigure(0,weight=1)
#         self.notepad_write_frame.columnconfigure(1,weight=1)

#         self.notepad_title= tk.Entry (self.notepad_write_frame,textvariable= "Untitled Notepad")
#         self.notepad_title.grid(row=0,column=0)

class calender_module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.title("calender Module")
        self.geometry ("375x300")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        self.calender_label = tk.Label(self,text="Calender",borderwidth=3, relief="groove")
        self.calender_label.grid(row=0,column=0)

class to_do_list_module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.title("To do list Module")
        self.geometry ("1000x700")

        for i in range (2):
            self.columnconfigure(i,weight=1)
        for i in range (2):
            self.rowconfigure(0, weight=1)
        # 3 columns, 2 rows

        self.add_td_item_btn = tk.Button (self,text="Add an item",borderwidth=3, relief = "solid", command= lambda: add_item(self))
        self.add_td_item_btn.grid(row=0, column=0, sticky="new", padx= 30, pady= 30)

        self.remove_td_btn = tk.Button (self,text="Remove top item",borderwidth=3, relief= "solid")
        self.remove_td_btn.grid(row=0, column=1, sticky="new", padx= 30, pady= 30)

        self.exit_td = tk.Button (self,text="Exit", borderwidth= 2, relief= "solid")
        self.exit_td.grid(row=2,column=0, sticky= "w", padx= 30, pady= 30)



        self.list_frame = tk.Frame(self,relief= 'raised', borderwidth=1)
        self.list_frame.grid(row=0,column=0,columnspan=2,rowspan=2,padx=20, pady=3,sticky="ew")
        self.list_frame.columnconfigure(0,weight=1)
        self.list_frame.columnconfigure(1,weight=1)
        for i in range (10):
            self.list_frame.rowconfigure(i,weight=1)

        self.to_do_list = tk.Label (self.list_frame,text ="Do some computer science nea")
        self.to_do_list.grid (row=0,column=0,columnspan=2,sticky="nsew", padx= 10, pady=3)
        for i in range (9):
            self.list_item_i = tk.Label (self.list_frame,text=f"item {i+1}")
            self.list_item_i.grid (row = i, column= 0, columnspan=2, sticky="nsew",padx=10, pady=3)

def add_item(self):
    global add_item_open
    if add_item_open == True:
        print("Cannot open, already open")
    else:
        add_item_open = True
        add_item_module(self)


class add_item_module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.title("Add an item")
        self.geometry ("300x250")

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)


        for i in range(2):
            self.rowconfigure(i,weight=1)

        self.add_item_button = tk.Button (self,text="Add item",borderwidth=3, relief= "solid")
        self.add_item_button.grid(row=2,column=1,padx=3,pady=3)

        self.item_input = tk.Text (self,borderwidth=3, relief= "solid")
        self.item_input.grid(row=1,column=0,columnspan=2)

        self.exit_td_add = tk.Button(self,text="Exit",borderwidth=3, relief= "solid", command = lambda: exit_add_item(self))
        self.exit_td_add.grid(row=2,column=0,padx=3,pady=3)