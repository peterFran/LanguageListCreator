import json
from urllib2 import urlopen
import urllib2
import re

class WordReferenceDefinition(object):
	# Readable flag, set if you want to be able to understand ANYTHING
	READABLE = False
	def getWordDefinitionAsDict(self, word, dictionary_code):
		url = "http://api.wordreference.com/0.8/8a8bc/json/%s/%s" % (dictionary_code,word)
		url = url.encode('utf8').rstrip()
		try:
			result = urlopen(url).read().decode('iso-8859-1').encode('utf8').rstrip()
			return json.loads(result)
		except urllib2.URLError, e:
			return None
	def getWordDefinitionWithCheck(self, word, dictionary_code):
		definition = self.getWordDefinitionAsDict(word, dictionary_code)
		if definition is None:
			return None
		elif len(definition) <= 2:
			return None
		elif "Error" in definition:
			return None
		else:
			if self.READABLE:
				return self._makeReadable(word, definition)
			else:
				return definition
	def _makeReadable(self,word, definition):
		structure = {"word":word,"translations":list(),"compound":list()}
		# Compute translations
		for category in definition:
			if re.match("term\d",category):
				for name in definition[category]:
					for tr in definition[category][name]:
						try:
							trans = {"original":definition[category][name][tr]["OriginalTerm"]["term"].decode('iso-8859-1').encode('utf8'),"translation":definition[category][name][tr]["FirstTranslation"]["term"].decode('iso-8859-1').encode('utf8')}
						except:
							trans = {"original":definition[category][name][tr]["OriginalTerm"]["term"].decode('iso-8859-1').encode('utf8')}
						structure["translations"].append(trans)
			elif re.match("original", category):
				for number in definition[category]["Compounds"]:
					compound = {"original":definition[category]["Compounds"][number]["OriginalTerm"]["term"].decode('iso-8859-1').encode('utf8'),"translation":unicode(definition[category]["Compounds"][number]["FirstTranslation"]["term"])}
					structure["compound"].append(compound)
		return structure


if __name__ == '__main__':
	print checkWordExists("Hola", "esen")
