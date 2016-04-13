import base64
from Crypto.Cipher import AES
import os
from PIL import Image as Img
from PIL import ImageTk as ImgTk
from Tkinter import *
import Tkinter,tkFileDialog

master = Tk()
master.wm_title("Visual Cryptography")
file = tkFileDialog.askopenfile(parent=master,mode='rb',title='Choose a file')
if file != None:
    data = file.read()
    str = base64.b64encode(data)
    print str
#with open(li, "rb") as imageFile:
    
#decrypt
#fh = open("vit.png", "wb")
#fh.write(str.decode('base64'))
#fh.close()
label = Label (master, text="")
label.pack()

#AES
# the block size for the cipher object; must be 16 per FIPS-197
BLOCK_SIZE = 16

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

# generate a random secret key
secret = os.urandom(BLOCK_SIZE)

# create a cipher object using the random secret
cipher = AES.new(secret,AES.MODE_CBC)

# encode a string
encoded = EncodeAES(cipher, 'str')
label.configure(text= "Encrypted string: " + encoded)
print 'Encrypted string:', encoded
master.mainloop()  