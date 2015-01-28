from langtools.SpanishDictionary import SpanishDictionary
from langtools.SpanishTranslator import SpanishTranslator
import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.tokenize import RegexpTokenizer



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

	def random_words(self,number):
		word_array = dict()
		for i in range(0,number):
			translated_word, word = None, None
			while translated_word is None:
				word = self.dictionary.get_random_word()
				if word not in word_array:
					translated_word = self.translator.translate_word(word)
			word_array[word]=translated_word
		return list(word_array.values())

	def get_list_from_file(self, path_to_file):
		tokenizer = RegexpTokenizer(r'\w+')
		text = open(path_to_file, 'r').read()
		tokenized_words = tokenizer.tokenize(text)[:50]
		word_array = dict()
		for word in tokenized_words:
			if word not in word_array:
				translated_word = self.translator.translate_word(word)
				if translated_word is not None:
					word_array[word]=translated_word
		return list(word_array.values())







