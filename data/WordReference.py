# coding=UTF-8
import json
from urllib2 import urlopen
import urllib2, re


class WordReferenceDefinition(object):
	# Readable flag, set if you want to be able to understand ANYTHING
	READABLE = False
	def getWordDefinitionAsDict(self, word, dictionary_code):
		# Use quote method to percent encode, after first encoding utf with hex
		url_word = urllib2.quote(word.encode('utf-8').rstrip())
		url = "http://api.wordreference.com/0.8/8a8bc/json/%s/%s" %(dictionary_code, url_word)
		try:
			# Get the JSON from the web server
			result = urlopen(url).read().rstrip()
			return json.loads(result)
		except urllib2.URLError, e:
			return None
		except ValueError, e:
			return None
	def getWordDefinitionWithCheck(self, word, dictionary_code):
		definition = self.getWordDefinitionAsDict(word, dictionary_code)
		# The first 3 here all me the word isn't valid
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
		# The structure of the dictionary
		structure = {"word":word,"translations":list(),"compound":list()}
		# These variables act as a mechanism to check that a translation is not repeated
		translation_set = set()
		compound_set = set()
		# This is just taking the convoluted word reference JSON and making it simpler
		for category in definition:
			if re.match("term\d",category):
				for name in definition[category]:
					for tr in definition[category][name]:
						trans = {"original":definition[category][name][tr]["OriginalTerm"]["term"],}
						if "FirstTranslation" in definition[category][name][tr]:
							trans["translation"]=definition[category][name][tr]["FirstTranslation"]["term"]
						else:
							trans["translation"]="None available"
						# These few lines prevent repetitions by not allowing any that don't expand a set
						# (And are therefore already existent in the set)
						before = len(translation_set)
						translation_set.add(trans["original"]+trans["translation"])
						after = len(translation_set)
						if before < after:
							structure["translations"].append(trans)
			elif re.match("original", category):
				for number in definition[category]["Compounds"]:
					compound = {"original":definition[category]["Compounds"][number]["OriginalTerm"]["term"],"translation":definition[category]["Compounds"][number]["FirstTranslation"]["term"]}
					
					# These few lines prevent repetitions by not allowing any that don't expand a set
					# (And are therefore already existent in the set)
					before = len(compound_set)
					compound_set.add(compound["original"]+compound["translation"])
					after = len(compound_set)
					if before < after:
						structure["compound"].append(compound)
		return structure


if __name__ == '__main__':
	wr = WordReferenceDefinition()
	wr.READABLE=True

	print wr.getWordDefinitionWithCheck("hijito", "esen")
