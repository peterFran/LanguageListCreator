import json
from urllib2 import urlopen

def getWordDefinitionAsDict(word, dictionary_code):
	url = "http://api.wordreference.com/0.8/8a8bc/json/%s/%s" % (dictionary_code,word)
	try:
		result = urlopen(url).read()
		print result
		return json.loads(result)
	except urllib2.URLError, e:
		return None

if __name__ == '__main__':
	getWordDefinitionAsDict("bonjour", "fren")
