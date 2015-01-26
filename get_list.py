
from prettytable import PrettyTable

import langtools

table = PrettyTable(["Word","First Translation","Second Translation","First Compound", "First Compound Translation"])
for verb, translations in verbs.items():
	def xstr(s):
		return "---" if s is None else s
	table.add_row([translations["Original Word"],translations["First Translation"],xstr(translations["Second Translation"]),xstr(translations["First Compound"]), xstr(translations["First Compound Translation"])])
print(table)