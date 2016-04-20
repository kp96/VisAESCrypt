# -*- coding: utf-8 -*-
# @Author: Krishna
# @Date:   2016-04-20 11:40:01
# @Last Modified by:   Krishna
# @Last Modified time: 2016-04-20 12:14:11
import base64
import hashlib
from AESCipher import AESCipher
from PIL import Image
from random import randint
class Decrypter:
	def __init__(self, cipher, shares):
		self.cipher = cipher
		self.shares = shares
	def get_image_from_shares(self):
		share_one = self.shares[0];
		share_two = self.shares[1];
		output = Image.new("1", share_one.size, "white")
		share_one_pix = share_one.load()
		share_two_pix = share_two.load()
		output_pix = output.load()
		width , height = output.size
		for i in range(height):
			for j in range(width):
				output_pix[j, i] = share_one_pix[j, i] ^ share_two_pix[j, i]
		return output
	def get_key_from_image(self):
		img = self.get_image_from_shares()
		key = ""
		img_pix = img.load()
		width, height = img.size
		for i in range(height):
			cur = 0
			for j in range(width):
				if img_pix[j, i] == 0:
					cur = cur + 1
				else:
					break
			key = key + chr(cur)
		return key
	def decrypt_image(self):
		key = self.get_key_from_image()
		cipher = self.cipher
		aes = AESCipher(key)
		base64_decoded = aes.decrypt(cipher)
		fh = open("decryptedImage.png", "wb")
		fh.write(base64_decoded.decode('base64'))
		fh.close() 



