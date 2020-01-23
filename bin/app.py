import web
#from gothonweb import map
import map
import auto
import onet
urls = (
	'/karol',  'Poczatek',
	'/', 'Index',
	'/auto_program', 'Auto',
	'/ostatni', 'Ostatni',
	'/wwpisy', 'Wwpisy',
	'/logout', 'Logout',
	'/suma_kosztow', 'SumaKK',
	'/onet', 'Czcz',
	'/przejechane', 'Przejechane',
)

app = web.application(urls, globals())



#little hack so that debug mode works with sessions
"""if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store,
									initializer={'room': None, 'count': 0})
	
	web.config._session = session
else:
	session = web.config._session
"""
	

render = web.template.render('templates/', base="layout")
#inny renderowanie
porender = web.template.render('templates/')







class Index(object):
	
	def GET(self):
		#this is used to "setup" the session with starting values
		#to odsyla dalej do nowej klasy
		web.seeother("/karol")


class Poczatek(object):

	def GET(self):
		return render.show_room(prawy="prawy", form=None)
		
	def POST(self):
		
		kot = auto.wpisy("d")
		#print kot

		return render.show_room(prawy=kot, form=form.action)
		web.seeother("/karol")
		
class Auto(object):
		

	def GET(self):
		return render.auto(a=None, kk=None)
	
	def POST(self):
		#Dane do zapisu
		form = web.input(name="action")
		korn = web.input(name="ilo")
		worn = web.input(name="cena")
		auto.do_dane(form.action,korn.ilo,worn.cena)
		web.seeother("karol")

#OStatni wpis		
class Ostatni(object):

	def GET(self):
		bb = auto.wpisy("d")
		kkk = auto.wpisy("k")
		#kk = kkk.k
		return render.auto(a=bb, kk=kkk)
		
class Wwpisy(object):

	def GET(self):
		bb = auto.wpisy("w")
		return render.auto(a=bb, kk=None)
		
		
class SumaKK(object):

	def GET(self):
		bb = auto.sumowanie_kosztow()
		return render.auto(a=bb, kk=None)
		
class Przejechane(object):

	def GET(self):
		bb = auto.sumowanie_kilometrow(1)
		return render.auto(a=bb, kk=None)
		
		
class Czcz(object):

	def GET (self):
		onet.linki()
		nazwa = r'C:\ex52_facelift\bin\onet.txt'
		aa = open(nazwa, 'r')
		#return aa
		return porender.onett(plik=aa)
		

		

	


if __name__ == "__main__":
	app.run()
else:
	print "Sie nie rowna"
	print __name__
