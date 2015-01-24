import re, random
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

	def all_verbs(self,):
		all_verbs = [word for word in self.dictionary if not word[0].isupper() and re.match(".*[i|e|a]r$", word)]
		return all_verbs

	def get_random_word(self):
		return self.dictionary[random.randrange(0,len(self.dictionary))]

	def get_random_verb(self):
		return self.all_verbs()[random.randrange(0, len(self.all_verbs()))]