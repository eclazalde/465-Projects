import binascii

from OpenSSL import rand

class ModEx(object):
	p = 0;
	#def __init__(self):
	#	p = 0
	
	def run(self):
		p = rand.bytes(500)
		print binascii.hexlify(p)
		print p.decode('ascii')
		#for character in p:
		 # print character.encode('hex')
		

if __name__ == '__main__':
    ModEx().run()
