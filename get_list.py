#!/usr/bin/env python

from prettytable import PrettyTable

from langtools.LanguageListCreator import LanguageListCreator
llc = LanguageListCreator()
verbs =llc.random_verbs(0)
words = llc.random_words(15)
table = PrettyTable(["Word",
	"First Translation",
	"Second Translation",
	"First Compound", 
	"First Compound Translation",
	#"Second Compound", 
	#"First Compound Translation",
	])
for translations in verbs:
	def xstr(s):
		return "---" if s is None else s
	table.add_row([translations["Original Word"],
		translations["First Translation"],
		xstr(translations["Second Translation"]),
		xstr(translations["First Compound"]), 
		xstr(translations["First Compound Translation"]),
		#xstr(translations["Second Compound"]), 
		#xstr(translations["Second Compound Translation"]),
		])
for translations in words:
	def xstr(s):
		return "---" if s is None else s
	table.add_row([translations["Original Word"],
		translations["First Translation"],
		xstr(translations["Second Translation"]),
		xstr(translations["First Compound"]), 
		xstr(translations["First Compound Translation"]),
		#xstr(translations["Second Compound"]), 
		#xstr(translations["Second Compound Translation"]),
		])
print(table)