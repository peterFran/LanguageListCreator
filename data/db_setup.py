#!/usr/local/bin/python
# coding=UTF-8

import sqlite3
import re

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
