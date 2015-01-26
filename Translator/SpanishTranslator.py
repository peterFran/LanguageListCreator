import re, random, json
from urllib.parse import quote
from urllib.request import urlopen
from urllib.request import URLError
class SpanishTranslator(object):
	def __init__(self):
		self.url = "http://api.wordreference.com/0.8/8a8bc/json/esen/{0}"

	def translate_word_full(self, word):
		# Use quote method to percent encode, after first encoding utf with hex
		word_url = self.url.format(word)
		try:
			# Get the JSON from the web server
			raw_json_result = urlopen(word_url).read().rstrip()
			result = json.loads(raw_json_result.decode())
			return result
		except URLError as e:
			return None
		except ValueError as e:
			return None

	def translate_word(self, word):
		word_object = self.translate_word_full(word)
		if word_object is None:
			return None
		if 'term0' not in word_object or 'PrincipalTranslations' not in word_object['term0']:
			return None
		return word_object['term0']['PrincipalTranslations']['0']['FirstTranslation']['term']

