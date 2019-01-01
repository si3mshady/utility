import tkinter as tk 
from tkinter import ttk 

#create BMR object - business 
class BMR():
	def __init__(self):
		self.age = 0
		self.weight = 0
		self.height = 0

	def getBMR(self):
		bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
		return bmr 

#frame constructor; class Mainframe is a subclass of ttk.Frame - presentation  
class Mainframe(ttk.Frame):
	def __init__(self,root_window):
		ttk.Frame.__init__(self,root_window,padding="10 10 10 10")		
		self.root_window = root_window
		self.bmr = BMR()
		#create StringVar objects to hold user entered data 
		self.age = tk.StringVar()
		self.weight = tk.StringVar()
		self.height = tk.StringVar()
		self.result = tk.StringVar()
		self.mel()

#make entries and lables  
	def mel(self):
		self.pack()
		ttk.Label(self,text="Age:").grid(column=0,row=0,sticky=tk.E)
		ttk.Entry(self,width=25,textvariable=self.age).grid(column=1,row=0)

		ttk.Label(self,text="Weight:").grid(column=0,row=1,sticky=tk.E)
		ttk.Entry(self,width=25,textvariable=self.weight).grid(column=1,row=1)

		ttk.Label(self,text="Height(inches):").grid(column=0,row=2,sticky=tk.E)
		ttk.Entry(self,width=25,textvariable=self.height).grid(column=1,row=2)

		ttk.Label(self,text="BMR:").grid(column=0,row=3,sticky=tk.E)
		ttk.Entry(self,width=25,textvariable=self.result).grid(column=1,row=3)
		self.makeButtons()

	def makeButtons(self):
		bframe = ttk.Frame(self)
		bframe.grid(column=0,row=4,columnspan=2,sticky=tk.E)

		ttk.Button(bframe,text="Calculate BMR",command=self.bmrCalc).grid(column=0,row=0, padx=5)
		ttk.Button(bframe,text="Exit Program",command=self.root_window.destroy).grid(column=1, row=0)

	def bmrCalc(self):
		self.bmr.age = int(self.age.get())
		self.bmr.weight = int(self.weight.get())
		self.bmr.height = int(self.height.get())
		bmr = 66 + (6.23 * self.bmr.weight) + (12.7 * self.bmr.height) - (6.8 * self.bmr.age)
		self.result.set(str(bmr))


if __name__=="__main__":
	root_window = tk.Tk()
	root_window.title("BMR Calculator")
	Mainframe(root_window)
	root_window.mainloop()


#ch18 BMR Calculator Enhanced w/ GUI  - Learning Python 3 with Murach  Elliott Arnold  10-20-18   Finish what you start   

