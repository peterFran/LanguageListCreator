#!/usr/local/bin/python

import sqlite3
import re
with open("es-ES.dic") as dictionary_file:
	with sqlite3.connect("word_lists.db") as db:
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
