from Encrypter import Encrypter
from PIL import Image
from Tkinter import *


master = Tk()
master.wm_title("Visual Cryptograpy")
l1=Label(master, text="Message")
l2=Label(master, text="Key")

l1.pack()
e1 = Entry(master)
e1.pack()
e1.focus_set()


l2.pack()
e2 = Entry(master)
e2.pack()
e2.focus_set()


label = Label (master, text="")
label.pack()
def callback():
	result=e1.get()
	result1=e2.get()
	x = Encrypter(result, result1,  2)
	output = x.generate_splits()
	output[0].save("share1.png")
	output[1].save("share2.png")
	size = 255, 13
	final = PIL.Image.new("1", size)
	pix = final.load()
	op1 = output[0].load()
	op2 = output[1].load()
	for i in range(13):
		for j in range(255):
			pix[j, i] = op1[j, i] ^ op2[j, i]
	final.save("combinedorignal.png")
	label.configure(text=x)
     

b = Button(master, text="Encrypter", width=10, command=callback)
b.pack()

master.mainloop()

