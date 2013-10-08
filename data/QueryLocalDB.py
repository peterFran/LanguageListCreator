# coding=UTF-8

import sqlite3
import random
import arrow
import os
if __name__ == '__main__':
	from QueryLocalDB import *
	ll = LanguageDatabase()
	for i in ll.getNewWords(10):
		print i
	ll.getWordsInPeriod(m=-1,d=1)

class LanguageDatabase(object):
	def __init__(self):
		with sqlite3.connect("./data/word_lists.db") as db:
			cur = db.cursor()
			cur.execute("SELECT MAX(id) FROM es")
			self.max_value = cur.fetchone()[0]

	def qualify(self,word):
		with sqlite3.connect("./data/word_lists.db") as db:
			cur = db.cursor()
			cur.execute("UPDATE es SET qualified=1 WHERE word='%s'" % word)
			db.commit()

	def getNewWord(self):
		word = None
		with sqlite3.connect("./data/word_lists.db") as db:
			cur = db.cursor()			
			while word is None:
				index = random.randint(1,self.max_value)
				cur.execute("SELECT word FROM es WHERE id IS %d AND date_learned IS null" % index)
				try:
					word = unicode(cur.fetchone()[0])
				except TypeError as e:
					word = None
			cur.execute("UPDATE es SET date_learned='%s' WHERE id='%d'" % (str(arrow.now().format('YYYY-MM-DD HH:mm:ss')), index))
			db.commit()
		return word

	def getNewWords(self, number_words):
		words = []
		for i in range(0,number_words):
			words.append(self.getNewWord())
		return words

	def getWordsInPeriod(self,d=0,m=0,y=0):
		with sqlite3.connect("./data/word_lists.db") as db:
			cur = db.cursor()
			end_period = arrow.now().replace(days=1).format('YYYY-MM-DD')
			start_period = arrow.now().replace(days=d,months=m,years=y).format('YYYY-MM-DD')
			words = []
			for word in cur.execute("SELECT word,date_learned FROM es WHERE qualified=1 AND date_learned BETWEEN '%s' AND '%s' ORDER BY date_learned" % (start_period,end_period)).fetchall():
				words.append(word[0])
			return words
