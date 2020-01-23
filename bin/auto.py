#-*- coding: utf-8 -*-
from sys import argv
from os.path import exists
import time
import sys
from datetime import date




# dodaje data do wydarzenie czyli kupionego paliwa
def do_dane(kilo, ilo, ceno):
	#dzisiejsza data
	today = date.today().isoformat()
	tt = date.today()

	print today

	#script, kilometry, ilosc, cena = argv
	#otwiera plik gdzie wszystko jest zapisane 
	kilometry = kilo
	ilosc = ilo
	cena = ceno
	nazwa = r'C:\ex52_facelift\bin\dane.txt'
	zapis = open(nazwa, "a")

	#dd = raw_input("Kilometry***Ilosc***Cena***")
	#s = zapis.read()
	#przerabia dane na liczby
	a = float(kilometry)
	b = float(ilosc)
	c = float(cena)
	print a/100

	#Obliczaniesredniej spalania
	if a > 100:
		ssre = b/(a/100)
		sre = round(ssre,3)
	#jesli mniej niz 100 kilometrow
	
	else:
		ssre = b/(a/10)
		sre = round(ssre,3)

	#zapisywanie danych
	zz = " "
	zapis.write(today + zz)
	zapis.write(kilometry + zz)
	zapis.write(ilosc + zz)
	zapis.write(cena + zz)
	zapis.write(str(sre))
	zapis.write("\n")


	zapis.close()

	#print dl

	#wyswietla zawartosc pliku
def wys():
	for x in b:
		print x

#operacje na danych

def sumowanie_kilometrow(i):
	nazwa = r'C:\ex52_facelift\bin\dane.txt'
	# otwieranie pliku tylko do odczytu
	aa = open(nazwa, "r")
	# czyta wszsystko z pliku i zapisuje w postaci listy
	# gdzie kazda linia pliku jest nowym elementem
	b = aa.readlines()
	dl = len(b)
	uma = 0
	for x in range(dl):
		d = b[x].split(" ")
		uma = uma + float(d[int(i)])
		
			
	b = "Suma kilometrów: %s." % uma
	lista =[]
	lista.append(b)
	return lista
	aa.close()

def sumowanie_kosztow():
	nazwa = r'C:\ex52_facelift\bin\dane.txt'
	# otwieranie pliku tylko do odczytu
	aa = open(nazwa, "r")
	# czyta wszsystko z pliku i zapisuje w postaci listy
	# gdzie kazda linia pliku jest nowym elementem
	b = aa.readlines()
	dl = len(b)
	# suma w euro
	uma = 0
	#suma w zloty
	puma = 0
	for x in range(dl):
		ilo = 0
		d = b[x].split(" ")
		ilo = float(d[2]) * float(d[3])
		#print ilo
		if float(d[3]) > 1:
			puma = puma + ilo
		else:
			uma = uma + ilo
		
	lista = []		
	b = "Suma zlotowek %s. A teraz wydanego Euro %s" % (round(puma, 2), round(uma, 2))
	lista.append(b)
	return lista
	aa.close()
		

#wyswietla zapisane dane 
def wpisy(a):
	nazwa = r'C:\ex52_facelift\bin\dane.txt'
	aa = open(nazwa, "r")
	b = aa.readlines()
	dl = len(b)
	lista = []
	
	if a == "w":
		for x in b:
			xx = x.split()
			print xx
			linne = "Data " +xx[0] + " Kilometry " + xx[1] + " Paliwo " + xx[2] + " Cena: " + xx[3] + " Srednia: " + xx[4]

			lista.append(linne)
		return lista
	elif a == "k":
		line = b[dl - 1]
		k = line.split()
		return k
	else:
		# po to ta lista zeby na stronie sie dobrze wyswietlalo
		line = b[dl - 1]
		print line
		k = line.split()
		pr = " "
		linne = "Data " + pr + k[0] + " Kilometry " + k[1] + " Paliwo " + k[2] + " Cena: " + k[3] + " Srednia: " + k[4]
		lista.append(linne)
		return lista
	aa.close()

def po_menu():
	d = raw_input("D - Nowy wpis. W Wszystkie wpisy. O Ostatni wpis. Z Back. C Zamknij program. ")
	if d == "d":
		do_dane()
		po_menu()
	elif d == "w":
		wpisy(d)
		po_menu()
	elif d == "o":
		wpisy(d)
		po_menu()
	elif d == "z":
		main()
	elif d == "c":
		sys.exit(0)
	else:
		po_menu()
			
		

def main():
	d = raw_input("D dane. S suma kilometrow. P suma kupionego paliwa. K koszty paliwo. ")
	if d == "d":
		po_menu()
	elif d == "s":
		sumowanie_kilometrow("1")
		main()
	elif d == "p":
		sumowanie_kilometrow("2")
		main()
	elif d =="k":
		sumowanie_kosztow()
		main()
	else:
		print "Sprobuj jeszcze raz."
		main()


#nowy plik z odwrotna kolejnoscia
#rev = open("datarev.txt", "a")

# wyswietla zawartosc pliku od tylu.
#def od_tylu():
	#for x in range((dl - 1), -1, -1):
		#rev.write(b[x])
		#print b[x]
	
#rev.close()

#sumowanie()
#main()