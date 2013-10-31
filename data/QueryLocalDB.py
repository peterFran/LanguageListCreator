# coding=UTF-8

import sqlite3
import random
import arrow
from collections import OrderedDict
import os
if __name__ == '__main__':
	from QueryLocalDB import *
	ll = LanguageDatabase()
	for i in ll.getNewWords(10):
		print i
	ll.getWordsInPeriod(m=-1,d=1)

class LanguageDatabase(object):
	def __init__(self, database_location):
		self.database_location = database_location

	def getNewWord(self, language, user):
		max_value = self._max_value(language):

		word = None
		word_id = None
		with sqlite3.connect(self.database_location) as db:
			cur = db.cursor()
			learned = True
			while learned is True:
				word_id = random.randint(1,max_value)
				cur.execute("SELECT id,word FROM %s WHERE id IS %d" % (language, index))
				try:
					word = unicode(cur.fetchone()[0])
				except TypeError as e:
					word = None
				learned = self._check_if_learned(word_id, language, user)
			cur.execute("INSERT INTO learned(word_id, user_id, language, date_learned) values(?,?,?,?)",(word_id, user_id, language, str(arrow.now().format('YYYY-MM-DD HH:mm:ss'))))
			db.commit()
		return word

	def _check_if_learned(self, word_id, language, user):
		if word_id is None:
			return True


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
			words_by_date = OrderedDict()
			for word in cur.execute("SELECT word,date_learned FROM %s WHERE qualified=1 AND date_learned BETWEEN '%s' AND '%s' ORDER BY date_learned" % (self.LANGUAGE, start_period,end_period)).fetchall():
				if word[1] not in words_by_date:
					words_by_date[word[1]]=list()
				words_by_date[word[1]].append(word[0])
			return words_by_date
