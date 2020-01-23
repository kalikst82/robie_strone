#-*- coding: utf-8 -*-
from mechanize import Browser
from bs4 import BeautifulSoup
import urllib

def linki():

	nazwa = r'C:\ex52_facelift\bin\onet.txt'
	with open(nazwa, "a") as zapis:

		url = "https://www.onet.pl/"
		html = urllib.urlopen(url).read()

		soup = BeautifulSoup(html, 'html.parser')
		tag = soup.find_all("span", {"class":"title"})
		"""
		for x in tag:
			#print(x.strip('<span class="title">'))
			print(x)
			
		"""

		wiadomosci = soup.find_all("div", {"class":"sideBarItem"})
		bak =[]
		zapis.truncate(0)
		for x in wiadomosci:
			#print x
			#bak = x.find_all("span", {"class":"title"})
			links = [a['href'] for a in x.find_all('a', href=True)]
			titel = [span for span in x.find_all('span', {"class":"title"})]
			b = [links, titel]
			#print b,
			#print titel
			#bak.append(str(x.find_all("a", href=True)))
		
			for u in links:
				#pink = soup.find_all("href", u.strip('u'))
				#print u.strip('u'), pink
				
				#zapis.write("<a href=" + u.strip('u')+ ">" + u.strip('u').strip('https://') + "</a><br>" + '\n')
				zapis.write(u.strip('u').strip('https://') + '\n')

