from termcolor import *
from prettytable import PrettyTable

def print_list_to_terminal(words):
		table = PrettyTable(["Index",
			"Word",
			"First Translation",
			"Second Translation",
			"First Compound", 
			"First Compound Translation",
			"Word Count",
			#"Second Compound", 
			#"First Compound Translation",
			])
		table.max_width["First Compound"] =30
		table.max_width["First Compound Translation"] =30
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
				i+1,
				xstr(translations["Original Word"]),
				xstr(translations["First Translation"]),
				xstr(translations["Second Translation"]),
				xstr(translations["First Compound"]), 
				xstr(translations["First Compound Translation"]),
				xstr(translations["count"]),
				#xstr(translations["Second Compound"]), 
				#xstr(translations["Second Compound Translation"]),
				])
			i += 1
		print(table)