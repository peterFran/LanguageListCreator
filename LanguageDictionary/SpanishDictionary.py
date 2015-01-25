import re, random, json
from urllib.parse import quote
from urllib.request import urlopen
#from urllib import URLError
class SpanishDictionary(object):
	dictionary = list()
	def __init__(self, file_location):
		
		try:
			with open(file_location, encoding='iso-8859-1') as dictionary_file:
				contents = dictionary_file.read()
				dictionary_array = list()
				self.dictionary = [line.split("/")[0] for line in contents.split("\n") if not re.search("\d|\?", line, re.U) and line.split("/")[0] is not ""]
		except IOError:
			return None

	def all_verbs(self,):
		all_verbs = [word for word in self.dictionary if not word[0].isupper() and re.match(".*[i|e|a]r$", word)]
		return all_verbs

	def get_random_word(self):
		return self.dictionary[random.randrange(0,len(self.dictionary))]

	def get_random_verb(self):
		return self.all_verbs()[random.randrange(0, len(self.all_verbs()))]

	def get_translations(self):
		return 
	def get_random_word_translated(self,):
		# Use quote method to percent encode, after first encoding utf with hex
		url_word = quote(self.get_random_word())
		url = "http://api.wordreference.com/0.8/8a8bc/json/esen/{0}".format(url_word)
		try:
			# Get the JSON from the web server
			result = urlopen(url).read().rstrip()
			return json.loads(result.decode())
		#except URLError as e:
			#eturn None
		except ValueError as e:
			return None