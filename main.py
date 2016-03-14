from Encrypter import Encrypter
from PIL import Image as Img
from PIL import ImageTk as ImgTk
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
	myMessage=e1.get()
	myKey=e2.get()
	x = Encrypter(myMessage, myKey,  2)
	output = x.generate_splits()
	tk1 = ImgTk.PhotoImage(output[0])
	tk2 = ImgTk.PhotoImage(output[1])
	tk1img = Label(image=tk1)
	tk1img.image = tk1 
	tk1img.pack()
	tk2img = Label(image=tk2)
	tk2img.image = tk2
	tk2img.pack()
	label.configure(text= "Cipher: " + output[2])
b = Button(master, text="Encrypt", width=10, command=callback)
b.pack()
master.mainloop()

