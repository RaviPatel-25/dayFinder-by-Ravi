from datetime import datetime
import tkinter
from tkinter import messagebox
from tkinter import*
class Calender:
    def __init__(self,root):
        self.root=root
        self.root.title("Calender Question")
        self.root.geometry("1020x2000+0+0")
        self.root.resizable(False,False)
        self.root.configure(bg='indigo')
        
        self.label=Label(self.root,text="● DAY FINDER ●",font=("freesansbold",15,"bold")).place(x=150,y=100)
        self.label=Label(self.root,text="Enter date........☆touch here to enter date",font=("freesansbold",5,"bold")).place(x=150,y=310)
        
        self.entdate=StringVar()
        
        self.entry=Entry(self.root,textvariable=self.entdate,bd=10,bg='#00ff00').place(x=150,y=350,height=100,width=700)
        
        self.btn=Button(self.root,text="Next",bd=10,bg="aqua",command=self.find).place(x=300,y=600,height=110,width=365)
        
        
    def find(self):
        try:
        	date=self.entdate.get()
        	days_name=["......Monday",".....Tuesday","Wednesday","....Thursday",".........Friday","....Saturday",".......Sunday"]
        	day=datetime.strptime(date,"%d %m %Y").weekday()
        	self.label=Label(self.root,text='》》 The day is...............'+days_name[day],font=("freesansbold",8,"bold")).place(x=150,y=850)
        except Exception:
        	messagebox.showinfo("Info","Enter date as dd mm yyyy")
        

root=Tk()
obj=Calender(root)
root.mainloop()
	