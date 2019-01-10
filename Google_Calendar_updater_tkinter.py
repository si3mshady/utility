import tkinter as tk
from gcp_auth import MAKE_GCP_SVC as mgs
import datetime 
global secret, scope, service, version 
scope = "https://www.googleapis.com/auth/calendar"
secret = "/Users/si3mshady/Documents/credentials.json"
service = 'calendar'
version = 'v3'
svc_gcp  = mgs(scope,secret,service,version)   

def set_google_calendar(start_year,end_year,start_month,end_month,start_day,end_day,start_hour,end_hour,start_minute,end_minute,start_seconds,end_seconds,description):
   start = datetime.datetime(start_year,start_month,start_day,start_hour,start_minute,start_seconds).isoformat()
   end = datetime.datetime(end_year,end_month,end_day,end_hour,end_minute,end_seconds).isoformat()
   desc  = description
   event = {'description':desc,'start':{'dateTime': start, 'timeZone': 'America/Chicago' },'end':{'dateTime': end, 'timeZone':'America/Chicago'}}
   event = svc_gcp.SVC.events().insert(calendarId='primary', body=event).execute()   

def start():      
    set_google_calendar(int(tkS1.get()),int(tkS2.get()),int(tkS3.get()),int(tkS4.get()),int(tkS5.get()),int(tkS6.get()),int(tkS7.get()),
    int(tkS8.get()),int(tkS9.get()),int(tkS10.get()),int(tkS11.get()),int(tkS12.get()),str(tkS13.get()))

root = tk.Tk()
root.title("Set Google Calendar")
frame = tk.Frame(root)
frame.config(bg='white')
frame.grid()

tkS1 = tk.StringVar()
label1 = tk.Label(frame,text="Start Year").grid(row=0,column=0,sticky='W') 
entry1 = tk.Entry(frame,textvariable=tkS1).grid(row=0,column=1) 
tkS2 = tk.StringVar()
label2 = tk.Label(frame,text="End Year").grid(row=0,column=2,sticky='W')
entry2 = tk.Entry(frame,textvariable=tkS2).grid(row=0,column=3)
tkS3 = tk.StringVar()
label3 = tk.Label(frame,text="Start Month").grid(row=1,column=0,sticky='W')
entry3 = tk.Entry(frame,textvariable=tkS3).grid(row=1,column=1)
tkS4 = tk.StringVar()
label4 = tk.Label(frame,text="End Month").grid(row=1,column=2,sticky='W')
entry4 = tk.Entry(frame,textvariable=tkS4).grid(row=1,column=3)
tkS5 = tk.StringVar()
label5 = tk.Label(frame,text="Start Day").grid(row=2,column=0,sticky='W')
entry5 = tk.Entry(frame,textvariable=tkS5).grid(row=2,column=1)
tkS6 = tk.StringVar()
label6 = tk.Label(frame,text="End Day").grid(row=2,column=2,sticky='W')
entry6 = tk.Entry(frame,textvariable=tkS6).grid(row=2,column=3)
tkS7 = tk.StringVar()
label7 = tk.Label(frame,text="Start Hour").grid(row=3,column=0,sticky='W')
entry7 = tk.Entry(frame,textvariable=tkS7).grid(row=3,column=1)
tkS8 = tk.StringVar()
label8 = tk.Label(frame,text="End Hour").grid(row=3,column=2,sticky='W')
entry8 = tk.Entry(frame,textvariable=tkS8).grid(row=3,column=3)
tkS9 = tk.StringVar()
label9 = tk.Label(frame,text="Start Min").grid(row=4,column=0,sticky='W')
entry9 = tk.Entry(frame,textvariable=tkS9).grid(row=4,column=1)
tkS10 = tk.StringVar()
label10 = tk.Label(frame,text="End Min").grid(row=4,column=2,sticky='W')
entry10 = tk.Entry(frame,textvariable=tkS10).grid(row=4,column=3)
tkS11 = tk.StringVar()
label11 = tk.Label(frame,text="Start Seconds").grid(row=5,column=0,sticky='W')
entry12 = tk.Entry(frame,textvariable=tkS11).grid(row=5,column=1)
tkS12 = tk.StringVar()
label12 = tk.Label(frame,text="End Seconds").grid(row=5,column=2,sticky='W')
entry12 = tk.Entry(frame,textvariable=tkS12).grid(row=5,column=3)
tkS13 = tk.StringVar()
label13 = tk.Label(frame,text="Description").grid(row=6,column=0,sticky='W')
entry13 = tk.Entry(frame,textvariable=tkS13).grid(row=6,column=1)
button = tk.Button(frame,text="Set Calendar", command=start,fg="blue").grid(row=7,column=3)

root.mainloop()

#1-10-19 Created a time management tool for inserting events into Google Calendar.  Elliott Arnold  = Si3mshady