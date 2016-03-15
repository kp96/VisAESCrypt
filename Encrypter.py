# -*- coding: utf-8 -*-
# @Author: Krishna
# @Date:   2016-03-13 14:41:06
# @Last Modified by:   Krishna
# @Last Modified time: 2016-03-14 22:45:16
import base64
import hashlib
from AESCipher import AESCipher
from PIL import Image
from random import randint
class Encrypter:
	def __init__(self, text, key, splits = None):
		self.text = text
		self.key = key
		print base64.b64encode(key)
		if splits is None:
			self.splits = 2
		else:
			self.splits = splits
	def generate_splits(self):
		aes = AESCipher(self.key)
		cipher = aes.encrypt(self.text)
		print cipher
		message = aes.decrypt(cipher)
		print message
		size = 255, len(self.key)
		im = Image.new("1", size, "white")
		pix =  im.load()
		for i in range(len(self.key)):
			for j in range(ord(self.key[i])):
				pix[j, i] = 0
		im.save("original.gif")
		share1 = Image.new("1", size, "white")
		share1pix = share1.load()
		for i in range(len(self.key)):
			for j in range(255):
				x = randint(0,1)
				if x == 0:
					share1pix[j, i] = 0
		share2 = Image.new("1", size)
		share2pix = share2.load()
		for i in range(len(self.key)):
			for j in range(255):
				if pix[j, i] == share1pix[j, i]:
					share2pix[j, i] = 0
				else:
					share2pix[j, i] = 255
		output = [share1, share2, cipher]
		return output

