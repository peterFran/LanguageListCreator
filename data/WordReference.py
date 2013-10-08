# coding=UTF-8
import json
from urllib2 import urlopen
import urllib2
import re

class WordReferenceDefinition(object):
	# Readable flag, set if you want to be able to understand ANYTHING
	READABLE = False
	def getWordDefinitionAsDict(self, word, dictionary_code):
		print word
		url_word = word# urllib2.quote(word)
		if isinstance(dictionary_code, unicode):
			print "woohoo"
		url = u"http://api.wordreference.com/0.8/8a8bc/json/"+dictionary_code+u'/'+url_word
		print url
		try:
			result = urlopen(url).read().encode('utf-8').rstrip()
			print result
			return json.loads(result)
		except urllib2.URLError, e:
			print url
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
		print word
		structure = {"word":word,"translations":list(),"compound":list()}
		# Compute translations
		for category in definition:
			if re.match("term\d",category):
				for name in definition[category]:
					for tr in definition[category][name]:
						trans = {"original":definition[category][name][tr]["OriginalTerm"]["term"],}
						if "FirstTranslation" in definition[category][name][tr]:
							trans["translation"]=definition[category][name][tr]["FirstTranslation"]["term"]
						else:
							trans["translation"]="None available"
						structure["translations"].append(trans)
			elif re.match("original", category):
				for number in definition[category]["Compounds"]:
					compound = {"original":definition[category]["Compounds"][number]["OriginalTerm"]["term"],"translation":definition[category]["Compounds"][number]["FirstTranslation"]["term"]}
					structure["compound"].append(compound)
		return structure


if __name__ == '__main__':
	wr = WordReferenceDefinition()
	wr.READABLE=True

	print wr.getWordDefinitionWithCheck("apolíneo", "esen")['translations'][0]['original']
