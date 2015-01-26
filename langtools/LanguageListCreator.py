from langtools.SpanishDictionary import SpanishDictionary
from langtools.SpanishTranslator import SpanishTranslator

class LanguageListCreator(object):
	def __init__(self, wordreference_api_key='8a8bc'):
		self.dictionary = SpanishDictionary()
		self.translator = SpanishTranslator(wordreference_api_key)

	def random_verbs(self, number):
		word_array = dict()
		for i in range(0,number):
			translated_word, word = None, None
			while translated_word is None:
				word = self.dictionary.get_random_verb()
				if word not in word_array:
					translated_word = self.translator.translate_word(word)
			word_array[word]=translated_word
		return list(word_array.values())

if __name__ == '__main__':
	llc = LanguageListCreator()
