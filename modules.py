import tkinter as tk
import frame_template as ft
import global_variables as gv

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

        for i in range(3):
            self.columnconfigure(i,weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.flashcard_label = tk.Label(self,text="Flashcard ahh frame",borderwidth=3, relief="groove",width= 50,height=10,font=("Arial", 15))
        self.flashcard_label.grid(row=0,column=1)

        self.right_button = tk.Button(self,text= "<", relief="groove",width= 25,height=10,font=("Arial", 10))
        self.right_button.grid(row=0,column=0)

        self.left_button = tk.Button(self,text= ">", relief="groove",width= 25,height=10,font=("Arial", 10))
        self.left_button.grid(row=0,column=3)

        self.flashcard_exit = tk.Button(self,text="Exit",relief="groove", command = self.exit_flashcards)
        self.flashcard_exit.grid(row=1,column=1)

    def exit_flashcards(self):
        print (gv.flashcard_open)
        gv.flashcard_open = False
        self.destroy()








class notepad_module(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent= parent
        self.geometry("800x650")
        self.title("Notepad Module")


        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        self.notepad_frame= notepad_init_frame(self)
        self.notepad_frame.grid(row=0,column=0)


class notepad_init_frame(tk.Frame):
    def __init__(self,notepad_parent):
        super().__init__(notepad_parent)
        self.notepad_parent = notepad_parent

        for i in range(2):
            self.rowconfigure(i,weight=1)
        
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)

        self.new_text_btn = tk.Button(self,text="Create a new text file new",command = self.open_new_notepad)
        self.new_text_btn.grid(row=0,column=0,padx=10)

        self.open_text_btn = tk.Button (self,text="Open a text file", command= self.select_new_notepad)
        self.open_text_btn.grid (row=0, column=1,padx=10)

        self.grid(row=0,column=0)

    def open_new_notepad(self):
        print ("opening new notepad")
        self.notepad_parent.notepad_frame.destroy()
        self.notepad_parent.notepad_frame= notepad_edit_frame(self.notepad_parent)

    def select_new_notepad(self):
        print("Selecting a new notepad")
        self.notepad_parent.notepad_frame.destroy()
        self.notepad_parent.notepad_frame= notepad_select_frame(self.notepad_parent)

class notepad_edit_frame(tk.Frame):
    def __init__(self,notepad_parent):
        super().__init__(notepad_parent)
        self.notepad_parent = notepad_parent

        for i in range (3):
            self.rowconfigure(i,weight=1)

        for i in range(2):
            self.columnconfigure(i,weight=1)

        self.title = tk.Label(self,text= "Untitled")
        self.title.grid(row=0,column=0)

        self.text_box= tk.Text(self,width= 50, height= 35)
        self.text_box.grid(row=1,column=0)

        self.exit_button = tk.Button(self,text="Save and exit",command = self.exit_notepad ,borderwidth=3)
        self.exit_button.grid(row=0,column=1)

        self.grid(row=0,column=0)


    def exit_notepad(self):
        print("exiting notepads")
        self.notepad_parent.notepad_frame.destroy()
        self.notepad_parent.notepad_frame= notepad_init_frame(self.notepad_parent)

class notepad_select_frame(tk.Frame):
    def __init__(self,notepad_parent):
        super().__init__(notepad_parent)
        self.notepad_parent = notepad_parent

        self.columnconfigure (1,weight=1)
        for i in range(8):
            self.rowconfigure (i,weight=1)

        self.notepad_select_title = tk.Label(self,text= "Select the page you want to edit")
        self.notepad_select_title.grid(row=0,column=0)
        
        for i in range(5):
            self.notepad_i = tk.Button(self,text = f" Example page {i}", command = self.open_new_notepad)
            self.notepad_i.grid(row=i+2 ,column=0)

        self.exit_button = tk.Button(self,text="Back",command= self.exit_notepad)
        self.exit_button.grid(row=1,column=0)

        self.grid(row=0,column=0)

    def open_new_notepad(self):
        self.notepad_parent.notepad_frame.destroy()
        self.notepad_parent.notepad_frame= notepad_edit_frame(self.notepad_parent)    

    def exit_notepad(self):
        print("exiting notepads")
        self.notepad_parent.notepad_frame.destroy()
        self.notepad_parent.notepad_frame= notepad_init_frame(self.notepad_parent)


class calender_module(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("calender Module")
        self.geometry ("1100x700")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        self.calender_frame= calender_frame(self)
        self.calender_frame.grid(row=0,column=0)

class calender_frame(tk.Frame):
    def __init__(self,calender_parent):
        super().__init__(calender_parent)
        self.calender_parent = calender_parent

        for i in range(17):
            self.rowconfigure(i, weight=1)

        for y in range(9):
            self.columnconfigure(y, weight=1)

        for i in range(17):
            for y in range(8):
                self.time_slot=tk.Label(self,text= f"Event no {i+y}",relief="groove", borderwidth=3,height=10,width=9)
                self.time_slot.grid(row=i,column=y,padx=10, pady=3)

        self.add_event_button = tk.Button(self,text="Add an event", command= self.add_new_event)
        self.add_event_button.grid(row=16,column=9)

    def add_new_event(self):
        print("Adding new event")
        new_event_popup(self)

class new_event_popup(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Add new event")
        self.geometry ("300x400")

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        for i in range(7):
            self.rowconfigure(i, weight=1)

        self.event_title_title = tk.Label(self,text="Title of event")
        self.event_title_title.grid(column=0,row=0)

        self.event_title_input = tk.Entry(self)
        self.event_title_input.grid(row=1,column=0,columnspan=1)

        self.time_block_label = tk.Label(self,text="select time block")
        self.time_block_label.grid(column=0,row=2)

        self.time_block_input = tk.Entry(self)
        self.time_block_input.grid(column=0,row=3)

        self.save_event = tk.Button(self,text="finish and save",command = self.save_event)
        self.save_event.grid(row=4, column= 0)

    def save_event(self):
        print("Saving event")
        self.destroy()
        



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

        self.exit_td = tk.Button (self,text="Exit", borderwidth= 2, relief= "solid",command = self.exit_to_do)
        self.exit_td.grid(row=2,column=0, sticky= "w", padx= 30, pady= 30)

    def exit_to_do(self):
        print (gv.to_do_list_open)
        gv.to_do_list_open = False
        self.destroy()


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