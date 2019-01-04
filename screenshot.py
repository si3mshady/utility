import pyautogui as niceShot 
import tkinter as tk 
from tkinter import ttk 


class Mainframe(ttk.Frame):
    def __init__(self,root_window):
        ttk.Frame.__init__(self,root_window,padding="10 10 10 10")
        self.root_window = root_window
        self.filename = tk.StringVar()		 #create StringVar objects to hold user entered data 
        self.makeLabel()

    def makeLabel(self):
        self.pack()  #required to populate frame with lables and entry objects
        ttk.Label(self,text="Save file as:").grid(column=0,row=0,sticky=tk.E)
        ttk.Entry(self,width=25,textvariable=self.filename).grid(column=1,row=0)
        self.makeButtons()
        
        
    def makeButtons(self):
        bframe = ttk.Frame(self)
        bframe.grid(column=0,row=4,columnspan=2,sticky=tk.E)
        ttk.Button(bframe,text="Oh,Snap!",command=self.shooter).grid(column=0,row=0, padx=5)
        ttk.Button(bframe,text="Exit Program",command=self.root_window.destroy).grid(column=1, row=0)    
    


    def shooter(self): #retrieves the ttk user entered value for file name
        self.shot = niceShot.screenshot(str(self.filename.get())) #retrieve the 
      #  self.gui_button = tk.Button(mainframe, text='Oh,Snap!',command=shooter)
      #  self.gui_button.place(x=25,y=25)


if __name__=="__main__":
    mainframe  = tk.Tk()
    mainframe.title("Nice [[Screen]] Shot!")
    Mainframe(mainframe)
    mainframe.mainloop()

#Implementing ideas + code reuse, using tkinter and pyautogui to make a small screenshot application on my birthday 1-3-2019    Elliott Arnold 
