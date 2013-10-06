import sqlite3
import random
import arrow
if __name__ == '__main__':
	from QueryLocalDB import *
	ll = LanguageDatabase()
	print ll.getNewWord()
	ll.getWordsInPeriod(m=-1,d=1)

class LanguageDatabase(object):
	def __init__(self):
		
		with sqlite3.connect("word_lists.db") as db:
			cur = db.cursor()
			cur.execute("SELECT MAX(id) FROM es")
			self.max_value = cur.fetchone()[0]
	def getNewWord(self):
		word = None
		with sqlite3.connect("word_lists.db") as db:
			cur = db.cursor()			
			while word is None:
				index = random.randint(1,self.max_value)
				cur.execute("SELECT word FROM es WHERE id IS %d AND date_learned IS null" % index)
				word = cur.fetchone()[0]
			cur.execute("UPDATE es SET date_learned='%s' WHERE id='%d'" % (str(arrow.now().format('YYYY-MM-DD HH:mm:ss')), index))
			db.commit()
		return word
	def getWordsInPeriod(self,d=0,m=0,y=0):
		with sqlite3.connect("word_lists.db") as db:
			cur = db.cursor()
			end_period = arrow.now().replace(days=1).format('YYYY-MM-DD')
			start_period = arrow.now().replace(days=d,months=m,years=y).format('YYYY-MM-DD')
			# for line in cur.execute("SELECT word,date_learned FROM es WHERE date_learned BETWEEN '%s' AND '%s' ORDER BY date_learned" % (ago,today)).fetchall():
			# 	print line[0],"\t",arrow.get(str(line[1]), 'YYYY-MM-DD HH:mm:ss').format('D MMMM YYYY')
			return cur.execute("SELECT word,date_learned FROM es WHERE date_learned BETWEEN '%s' AND '%s' ORDER BY date_learned" % (start_period,end_period)).fetchall()

			