from nltk.tokenize import RegexpTokenizer
from collections import Counter
from copy import copy
import pickle
from langtools.translator.SpanishTranslator import SpanishTranslator
from langtools.classify.FilterWords import FilterWords


class TextTranslation(object):
	"""docstring for ClassName"""
	def __init__(self, chapter):
		self.text = chapter
		
		# Tokenize the text
		tokenizer = RegexpTokenizer(r'\w+')
		self.tokenized_words = tokenizer.tokenize(self.text)

		# Get verbs nouns etc
		self.tagger = FilterWords(self.tokenized_words)
		
		# Get translator object
		self.translator = SpanishTranslator()
		


	def _get_n_words(self, number_words, ordered_tokens, translate=False):
		index = 0
		word_list = []
		# Loop over the words in sorted dict
		for word in ordered_tokens:
			# If we haven't got enough words yet
			if index < number_words:
				# try to get a translation
				attempted = self.translator.translate_word(word[0])
				# if it works, add it to the list to be returned
				if attempted is not None:
					attempted['Count'] = word[1]
					word_list.append(attempted)
					index += 1
			else:
				break
		return word_list

	def get(self, number_words, types=[], translate=False, reverse=False):
		tagged_words = Counter(self.tagger.get(types)).most_common()
		if reverse is True:
			tagged_words.reverse()
		
		if translate is True:
			return self._get_n_words(number_words, tagged_words)
		else:
			return[{'Word':word[0], 'Count':word[1]} for word in tagged_words][:number_words]
