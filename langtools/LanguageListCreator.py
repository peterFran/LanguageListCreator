from langtools.SpanishDictionary import SpanishDictionary
from langtools.SpanishTranslator import SpanishTranslator
import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.tokenize import RegexpTokenizer
from collections import Counter



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

	def get_list_from_file(self, path_to_file, num):
		tokenizer = RegexpTokenizer(r'\w+')
		text = open(path_to_file, 'r').read()
		tokenized_words = tokenizer.tokenize(text)[:num]
		word_dict = dict()
		word_count = dict()
		word_list = list()
		for word in tokenized_words:
			if word not in word_dict:
				translated_word = self.translator.translate_word(word)
				if translated_word is not None:
					word_dict[word]=translated_word
					word_count[word]=0
			else:
				word_count[word] +=1
		print(word_count)
		word_list = [word_dict[word] for word in sorted(word_count, key=word_count.get, reverse=True)]
		return word_list

	def get_list_from_text(self, text, num):
		tokenizer = RegexpTokenizer(r'\w+')
		tokenized_words = tokenizer.tokenize(text)
		#print(tokenized_words)
		word_dict = dict()
		word_count = dict()
		word_list = list()
		for word in tokenized_words:
			if word not in word_count:
				word_count[word]=0
			else:
				word_count[word] +=1
		counted = Counter(word_count).most_common()
		index = 0
		translated_words = []
		for word in counted:
			if index < num:
				print(word)
				attempted = self.translator.translate_word(word[0])
				if attempted is not None:
					translated_words.append(attempted)
					index += 1
			else:
				break
		return translated_words






