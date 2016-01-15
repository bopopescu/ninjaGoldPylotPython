from system.core.controller import*
import random
import datetime
from time import strftime
class Ninja(Controller):
	def __init__(self, action):
		super(Ninja, self).__init__(action)
	def index(self):
		try:
			session['gold']
		except:
			session['gold'] = 0
		try:
			session['activities']
		except:
			session['activities'] = []
		return self.load_view('ninja.html')
	def clear(self):
		session.clear()
		return redirect('/')
	def process(self):
		action = request.form['action']
		randomNumber = random.random()
		print randomNumber
		if action == "farm":
			earn = int(randomNumber*10)+10
		elif action == 'cave':
			earn = int(randomNumber*5)+5
		elif action == "house":
			earn = int(randomNumber*3)+2
		elif action == "casino":
			earn = int(randomNumber*100)-50
		session['gold'] += earn
		timeNow = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S %p')
		if earn >= 0 :
			newAction = {
				'status' : 'earn',
				'action' : "Earned {} gold from {} ({})".format(earn, action, timeNow)
			}
		else:
			newAction = {
				'status' : 'lost',
				'action' : "Entered Casino and lost {} gold.. Ouch.. ({})".format(-earn, timeNow)
			}
		print newAction
		session['activities'].append(newAction)
		print session['activities']
		return redirect('/')