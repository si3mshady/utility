import requests,shelve
import tkinter as tk 
from tkinter import ttk 
from weather_data import Brick_Tamland

class Mainframe(ttk.Frame):
    def __init__(self,root_window):
        ttk.Frame.__init__(self,root_window,padding="10 10 10 10")
        self.root_window = root_window       
        self.city = tk.StringVar()
        self.condition = tk.StringVar()
        self.celcius = tk.StringVar()
        self.farenheit = tk.StringVar()       
        self.mel()
            
    def mel(self):
        self.pack()
        ttk.Label(self,text="City:").grid(column=0,row=0,sticky=tk.W)
        ttk.Entry(self,width=25,textvariable=self.city).grid(column=1,row=0)
        ttk.Label(self,text="Current Farenheit:").grid(column=0,row=1,sticky=tk.W)
        ttk.Label(self,width=25,textvariable=self.farenheit).grid(column=1,row=1)
        ttk.Label(self,text="Current Celcius:").grid(column=0,row=2,sticky=tk.W)
        ttk.Label(self,width=25,textvariable=self.celcius).grid(column=1,row=2)
        ttk.Label(self,text="Current Condition:").grid(column=0,row=3,sticky=tk.W)
        ttk.Label(self,width=25,textvariable=self.condition).grid(column=1,row=3)
        self.makeButtons()    

    def makeButtons(self):
        bframe = ttk.Frame(self)
        bframe.grid(column=0,row=4,columnspan=2,sticky=tk.E)
        ttk.Button(bframe,text="Get Weather Data",command=self.fetch_weather_data).grid(column=0,row=5, padx=5)
        ttk.Button(bframe,text="Exit Program",command=self.root_window.destroy).grid(column=0, row=6)

    def fetch_weather_data(self):        
        self.cuidad = self.city.get()
        self.weather_man = Brick_Tamland(self.cuidad)
        self.currently = self.weather_man.weather_report
        self.condition_result = self.currently['current']['condition']['text']
        self.celcius_result = self.currently['current']['feelslike_c']
        self.farenheit_result  = self.currently['current']['feelslike_f']  
        self.farenheit.set(self.farenheit_result)
        self.celcius.set(self.celcius_result)
        self.condition.set(self.condition_result)

if __name__=="__main__":
	root_window = tk.Tk()
	root_window.title("Brick Tamland GU3")
	Mainframe(root_window)
	root_window.mainloop()


#python3 tkinter practice. Brick Tamland weather data script modified with GUI   1-19-19