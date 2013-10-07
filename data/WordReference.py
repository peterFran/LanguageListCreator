import json
from urllib2 import urlopen
import urllib2

class WordReferenceDefinition(GenericDefinition):
	# Readable flag, set if you want to be able to understand ANYTHING
	self.READABLE = False
	def getWordDefinitionAsDict(word, dictionary_code):
		url = "http://api.wordreference.com/0.8/8a8bc/json/%s/%s" % (dictionary_code,word)
		url = url.encode('utf8').rstrip()
		print url
		try:
			result = urlopen(url).read().decode('iso-8859-1').encode('utf8').rstrip()
			return json.loads(result)
		except urllib2.URLError, e:
			return None
	def getWordDefinitionWithCheck(word, dictionary_code):
		definition = self.getWordDefinitionAsDict(word, dictionary_code)
		if definition is None:
			print "nope1"
			return None
		elif len(definition) <= 2:
			print "nope2"
			return None
		elif "Error" in definition:
			print "nope3"
			return None
		else:
			if self.READABLE:
				return self._makeReadable(word, definition)
			else:
				return definition
	def _makeReadable(definition):
		stucture = {"word":word;"translations":None;"usages":None;"compound":None}

if __name__ == '__main__':
	print checkWordExists("Hola", "esen")
