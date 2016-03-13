from Encrypter import Encrypter
from PIL import Image
x = Encrypter("nee m**** le ra jaffa poyyi banga", "epic shit bro",  2)
output = x.generate_splits()
output[0].save("share1.png")
output[1].save("share2.png")
size = 255, 13
final = Image.new("1", size)
pix = final.load()
op1 = output[0].load()
op2 = output[1].load()
for i in range(13):
	for j in range(255):
		pix[j, i] = op1[j, i] ^ op2[j, i]
final.save("combinedorignal.png")