#!/usr/bin/python3
import tkinter as tk
from functools import partial
from tkinter import messagebox
import NumPad as Numpad
import DBConnection as db
import CheckPersonel as cp
import datetime
class BaseFrame(tk.Frame):
	"""docstring for BaseFrame"""
	def __init__(self, master, controller):
		tk.Frame.__init__(self,master)
		self.controller = controller
		#self.grid()
		self.create_widgets()

	def create_widgets(self):
		raise NotImplementedError
 
class PageHome(BaseFrame):
	"""docstring for ExecuterFrame"""

	def OnEntryBtn(self):
		personelId = Numpad.NumPad("Personel Id").getValue() 
		password = Numpad.NumPad("Personel Password").getValue() 
		check = cp.CheckPersonel(personelId,password,1)
		result = check.CheckResult()
		if result:
			tk.messagebox.showinfo(title="Giriş",message=result[1])
		else:

			tk.messagebox.showerror(title="Hata",message="Personel Bulunamadı")

	def create_widgets(self):
		winW = self.winfo_screenwidth()
		winH = self.winfo_screenheight() 
		self.entryBtn = tk.Button(self, text="Şifreyle Giriş Yap", command=self.OnEntryBtn)
	 
		self.entryBtn.pack(side="right");

class PageSettings(BaseFrame):
	def session_control(self):
		self.pack_forget() 

	def create_widgets(self):

		con = db.DBConnection(Server="127.0.0.1",Database="terminal",Uid="phpmyadmin", Pwd="880739")
		rows = con.Select("info",["name","ip_address","netmask","gateway","server_ip"],{})

		winW = self.winfo_screenwidth()
		winH = self.winfo_screenheight() 
		container = tk.Frame(self,width=int(self.winfo_screenwidth())-81)
		container.grid(row=0,column=0, sticky="nw") 
		container.update()
		self.labelIpAddress = tk.Label(container, text=rows[0]["name"]).grid(row=0,column=0, ipadx=int(self.winfo_screenwidth()/4)-35)
		self.buttonIpAdress = tk.Button(container, text="Change").grid(row=0,column=1) 

		self.labelIpAddress = tk.Label(container, text=rows[0]["ip_address"]).grid(row=1,column=0, ipadx=int(self.winfo_screenwidth()/4)-35)
		self.buttonIpAdress = tk.Button(container, text="Change").grid(row=1,column=1) 

		self.labelIpAddress = tk.Label(container, text=rows[0]["netmask"]).grid(row=2,column=0, ipadx=int(self.winfo_screenwidth()/4)-35)
		self.buttonIpAdress = tk.Button(container, text="Change").grid(row=2,column=1) 

		self.labelIpAddress = tk.Label(container, text=rows[0]["gateway"]).grid(row=3,column=0, ipadx=int(self.winfo_screenwidth()/4)-35)
		self.buttonIpAdress = tk.Button(container, text="Change").grid(row=3,column=1) 

		self.labelIpAddress = tk.Label(container, text=rows[0]["server_ip"]).grid(row=4,column=0, ipadx=int(self.winfo_screenwidth()/4)-35)
		self.buttonIpAdress = tk.Button(container, text="Change").grid(row=4,column=1) 

class PythonGUI(tk.Tk):
	"""docstring for PythonGUI"""
	def __init__(self):
		tk.Tk.__init__(self)
		self.title = "PythonGUI"
		self.attributes("-fullscreen", True)
		self.create_widgets()
		#self.resizable(0,0)
		
		#frameMenu = tk.Frame(self, width=winW, height=60, borderwidth=2, relief=tk.RIDGE)
		#frameMenu.pack_propagate(False)
		#frameMenu.pack(side="top")

	def UpdateTimeLine(self):
		self.timeLine.configure(text = datetime.datetime.now().strftime("%H:%M:%S"))
		self.after(1000,self.UpdateTimeLine)
		

	def create_widgets(self):

		winW = self.winfo_screenwidth()
		winH = self.winfo_screenheight() 


		self.topBar = tk.Frame(self, width=winW, padx = 15, pady=15, height=100, borderwidth=2,bg="blue", relief=tk.RIDGE)
		self.topBar.pack_propagate(False)
		self.topBar.pack(side="top",fill="x")


		self.dateLine = tk.Label(self.topBar, padx=15, pady=15,text=datetime.datetime.now().strftime("%d %B %Y"),font=("Verdana",10),bg="blue",fg="white")
		self.dateLine.pack(side="left", fill="both")

		self.timeLine = tk.Label(self.topBar, padx=15, pady=15,text=datetime.datetime.now().strftime("%H:%M:%S"),font=("Verdana",45),bg="blue",fg="white")
		self.timeLine.pack(side="left", fill="both") 
		self.timeLine.after(1000,self.UpdateTimeLine)

		self.menuHome = tk.Button(self.topBar, padx = 15, pady=15, text="Home", command=lambda: self.showPage(PageHome))
		self.menuHome.pack(side="right", fill="both")
		self.menuSettings= tk.Button(self.topBar, padx = 15, pady=15, text="Settings", command=lambda: self.showPage(PageSettings))
		self.menuSettings.pack(side="right", fill="both")


		self.container = tk.Frame(self, width=winW, padx = 15, pady=15, height=winH, borderwidth=2, relief=tk.RIDGE)
		self.container.pack_propagate(False)
		self.container.pack(side="top", fill="both") 

		self.frames = {}

		for F in (PageHome,PageSettings):
			frame = F(self.container, self)
			frame.grid(row=0, column=0,sticky="NSEW")
			self.frames[F] = frame

		self.showPage(PageHome)

	
	initNumpad = False
	def showPage(self, cls):
		if self.initNumpad:
			if cls!=PageHome:
				result = Numpad.NumPad("Yöneciti Şifresi Gir").getValue()
			#tk.messagebox.askyesno(title="Password",message=result)
			#self.menuHome.config(text=result)
		else:
			self.initNumpad=True
		
		self.frames[cls].tkraise()


		
		
app = PythonGUI()
app.mainloop()