#!/usr/bin/env python
from langtools.EpubTranslationList import EpubTranslationList
from langtools.print_tools import print_list_to_terminal
from optparse import OptionParser
# create a subclass and override the handler methods

parser = OptionParser()
parser.add_option("-f", "--file", 
					dest="filename",
                  	help="location of EPUB",
                  	action="store",
                  	type="string",
                  	default=None)
parser.add_option("-c", "--chapter",
                  	action="store", 
                  	dest="chapter", 
                  	help="Which chapter would you like to load",
                  	type="int",
                  	default=None)
parser.add_option("-r", "--reverse",
					dest="reverse",
					help="see least common words",
					action="store_true",
					default=False)
parser.add_option("-n", "--number",
					action="store",
					dest="number",
					type="int",
					help="number of words you'd like to see.",
					default=5)
(options, args) = parser.parse_args()
if options.filename is not None:
	book = EpubTranslationList(options.filename)
	if options.chapter is None:		
		print("Imported {0}, please select which chapter to read".format(book.title))
		
		for index, item in enumerate(book.chapters):
			print("{0}. {1}".format(index,item.get_name()))
	else:
		chapter = book.get_chapter(options.chapter)
		words = []
		if options.reverse is True:
			words = chapter.get_least_common(options.number)
		else:
			words = chapter.get_most_common(options.number)
		print_list_to_terminal(words)
