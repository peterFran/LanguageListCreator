#!/usr/bin/env python
from langtools.LanguageListCreator import LanguageListCreator
from prettytable import PrettyTable
from termcolor import *
import sys
llc = LanguageListCreator()
words = []
num = 5
if len(sys.argv) > 1:
	num = int(sys.argv[1])
words = llc.get_list_from_file('resources/cien.txt', num)
table = PrettyTable(["Word",
	"First Translation",
	"Second Translation",
	"First Compound", 
	"First Compound Translation",
	#"Second Compound", 
	#"First Compound Translation",
	])
table.max_width["First Compound"] =30
i =0
for translations in words:
	
	def xstr(s):
		if i % 4 == 0:
			return colored("---","red") if s is None else colored(s, "red")
		elif i % 4 == 2 :
			return colored("---","green") if s is None else colored(s, "green")
		elif i % 4 == 1:
			return colored("---","white") if s is None else colored(s,"white")
		else:
			return colored("---","yellow") if s is None else colored(s, "yellow")
	table.add_row([
		xstr(translations["Original Word"]),
		xstr(translations["First Translation"]),
		xstr(translations["Second Translation"]),
		xstr(translations["First Compound"]), 
		xstr(translations["First Compound Translation"]),
		#xstr(translations["Second Compound"]), 
		#xstr(translations["Second Compound Translation"]),
		])
	i += 1
print(table)