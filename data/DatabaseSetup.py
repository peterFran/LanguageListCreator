#!/usr/local/bin/python
# coding=UTF-8

import sqlite3
import re
import data.DictionaryReduce
class DatabaseSetup(object):
	def __init__(self, database_location):
		self.database_location = database_location
	def reset(self):
		with sqlite.connect(self.database_location):
			db.execute("DROP TABLE IF EXISTS user")
			db.execute("DROP TABLE IF EXISTS learned")
			db.execute("DROP TABLE IF EXISTS es")
			db.execute("DROP TABLE IF EXISTS it")
			db.execute("CREATE TABLE user(id INTEGER PRIMARY KEY, username TEXT, email_address TEXT, default_user BOOLEAN")
			db.execute("CREATE TABLE learned(word_id INTEGER, user_id INTEGER, language TEXT, date_learned DATE)")
			db.execute("CREATE TABLE es(word_id INTEGER, word TEXT, void BOOLEAN")
			db.execute("CREATE TABLE it(word_id INTEGER, word TEXT, void BOOLEAN")
			db.commit()
	
	def check(self):
		with sqlite.connect(self.database_location):
			try:
				db.execute("SELECT id FROM user")
				return True
			except:
				return False
	def setup_language(self, language):
		dictionary = DictionaryReduce()
		with sqlite3.connect("data/word_lists.db") as db:
			for word in dictionary.getDictionary(langauge):
				db.execute("insert into %s(word_id, word, void) values(?, ?, ?)" % language, (None, word, 0))
			db.commit()
	def setup_user(self, username, email_address, default_user):
		with sqlite3.connect("data/word_lists.db") as db:
			if default_user is True:
				db.execute("UPDATE user SET default_user=0 WHERE default_user=1")
			db.execute("insert into user(id, username, email_address, default_user) values(?, ?, ?, ?)",(None, username, email_address, default_user))

def check(language):
	with sqlite3.connect("data/word_lists.db") as db:
		try:
			db.execute("SELECT word FROM %s where qualified='1'" % language)
			return True
		except:
			return False
def setup(language):
	print language
	if language == "es":
		with open("data/es-ES.dic") as dictionary_file:
			with sqlite3.connect("data/word_lists.db") as db:
				db.execute("DROP TABLE if exists es")
				db.execute("CREATE TABLE es(id INTEGER PRIMARY KEY, word text, date_learned DATE, qualified BOOLEAN)")
				db.commit()
				cur = db.cursor()
				contents = dictionary_file.read().rstrip()
				oldline = ""
				for line in contents.split("\n"):
					if not re.search("\d|\?", line, re.U):
						word = line.split("/")[0].decode('iso-8859-1')
						row = (None,word,0)
						ending = line.rstrip("s").rstrip("o|a|e")
						if ending != oldline:
							db.execute("insert into es(id,word, qualified) values(?, ?,?)" , row)
							oldline = ending
				db.commit()
	elif language=="it":
		with open("data/it_IT.dic") as dictionary_file:
			with sqlite3.connect("data/word_lists.db") as db:
				db.execute("DROP TABLE if exists it")
				db.execute("CREATE TABLE it(id INTEGER PRIMARY KEY, word text, date_learned DATE, qualified BOOLEAN)")
				db.commit()
				cur = db.cursor()
				contents = dictionary_file.read().rstrip()
				oldline = ""
				for line in contents.split("\n"):
					if not re.search("\d|\?", line, re.U) and line.split("/")[0] is not "":
						word = line.split("/")[0].decode('iso-8859-1')
						row = (None,word,0)
						ending = line.rstrip("o|a|e|i")
						if ending != oldline:
							db.execute("insert into it(id,word, qualified) values(?, ?,?)" , row)
							oldline = ending
				db.commit()
