#!/usr/bin/env python
from langtools.EpubTranslationList import EpubTranslationList
from prettytable import PrettyTable
from ebooklib import epub
from termcolor import *
import sys
from bs4 import BeautifulSoup
# create a subclass and override the handler methods

if len(sys.argv) > 1:
	book = EpubTranslationList(sys.argv[1])
	if len(sys.argv) < 3:		
		#print(dir(epub.EpubReader(sys.argv[1]).book))
		print("Imported {0}, please select which chapter to read".format(book.title))
		
		for index, item in book.chapters:
			print("{0}. {1}".format(index,item.get_name()))
	else:
		chapter = items[int(sys.argv[2])].get_content().decode('utf-8')
		soup = BeautifulSoup(chapter)
		llc = LanguageListCreator()
		num = 10
		if len(sys.argv) > 3:
			num = int(sys.argv[3])
		words = llc.get_list_from_text(soup.get_text(), num)
		table = PrettyTable(["Index",
			"Word",
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
				i,
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
