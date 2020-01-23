#-*- coding: utf-8 -*-
import os
lista_data = []
lista_kilom = []
ee = []
bb = []
ostatnia = []
suma = 0

def raport():

	#otwieramy plik  z danymi
	nazwa = r'C:\ex52_facelift\bin\dane.txt'
	czy = os.path.exists(nazwa)
	print czy
	aa = open(nazwa, 'r')
	#robimy sobie z niego liste
	b = aa.readlines()
	#mierzymy ile ona ma
	dl = len(b)
	uma = 0
	
	for x in range(dl):
		d = b[x].split(' ')
		#d[1] kilometry
		#print d[1]
		e = d[0].split('-')
		lista_data.append((e[0], e[1]))
		lista_kilom.append((e[0], e[1], d[1]))
		
	#usuwanie tych samych dat
	
	#print tt
	
	##sukces sukces
	#przeszukuje liste po kopi listy
	"""for x in list(lista_data):
		if x == x:
			lista_data.remove(x)
			if x not in ee:
				#ee.append(x)"""
			
	#tyle meczenia i to wystrczy
	#to usuwa duplikaty i tworzy liste miesiecy
	# w ktorych bylo tankowanie
	for x in lista_data:
		if x not in ee:
			ee.append(x)
		
		
	# dodawanie kilometrow w tym przypadk
	#porownuje dwie listy tzn liste miesiecy porownuje
	#do listy tankowania
	suma = 0	
	for a in ee:
		for x in lista_kilom:
			if a[0]==x[0] and a[1]==x[1]:
				data = x[0] + "-" + x[1] + " "
				suma = suma + int(x[2])
				bb.append((x[0], x[1], suma))
				print data, suma
		suma = 0
	
	print bb
	
	for x in ee:
		l = 0
		for y in bb:
			if x[0] == y[0] and x[1] == y[1]:
				#print y[2]
				l = l + 1
			#print l
		l = 0
		
			
		
	
	aa.close()
					
		
			
	
raport()

b = []


#print lista_data