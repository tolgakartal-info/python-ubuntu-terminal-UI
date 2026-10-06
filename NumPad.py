import tkinter as tk
from functools import partial
class NumPad: 
	numPadVal=""
	is_init = False
	screen_size = {"width":0,"height":0}
	def __init__(self,title):
		if self.is_init!=True:
			self.form = tk.Tk()
			self.form.attributes("-fullscreen",True)
			self.form.configure(background="black")
			self.screen_size["width"] = self.form.winfo_screenwidth()
			self.screen_size["height"] = self.form.winfo_screenheight()
			self.form.geometry("{}x{}".format(self.screen_size["width"],self.screen_size["height"]))
			# Numpad grid yüksekliği
			gridH = int(self.screen_size["height"]/5)
			gridPercent = self.screen_size["width"]/self.screen_size["height"]  
			winW = self.form.winfo_screenwidth()
			winH = self.form.winfo_screenheight() 
			self.titleLabel = tk.Label(self.form,font=("Verdana",25),bg="black",fg="white",text=title)
			self.titleLabel.place(x=30,y=0,width=winW-60, height=90)
			self.textBox = tk.Entry(self.form,font=("Verdana",30), justify="center")
			self.textBox.place(x=30,y=90,width=winW-60, height=gridH-60)
			screenX = 1
			screenY = 1
			btnSize = gridH-5
			numPadLeft = int(self.screen_size["width"]-(btnSize*5))/2

			for num in ["1","2","3","4","5","6","7","8","9","0","<","Tamam"]:
				self.n = tk.Button(self.form, anchor="center",text=num,font=("Verdana",20),bg="black",fg="white",command = partial(self.changeText,num))
				self.n.place(x=numPadLeft+(btnSize*screenX),y=35+(btnSize*screenY),width=btnSize, height=btnSize);
				if screenX % 3 == 0:
					screenX=0
					screenY+=1
				screenX+=1
			self.textBox.focus()
			self.form.mainloop()
		else: self.is_init=True


	def changeText(self,num):
		if num=="Tamam":
			self.form.quit()
			self.form.destroy()
			return
		if num=="<":
			if len(self.numPadVal)>0:
				self.textBox.delete(len(self.numPadVal)-1,len(self.numPadVal))
				self.numPadVal = self.textBox.get()
			return
		self.textBox.insert("end",num)
		self.numPadVal=self.numPadVal + str(num) 

	def getValue(self):
		return self.numPadVal
