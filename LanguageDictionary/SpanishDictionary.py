import json, re
class SpanishDictionary(object):
	dictionary = list()
	def __init__(self, file_location):
		
		try:
			with open(file_location, encoding='iso-8859-1') as dictionary_file:
				contents = dictionary_file.read()
				dictionary_array = list()
				for line in contents.split("\n"):
					if not re.search("\d|\?", line, re.U) and line.split("/")[0] is not "":
						word = line.split("/")[0]
						self.dictionary.append(word)
		except IOError:
			return None