import random
import OpenSSL
import itertools

class ModEx(object):
	
	def run(self):
		#g= 5
		g = 2573041524068575501546774721958551382793444058852959448173073424708835049483214746377114621027868168763968221918355434732930964212304265577079830246362
		s = 0
		p = 0
		f  = open('large numbers.txt', 'r')

		for line in f:
			l = line.split('=')
			if l[0] == 's':
				s = int(l[1])
			if l[0] == 'p':
				p = int(l[1])
		
		if p == 1:
			print 0
			
		result = 1
		g = g % p
		while s > 0:
			if (s % 2 == 1):
				result = (result * g) % p
			s = s >> 1
			g = (g * g) % p
		
		print result
		
		
class LargeRandom(object):
	
	def run(self):
		#
		# Generate large number for s
		p = 0
		p = random.SystemRandom(random.seed()).getrandbits(500)
		print "{}".format(p)
		
			

if __name__ == '__main__':
	#LargeRandom().run()
    ModEx().run()
