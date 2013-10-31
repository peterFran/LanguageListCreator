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
def setup_database():
	with sqlite3.connect("data/word_lists.db") as db:
		db.execute("DROP TABLE if exists user")
		db.execute("DROP TABLE if exists learned")
		db.execute("CREATE TABLE user(id INTEGER PRIMARY KEY, username text, email_address text, default_user BOOLEAN")
		db.execute("CREATE TABLE learned(user_id INTEGER, word_id INTEGER, date_learned DATE, language text")

def clear_database():
	with sqlite3.connect("data/word_lists.db") as db:
		db.execute("DROP TABLE if exists user")
		db.execute("DROP TABLE if exists learned")
		db.execute("CREATE TABLE user(id INTEGER PRIMARY KEY, username text, email_address text, default_user BOOLEAN")
		db.execute("CREATE TABLE learned(user_id INTEGER, word_id INTEGER, date_learned DATE, language text")

def setup_user(username, email_address, default=False):
	with sqlite3.connect("data/word_lists.db") as db:
		db.execute("INSERT INTO user(id username, email_address, default_user) values(?,?,?,?)", (None, username, email_address, default))
		
def setup_language(language):
	print "Seting up database for chosen language..."
	with open("data/%s.dic" % language) as dictionary_file:
		with sqlite3.connect("data/word_lists.db") as db:
			db.execute("DROP TABLE if exists %s" % language)

			db.execute("CREATE TABLE %s(id INTEGER PRIMARY KEY, word text, black_listed BOOLEAN)"% language)
			db.commit()
			cur = db.cursor()
			contents = dictionary_file.read().rstrip()
			oldline = ""
			if language == "es":
				for line in contents.split("\n"):
					if not re.search("\d|\?", line, re.U) and line.split("/")[0] is not "":
						word = line.split("/")[0].rstrip().decode('iso-8859-1')
						row = (None,word,0)
						ending = line.rstrip("s").rstrip("o|a|e")
						if ending != oldline:
							db.execute("insert into es(id,word, qualified) values(?, ?,?)" , row)
							oldline = ending
			elif language == "it":
				for line in contents.split("\n"):
					if not re.search("\d|\?", line, re.U) and line.split("/")[0] is not "":
						word = line.split("/")[0].rstrip().decode('iso-8859-1')
						row = (None,word,0)
						ending = line.rstrip("o|a|e|i")
						if ending != oldline:
							db.execute("insert into it(id,word, qualified) values(?, ?,?)" , row)
							oldline = ending
			#TODO Burcu, here is where the algoritm for roming similar words in Turkish should go!
			elif language == "tr":
				for line in contents.split("\n"):
					if not re.search("\d|\?", line, re.U) and line.split("/")[0] is not "":
						word = line.split("/")[0].rstrip().decode("UTF-8")
						row = (None,word,0)
						print row
						db.execute("insert into tr(id,word, qualified) values(?,?,?)" , row)
			db.commit()