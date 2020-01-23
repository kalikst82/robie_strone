#-*- coding: utf-8 -*-



def raport():

	#otwieramy plik  z danymi
	nazwa = r'C:\ex52_facelift\bin\dane.txt'
	aa = open(nazwa, 'r')
	#robimy sobie z niego liste
	b = aa.readlines()
	#mierzymy ile ona ma
	dl = len(b)
	uma = 0
	
	for x in range(dl):
		d = b[x].split(' ')
		#print d[0]
		e = d[0].split('-')
		
		#print e[1]
		ll = []
		for k in range(len(b)):
			ll.append(k)
			dd = b[k].split(' ')
			ee = dd[0].split('-')
			if e[1] == ee[1]:
				uma = uma + int(dd[1])
				
				print uma, dd[1], ll
			elif e[1] != ee[1]:
			
				for i in range(len(ll), -1):		
					b.remove(b[i])
				ll = []
		uma = 0
		print len(b)
		
					
		
			
	
raport()