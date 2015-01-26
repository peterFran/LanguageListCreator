from .LanguageDictionary.SpanishDictionary import SpanishDictionary
from .Translator.SpanishTranslator import SpanishTranslator

class LanguageListCreator(object):
	def __init__(self):
		self.dictionary = SpanishDictionary("dic/es.dic")
		self.translator = SpanishTranslator()

	def random_verbs(self, number):
		word_array = dict()
		for i in range(0,number):
			translated_word, word = None, None
			while translated_word is None:
				word = self.dictionary.get_random_verb()
				if word not in word_array:
					translated_word = self.translator.translate_word(word)
			word_array[word]=translated_word
		return word_array