#!/usr/local/bin/python
# coding=UTF-8

import sqlite3
import re

def check():
	with sqlite3.connect("data/word_lists.db") as db:
		try:
			db.execute("SELECT word FROM es where qualified='1'")
			return True
		except:
			return False
def setup():
	with open("es-ES.dic") as dictionary_file:
		with sqlite3.connect("data/word_lists.db") as db:
			db.execute("DROP TABLE if exists es")
			db.execute("CREATE TABLE es(id INTEGER PRIMARY KEY, word text, date_learned DATE, qualified BOOLEAN)")
			db.commit()
			cur = db.cursor()
			contents = dictionary_file.read().decode('iso-8859-1').encode('utf8').rstrip()
			oldline = ""
			for line in contents.split("\n"):
				if not re.search("\d|\?", line, re.U):
					line = line.split("/")[0]
					ending = line.rstrip("s").rstrip("o|a|e")
					if ending != oldline:
						db.execute("insert into es(id,word, qualified) values(null,'"+line.split("/")[0]+"',0)")
						oldline = ending
			db.commit()
