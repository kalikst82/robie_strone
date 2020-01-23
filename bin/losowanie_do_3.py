import random

koszyk = range(3, 53)
#print koszyk

"""los = random.choice(koszyk)
print los
koszyk.remove(los)
print koszyk """


licznik = input("Podaj liczbe powtorzen.")

#glowna fukcja liczaca ile razy zdarzy sie trojka a ile nie
def glowna(ll):
	yes_sum = 0
	no_suma = 0
	while ll > 0:
		ll -= 1
		lolo = losowanie()
		if lolo == 0:
			no_suma += 1
		else:
			yes_sum += 1
	ulamek = float(float(yes_sum) / float(no_suma))
	print "Tyle razy trafilo %d. A tyle razy nie %d.\n A to ulamek %.3f" % (yes_sum, no_suma, ulamek)

def losowanie():
	i = 5
	n = 0
	urna = range(3, 53)
	#losujemy z pozostaluch 50 kart
	los = random.choice(urna)
	while i > 0:
		#print i, los
		i -= 1
		if los == 13 or los == 14:
			n = 1
			break
			#return zatrzymuje petle
			#return n
			#print n
			
		else:
			#print n
			#usuwamy z urny karte
			urna.remove(los)
			# i od nowa losujemy karte
			los = random.choice(urna)
	return n     #zwraca sukces albo porazke
			
			
glowna(licznik)