from tkinter import *
import tkinter as tk
from tkinter import ttk
import frame_template as ft
import global_variables as gv
gv.index = None
import os

add_item_open = False


    
#The Toplevel that the flashcard frame is placed into, no data in it originally

class flashcard_module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.title("Flashcard Module")
        self.geometry ("900x600")

        self.rowconfigure(0,weight=1)

        self.columnconfigure(0,weight=1)

        self.flashcard_frame= flashcard_select_frame(self)
        self.flashcard_frame.grid(row=0,column=0)
        
#The first flashcard frame that allows the user to select which mode they want      
class flashcard_select_frame(tk.Frame):
        def __init__(self,flashcard_parent):
            super().__init__(flashcard_parent)
            self.flashcard_parent = flashcard_parent
            

            self.rowconfigure(0,weight=1)
            self.rowconfigure(1,weight=1)

            self.columnconfigure(0,weight=1)
            self.columnconfigure(1,weight=1)
            self.columnconfigure(2,weight=1)

            self.edit_flashcards_btn = tk.Button(self,text="Edit Flashcards",command= self.edit_flashcards)
            self.edit_flashcards_btn.grid(row=0,column=0)
            self.open_flashcards_btn = tk.Button(self,text="open Flashcards",command= self.open_flashcards_folder)
            self.open_flashcards_btn.grid(row=0,column=1)

            self.exit_flashcards_btn = tk.Button(self,text="Exit",command=self.exit_flashcards_whole)
            self.exit_flashcards_btn.grid(row=2,column=3)


        def open_flashcards_folder(self):
            #opnes the frame to allow the user to select which flashcards to revise from
            print("opening flashcards folder")
            self.flashcard_parent.flashcard_frame.destroy()
            self.flashcard_parent.flashcard_frame= flashcard_files_frame(self.flashcard_parent)

        def edit_flashcards(self):
            #opens the frame to allow the user to create flashcards
            self.flashcard_parent.flashcard_frame.destroy()
            self.flashcard_parent.flashcard_frame = flashcard_edit_frame(self.flashcard_parent)

        def exit_flashcards_whole(self):
            #closes the flashcard frame
            gv.flashcard_open = False
            self.flashcard_parent.destroy()

class flashcard_files_frame(tk.Frame):
        #the frame to allow the user to use the flashcards
        def __init__(self,flashcard_parent):
            super().__init__(flashcard_parent)
            self.flashcard_parent = flashcard_parent

            self.rowconfigure(0,weight=1)
            for i in range(5):
                self.columnconfigure(i,weight=1)

            self.select_flashcards_label=tk.Label(self,text="Select Flashcards")
            self.select_flashcards_label.grid(row=0,column=0)

            flashcards_list = os.listdir("storage/Flashcards")
            for i in range(len(flashcards_list)):
               
                self.flashcard_label = tk.Button(self,text = str(i) + "." + str(flashcards_list[i]), command = lambda i=i:self.open_flashcards(i)) # open flashcards function is passed with the index
                self.flashcard_label.grid(row=i+1,column=0)

            self.grid(row=0,column=0)

        def open_flashcards(self,index):
            #opens the flashcards that the user selected, passing in the index and changing the gv.flashcard_index variable to be the index so the program can refrence it later
            gv.flashcard_index = index
            print("opening flashcards")
            self.flashcard_parent.flashcard_frame.destroy()
            self.flashcard_parent.flashcard_frame= flashcard_frame(self.flashcard_parent)
        
        
class flashcard_frame(tk.Frame):
        #the frame that the user will actually revise from
        def __init__(self,flashcard_parent):
            super().__init__(flashcard_parent)
            self.flashcard_parent = flashcard_parent
            self.questions = []
            self.answers = []        

            gv.flashcard_no = 0

            for i in range(3):
                self.columnconfigure(i,weight=1)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=1)
            self.rowconfigure(2,weight=1)

            #reads the flashcards folder and creates a button for each item, passing in the integer when the program is run 
            flashcards_list = os.listdir("storage/Flashcards")
            with open (f"storage/Flashcards/{flashcards_list[ gv.flashcard_index]}") as f:
                print("reading")
                flashcard_data = f.read()
                flashcard_data = flashcard_data.split('\n')

                for v in range(len(flashcard_data)):
                    print (v)
                    if v % 2 ==0:
                        self.questions.append(flashcard_data[v])
                    else:
                        self.answers.append(flashcard_data[v])
                
                print(self.questions)
                print(self.answers)


            flashcard_no = 0
            answer_revealed = False
            
            self.flashcard_label = tk.Label(self,text=self.questions[0],borderwidth=3, relief="groove",width= 50,height=10,font=("Arial", 15))
            self.flashcard_label.grid(row=0,column=1)

            self.pre_button = tk.Button(self,text= "<", relief="groove",width= 13,height=5,font=("Arial", 10),command = self.previous_flashcard)
            self.pre_button.grid(row=0,column=0)

            self.next_button = tk.Button(self,text= ">", relief="groove",width= 13,height=5,font=("Arial", 10),command= self.next_flashcard)
            self.next_button.grid(row=0,column=3)

            self.flashcard_exit = tk.Button(self,text="Exit",relief="groove", command = self.exit_flashcards)
            self.flashcard_exit.grid(row=2,column=1)

            self.flashcard_flip = tk.Button(self,text = "Flip", relief="groove",width= 10, height=3, padx=20, pady= 20,command= self.flip)
            self.flashcard_flip.grid(row=1,column=1)

            self.flashcard_counter = tk.Label(self,text = f"1/{len(self.questions)}",relief ="groove")
            self.flashcard_counter.grid(row=2,column=3)



            self.grid(row=0,column=0)
        
        def exit_flashcards(self):
            #closes the flashcards module
            print (gv.flashcard_open)
            gv.flashcard_open = False
            self.flashcard_parent.destroy()

        def next_flashcard(self):
            # Changes the flashcard to show the next flashcard
            if len(self.questions) == (gv.flashcard_no + 1):
                print("thats the end buckeroo")
                if gv.flashcard_end_open == False:
                    gv.flashcard_end_open = True
                    flashcard_end(self)

            else:
                gv.flashcard_no += 1
                self.flashcard_label.config(text = self.questions[gv.flashcard_no])
                self.flashcard_counter.config(text=f"{gv.flashcard_no+1}/{len(self.questions)}")
                gv.flshcrd_revealed = False

        def previous_flashcard(self):
            # Changes the flashcard to show the previous flashcard
            if gv.flashcard_no <= 0:
                print("Cant go that way bud")
            else:
                gv.flashcard_no -= 1
                self.flashcard_label.config(text = self.questions[gv.flashcard_no])
                self.flashcard_counter.config(text=f"{gv.flashcard_no+1}/{len(self.questions)}")
                gv.flshcrd_revealed = False

        def flip(self):
            #Changes the question frame to show either the question or the answer depending on what was there before.
            if gv.flshcrd_revealed == False:
                self.flashcard_label.config(text = self.answers[gv.flashcard_no])
                print("flip")
                gv.flshcrd_revealed = True
            elif gv.flshcrd_revealed == True:
                self.flashcard_label.config(text = self.questions[gv.flashcard_no])
                gv.flshcrd_revealed = False


class flashcard_end(tk.Toplevel):
    # the toplevel that appears when the user has reached the end of their flashcard set
    def __init__(self,parent):
        super().__init__(parent)
        self.parent= parent
        self.geometry("300x200")
        self.title("")


        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)

        self.top_label = tk.Label(self,text = "You've finished this set of flashcards",relief="groove")
        self.top_label.grid(row=0,column=0)

        self.exit = tk.Button(self,text = "Exit",command = self.exit_top, relief= "solid")
        self.exit.grid(row=1,column=0)

    def exit_top(self):
        #closes the toplevel
        gv.flashcard_end_open = False
        flashcard_end.destory()



class flashcard_edit_frame(tk.Frame):
        #the frame that allows the user to create new flashcards
        def __init__(self,flashcard_parent):
            super().__init__(flashcard_parent)
            self.flashcard_parent = flashcard_parent

            self.columnconfigure(0,weight=1)
            self.columnconfigure(1,weight=1)

            self.flashcard_counter_no = 1

            for i in range(8):
                self.rowconfigure(i,weight=1)

            self.flshcard_edit_title = tk.Label(self,text= "Input Flashcard Title")
            self.flshcard_edit_title.grid(row=0,column=0,columnspan=2)

            self.flashcard_counter= tk.Label(self,text=str(self.flashcard_counter_no),relief= "groove")
            self.flashcard_counter.grid(row=0,column=2)
            
            self.flshcrd_title_input = tk.Entry(self)     
            self.flshcrd_title_input.grid(row=1,column=0,columnspan=2)       
            
            self.flashcard_question_label = tk.Label(self,text="Flashcard Question")
            self.flashcard_question_label.grid(row=3,column=0)
            
            self.flashcard_answer_label = tk.Label(self,text="Flashcard Answer")
            self.flashcard_answer_label.grid(row=3,column=1)

            self.flashcard_question = tk.Text(self,height=10,width=25)
            self.flashcard_question.grid(row=4,column=0)
            
            self.flashcard_answer = tk.Text(self,height=10,width=25)
            self.flashcard_answer.grid(row=4,column=1)

            self.new_flashcard_button = tk.Button(self,text="+",relief="groove",command= self.add_new_flashcard)
            self.new_flashcard_button.grid(row=5,column=0,columnspan=2)

            self.exit_flashcard_edit = tk.Button(self,text="Save and exit", command= self.exit_flashcard_edit)
            self.exit_flashcard_edit.grid(row=6,column=2)


            self.grid(row=0,column=0)
            

        def exit_flashcard_edit(self):
            print("Saving event")
            gv.flashcard_open = False
            self.flashcard_parent.destroy()

        def add_new_flashcard(self):
            #saves the title, question and answer of the flashcards and then clears the question and answer sections
            title = self.flshcrd_title_input.get()
            flashcard_question = self.flashcard_question.get("1.0","end-1c")
            flashcard_answer = self.flashcard_answer.get("1.0","end-1c")
            flashcard_list = os.listdir("storage/Flashcards")


            with open (f"storage/Flashcards/{title}","a") as f:
                f.write(flashcard_question+ "\n"+flashcard_answer + "\n")

            self.flashcard_counter_no += 1
            self.flashcard_counter.config(text = str(self.flashcard_counter_no))

            self.flashcard_question.delete('1.0',"end-1c")
            self.flashcard_answer.delete('1.0',"end-1c")








class notepad_module(tk.Toplevel):
    #The toplevel frame for the notepad module
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
    #the frame which allows the user to select which notepad mode they want to open
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

        self.exit_flashcards_btn = tk.Button(self,text="Exit",command=self.exit_notepad_whole)
        self.exit_flashcards_btn.grid(row=2,column=3)

        self.grid(row=0,column=0)

    def open_new_notepad(self):
        print ("opening new notepad")
        self.notepad_parent.notepad_frame.destroy()
        self.notepad_parent.notepad_frame= notepad_edit_frame(self.notepad_parent)

    def select_new_notepad(self):
        print("Selecting a new notepad")
        gv.index = None
        self.notepad_parent.notepad_frame.destroy()
        self.notepad_parent.notepad_frame= notepad_select_frame(self.notepad_parent)

    def exit_notepad_whole(self):
        gv.notepad_open = False
        self.notepad_parent.destroy()

class notepad_edit_frame(tk.Frame):
    #the frame that lets the user create/ edit a notepad 
    def __init__(self,notepad_parent,var = "untitled",notevar=""):
        super().__init__(notepad_parent)
        self.notepad_parent = notepad_parent
        self.var = var
        self.notevar = notevar

        for i in range (3):
            self.rowconfigure(i,weight=1)

        for i in range(2):
            self.columnconfigure(i,weight=1)


        if gv.index == None:
            self.var =tk.StringVar(value= "Untitled")
            self.title = tk.Entry(self,textvariable=self.var)
            self.title.grid(row=0,column=0)

            self.text_box= tk.Text(self,width= 50, height= 35)
            self.text_box.grid(row=1,column=0)

            self.exit_button = tk.Button(self,text="Save and exit",command = self.exit_notepad ,borderwidth=3)
            self.exit_button.grid(row=0,column=1)
        else:
            files=os.listdir("storage/Notepad")
            self.var =tk.StringVar(value= files[gv.index])
            
            self.title = tk.Entry(self,textvariable=self.var)
            self.title.grid(row=0,column=0)


            self.text_box= tk.Text(self,width= 50, height= 35)
            self.text_box.grid(row=1,column=0)

            with open (f"storage/Notepad/{files[gv.index]}","r") as f:
                notes_text = f.read()

            
            print (notes_text)
            self.text_box.insert('1.0',notes_text)

            self.exit_button = tk.Button(self,text="Save and exit",command = self.exit_notepad ,borderwidth=3)
            self.exit_button.grid(row=0,column=1)

        self.grid(row=0,column=0)


    def exit_notepad(self):
        print("exiting notepads")
        new_notepad = self.text_box.get("1.0","end-1c")
        print (new_notepad)
        new_notepad_title = self.title.get()#"1.0","end-1c")
        print(new_notepad_title)

        gv.index = None
        #save new_notepad_title & new_notepad data
        if new_notepad != "":
            with open( f"storage/Notepad/{new_notepad_title}","w" ) as f:
                f.write(new_notepad)
        else:
            print("exiting, nothing save")


        gv.index = None

        self.notepad_parent.notepad_frame.destroy()
        self.notepad_parent.notepad_frame= notepad_init_frame(self.notepad_parent)

class notepad_select_frame(tk.Frame):
    #allows the user to select which notepad they want to open 
    def __init__(self,notepad_parent):
        super().__init__(notepad_parent)
        self.notepad_parent = notepad_parent

        self.columnconfigure (1,weight=1)
        for i in range(8):
            self.rowconfigure (i,weight=1)

        self.notepad_select_title = tk.Label(self,text= "Select the page you want to edit")
        self.notepad_select_title.grid(row=0,column=0)

        files = os.listdir("storage/Notepad")
        for i in range (len(files)):
            self.notepad = tk.Button(self, text =str(i)+ ". " + str(files[i]), command = lambda i=i:self.open_new_notepad(i))
            self.notepad.grid(row= i+2, column=0)
        
        # for i in range(5):
        #     self.notepad_i = tk.Button(self,text = f" Example page {i}", command = self.open_new_notepad)
        #     self.notepad_i.grid(row=i+2 ,column=0)

        # self.exit_button = tk.Button(self,text="Back",command= self.exit_notepad)
        # self.exit_button.grid(row=1,column=0)

        self.grid(row=0,column=0)

    def open_new_notepad(self,new_index):
        #the code to open a notepad that has already been created
        #the function name is misleading but its already coded and it works so its fine right now
        gv.index = new_index
        self.notepad_parent.notepad_frame.destroy()
        self.notepad_parent.notepad_frame= notepad_edit_frame(self.notepad_parent)
    def exit_notepad(self):
        print("exiting notepads")
        self.notepad_parent.notepad_frame.destroy()
        self.notepad_parent.notepad_frame= notepad_init_frame(self.notepad_parent)
        


class calender_module(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.title("calender Module")
        self.geometry ("1100x700")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        self.calender_frame= calender_frame(self)
        self.calender_frame.grid(row=0,column=0)

class calender_frame(tk.Frame):
    #the frame for the calendar
    def __init__(self,calender_parent):
        super().__init__(calender_parent)
        self.calender_parent = calender_parent

        #the count to determine which event no the program is on, so that there are no repeats
        count = 1

        event_list = os.listdir("storage/Cal")
        print (event_list)

        for i in range(0,20):
            self.rowconfigure(i, weight=1)

        for y in range(10):
            self.columnconfigure(y, weight=1)

        self.test_block =tk.Label(self,text= "test",bg="gray",width=10,height=10)
        self.test_block.grid(row=1,column=1)

        #places all the blocks that the events can be placed into
        for i in range(1,18):
            for y in range(7):
                self.time_slot=tk.Label(self,text= f"{count}",relief="groove", borderwidth=3,height=10,width=9)
                self.time_slot.grid(row=i+1,column=y+1,padx=10, pady=3)
                count += 1

        ##iterates through every file of an event and places them as labels on the calendar
        for event in event_list:
            with open (f"storage/Cal/{event}","r") as f:
                event_data = f.read()
            self.event_label= tk.Label(self,text=event_data,relief="groove", borderwidth=3,height=10,width=9,bg="white")
            div= divmod(int(event),7)
            event_row = div[0]+2
            event_column = div[1]
            if event_column == 0:
                event_column = 7
                event_row -= 1
            print(event_data,event_column, event_row)
            self.event_label.grid(row=event_row,column=event_column)
                        

        #Creates arrays for the time and days, and then places htem around the grid, allowing the user to see where they want to place an event
        hour_arr = ["7am","8am","9am","10am","11am","12am","1pm","2pm","3pm","4pm","5pm","6pm","7pm","8pm","9pm","10pm","11pm"]
        day_arr = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

        for i in range(17):
            self.time_label = tk.Label(self,text=hour_arr[i])
            self.time_label.grid(row=i+2,column=0)

        for i in range(7):
            self.day_label = tk.Label(self,text=day_arr[i])
            self.day_label.grid(row=1,column=i+1)

        self.add_event_button = tk.Button(self,text="Add an event", command= self.add_new_event)
        self.add_event_button.grid(row=17,column=10)

        self.exit_calendar_button = tk.Button(self,text="Exit calendar",command= self.exit_calendar)
        self.exit_calendar_button.grid(row=16,column=10)

        self.delete_event_button = tk.Button(self,text = "Delete event",command = self.delete_event)
        self.delete_event_button.grid(row=15,column=10)



    def add_new_event(self):    
        new_event_popup(self)

    def delete_event(self):
        delete_event_popup(self)

    def exit_calendar(self):
        gv.calender_open = False
        self.calender_parent.destroy()

    def refresh(self):
        self.destroy
        self.__init__

    #The popup that allows the user to decide on which events they want to delete
class delete_event_popup(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.title = ("delete_event")
        self.geometry("300x500")

        self.rowconfigure(1,weight=1)
        self.columnconfigure(1,weight=1)

        event_frame = tk.Frame(self,border=2,borderwidth=2,relief='groove')
        event_frame.grid(row=1,column=1,sticky='nsew',padx=25,pady=25)

        events = os.listdir("storage/Cal")
        print(events)

        for i in range(len(events)):
            event_frame.rowconfigure(i,weight=1)

        event_frame.columnconfigure(1,weight = 1)

        for y in range(len(events)):
            with open (f"storage/Cal/{events[y]}","r") as f:
                event_data = f.read()
            event_button = tk.Button(event_frame,text=events[y]+"-"+ event_data,command = lambda y=y: self.delete_event_item(y))
            event_button.grid(row=y+1,column=1,pady=5)

    def delete_event_item(self,index):
        gv.event_index = index
        print(index)
        os.remove(f"storage/Cal/{str(index)}")
        self.destroy()
        self.parent.refresh()

    #the popup that allows the user to create a new event
class new_event_popup(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
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

        hour_arr = ["7am","8am","9am","10am","11am","12am","1pm","2pm","3pm","4pm","5pm","6pm","7pm","8pm","9pm","10pm","11pm"]
        day_arr = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

        self.day_select = ttk.Combobox(self,values=day_arr)
        self.day_select.set ("Select a day")
        self.day_select.grid(column=0, row=2)

        self.hour_select = ttk.Combobox(self,values=hour_arr)
        self.hour_select.set ("Select an hour")
        self.hour_select.grid(column=0, row=3)

        self.save_event = tk.Button(self,text="finish and save",command = self.save_event)
        self.save_event.grid(row=4, column= 0)

    def save_event(self, *arg):
        
        #Saves the event as a file with the event placement as the name, allowing it to be placed when the file is loaded
        hour_arr = ["7am","8am","9am","10am","11am","12am","1pm","2pm","3pm","4pm","5pm","6pm","7pm","8pm","9pm","10pm","11pm"]
        day_arr = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

        print (f"the value is at {str(self.hour_select.current())}")
        hour_selection = self.hour_select.current()
        day_selection = self.day_select.current()

        if hour_selection == None or day_selection == None:
            print ("fil lin please")
            return
        else:

            print (f"the value is {hour_arr[hour_selection]}")
            print (f"the value is the day {day_arr[day_selection]}")
            
            am7 = [1,2,3,4,5,6,7]
            am8 = [8,9,10,11,12,13,14]
            am9 = [15,16,17,18,19,20,21]
            am10 = [22,23,24,25,26,27,28]
            am11 = [29,30,31,32,33,34,35]
            pm12 = [36,37,38,39,40,41,42]
            pm1 = [43,44,45,46,47,48,49]
            pm2 = [50,51,52,53,54,55,56]
            pm3 = [57,58,59,60,61,62,63]
            pm4 = [64,65,66,67,68,69,70]
            pm5 = [71,72,73,74,75,76,77]
            pm6 = [78,79,80,81,82,83,84]
            pm7 = [85,86,87,88,89,90,91]
            pm8 = [92,93,94,95,96,97,98]
            pm9 = [99,100,101,102,103,104,105]
            pm10 = [106,106,108,109,110,111,112]
            pm11 = [113,114,115,116,117,118,119]

            times_arr = [am7,am8,am9,am10,am11,pm12,pm1,pm2,pm3,pm4,pm5,pm6,pm7,pm8,pm9,pm10,pm11]

            if hour_selection == 0:
                event_time = str(am7[day_selection])
            elif hour_selection == 1:
                event_time = str(am8[day_selection])
            elif hour_selection == 2:
                event_time = str(am9[day_selection])
            elif hour_selection == 3:
                event_time = str(am10[day_selection])
            elif hour_selection == 4:
                event_time = str(am11[day_selection])
            elif hour_selection == 5:
                event_time = str(pm12[day_selection])
            elif hour_selection == 6:
                event_time = str(pm1[day_selection])
            elif hour_selection == 7:
                event_time = str(pm2[day_selection])
            elif hour_selection == 8:
                event_time = str(pm3[day_selection])
            elif hour_selection == 9:
                event_time = str(pm4[day_selection])
            elif hour_selection == 10:
                event_time = str(pm5[day_selection])
            elif hour_selection == 11:
                event_time = str(pm6[day_selection])
            elif hour_selection == 12:
                event_time = str(pm7[day_selection])
            elif hour_selection == 13:
                event_time = str(pm8[day_selection])
            elif hour_selection == 14:
                event_time = str(pm9[day_selection])
            elif hour_selection == 15:
                event_time = str(pm10[day_selection])
            elif hour_selection == 16:
                event_time = str(pm10[day_selection])
            
            print("Saving event")
            event_data = self.event_title_input.get()
            print(event_time)
            with open (f"storage/Cal/{event_time}","w") as f:
                f.write(event_data)
            self.refresh_parent()
            self.destroy()

    def refresh_parent(self,):
        self.parent.refresh()
        



class to_do_list_module(tk.Toplevel):
    #the toplevel for the to do module, doesnt make use of a frame even though the others do
    def __init__(self,master=None):
        super().__init__(master)
        self.title("To do list Module")
        self.geometry ("1000x700")

        for i in range (2):
            self.columnconfigure(i,weight=1)
        for i in range (2):
            self.rowconfigure(0, weight=1)
        # 3 columns, 2 rows

        td_files = os.listdir("storage/To_do_list")
        gv.curr_td_items = len(td_files)
        print (gv.curr_td_items)

        #Procedures that open the new toplevel allowing the user to add an item
        self.add_td_item_btn = tk.Button (self,text="Add an item",borderwidth=3, relief = "solid", command= lambda: add_item(self))
        self.add_td_item_btn.grid(row=0, column=0, sticky="new", padx= 30, pady= 30)

        self.remove_td_btn = tk.Button (self,text="Remove bottom item",borderwidth=3, relief= "solid", command = self.remove_bottom_td)
        self.remove_td_btn.grid(row=0, column=1, sticky="new", padx= 30, pady= 30)
        #function that closes the toplevel
        self.exit_td = tk.Button (self,text="Exit", borderwidth= 2, relief= "solid",command = self.exit_to_do)
        self.exit_td.grid(row=2,column=0, sticky= "w", padx= 30, pady= 30)


        self.list_frame = tk.Frame(self,borderwidth=1)
        self.list_frame.grid(row=0,column=0,columnspan=2,rowspan=2,padx=20, pady=3,sticky="ew")
        
        self.list_frame.columnconfigure(0,weight=1)
        self.list_frame.columnconfigure(1,weight=1)
        for i in range (100):
            self.list_frame.rowconfigure(i,weight=1)

        td_files = os.listdir("storage/To_do_list")
        td_count = 0
        for i in td_files:
            with open( f"storage/To_do_list/{i}","r" ) as f:
                td_item_text = f.read()
                self.td_item = tk.Label(self.list_frame, text= td_item_text,relief= 'raised', borderwidth= 1,width=250,padx=10,pady= 50)
                self.td_item.grid(row=td_count,column=0,columnspan=2)
                td_count +=1
        

    def refresh(self):
        to_do_list_module.destroy(self)
        to_do_list_module.__init__(self)

    def exit_to_do(self):
        print (gv.to_do_list_open)
        gv.to_do_list_open = False
        self.destroy()

    def exit_add_item(self):
        gv.add_td_item = False
        print("destorying")
        self.destroy()

    def save_td_item(self):
        td_item_save = self.item_input.get("1.0","end-1c")
        print(td_item_save)
        gv.curr_td_items += 1
        with open(f"storage/To_do_list{gv.curr_td_items}","w") as f:
            f.write(td_item_save)
        gv.add_td_item = False
        self.destroy()
        self.refresh()

    def remove_bottom_td(self):
        td_files = os.listdir("storage/To_do_list")
        os.remove(f"storage/To_do_list/{td_files[gv.curr_td_items-1]}")
        gv.curr_td_items -= 1
        self.refresh()

def add_item(self):
    if gv.add_td_item == True:
        print("Cannot open, already open")
    else:
        gv.add_td_item = True
        add_item_module(self)




class add_item_module(tk.Toplevel):
    #the modlue that allows the user to add a new item
    def __init__(self,master=None):
        super().__init__(master)
        self.title("Add an item")
        self.geometry ("300x250")
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)

        for i in range(2):
            self.rowconfigure(i,weight=1)

        self.add_item_button = tk.Button (self,text="Add item",borderwidth=3, relief= "solid",command= lambda: save_td_item(self))
        self.add_item_button.grid(row=2,column=1,padx=3,pady=3)

        self.item_input = tk.Text (self,borderwidth=3, relief= "solid")
        self.item_input.grid(row=1,column=0,columnspan=2)

        self.exit_td_add = tk.Button(self,text="Exit",borderwidth=3, relief= "solid", command = lambda: exit_add_item(self))
        self.exit_td_add.grid(row=2,column=0,padx=3,pady=3)

def exit_add_item(self):
    gv.add_td_item = False
    print("destorying")
    self.destroy()

def save_td_item(self):
    td_item_save = self.item_input.get("1.0","end-1c")
    print(td_item_save)
    gv.curr_td_items += 1
    with open(f"storage/To_do_list/{gv.curr_td_items}","w") as f:
        f.write(td_item_save)
    gv.add_td_item = False

    to_do_list_module.destroy(self)
    to_do_list_module.__init__(self)
    self.destroy()