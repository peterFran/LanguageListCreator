from langtools.LanguageListCreator import LanguageListCreator
from prettytable import PrettyTable
from termcolor import *

llc = LanguageListCreator()

words = llc.get_list_from_file('resources/cien.txt')
table = PrettyTable(["Word",
	"First Translation",
	"Second Translation",
	"First Compound", 
	"First Compound Translation",
	#"Second Compound", 
	#"First Compound Translation",
	])
i =0
for translations in words:
	
	def xstr(s):
		if i % 4 == 0:
			return colored("---","red") if s is None else colored(s, "red")
		elif i % 4 == 2 :
			return colored("---","green") if s is None else colored(s, "green")
		elif i % 4 == 1:
			return "---" if s is None else s
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