
import OpenSSL

a = ["05","ab", "ff"] 
bnry = ""

test = OpenSSL.rand(6)

for el in a:
	bnry += bin(int(el, 16))[2:]
	
count = 0

print bnry

for b in bnry:
	if int(b) == 1:
		print '{0}: {1}^{2}'.format(b, b, count)
	count += 1
