import json, re
class DictionaryReduce(object):
	def _find_reduced_file(self, language):
		try:
			with open("dic/%s_reduced.dic" % language) as dic:
				contents = dic.read()
				return json.loads(contents)
		except IOError:
			print "worked"
			return None
	def _create_reduced_file(self, language, ignore_existing=False):
		print "create reduced"
		if ignore_existing is False:
			dic = self._find_reduced_file(language)
			if dic is not None:
				return dic
		with open("dic/%s.dic" % language, 'r') as dictionary_file:
			print "getting there"
			try:
				if language == "es":
					contents = dictionary_file.read().rstrip()
					oldline = ""
					dic = list()
					for line in contents.split("\n"):
						if not re.search("\d|\?", line, re.U) and line.split("/")[0] is not "":
							word = line.split("/")[0].decode('iso-8859-1')
							ending = line.rstrip("s").rstrip("o|a|e")
							if ending != oldline:
								dic.append(word)
								oldline = ending
				elif language=="it":
					contents = dictionary_file.read().rstrip()
					oldline = ""
					dic = list()
					for line in contents.split("\n"):
						if not re.search("\d|\?", line, re.U) and line.split("/")[0] is not "":
							word = line.split("/")[0].decode('iso-8859-1')
							ending = line.rstrip("o|a|e|i")
							if ending != oldline:
								dic.append(word)
								oldline = ending
				with open("dic/%s_reduced.dic" % language, "a") as dic_reduced:
					dic_reduced.write(json.dumps(dic))
				return self._find_reduced_file(language)
			except IOError:
				return None
			
	def getDictionary(self, language):
		reduced_dictionary = self._find_reduced_file(language)
		if reduced_dictionary is None:
			reduced_dictionary = self._create_reduced_file(language)
			if reduced_dictionary is None:
				return None
		return reduced_dictionary
