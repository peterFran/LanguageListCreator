from nltk.tokenize import RegexpTokenizer
from collections import Counter
from copy import copy
import pickle
from langtools.translator.SpanishTranslator import SpanishTranslator


class TextTranslation(object):
	"""docstring for ClassName"""
	def __init__(self, chapter):
		self.text = chapter
		self.tagged_words = None
		self.verbs = None
		self.least_common_verbs = None
		# Tokenize the text
		
		tokenizer = RegexpTokenizer(r'\w+')
		self.tokenized_words = tokenizer.tokenize(self.text)
		
		# Tag words
		
		self.class_tagger = None
		try:
			with open('class.pickle', 'rb') as fa:
				self.class_tagger = pickle.load(fa)
		except FileNotFoundError as a:
		    # training data
		    print("Language Tagger does not exist in memory, recreating tagger")
		    from nltk.tag.sequential import ClassifierBasedPOSTagger
		    from nltk.corpus import cess_esp
		    self.class_tagger = ClassifierBasedPOSTagger(train=cess_esp.tagged_sents())

		    with open('class.pickle', 'wb') as fb:
		        pickle.dump(self.class_tagger, fb)

		print("Finding most and least common words...")
		# Get most and least common orderings
		self.most_common_words = Counter(self.tokenized_words).most_common()
		self.least_common_words = copy(self.most_common_words)
		self.least_common_words.reverse()

		

		print("Word processing finished, begin translation")
		# Get translator object
		self.translator = SpanishTranslator()

	def _get_n_words(self, number_words, ordered_tokens, translate=False):
		index = 0
		word_list = []
		# Loop over the words in sorted dict
		for word in ordered_tokens:
			# If we haven't got enough words yet
			if index < number_words:
				# If we want a translation
				if translate is True:
					# try to get a translation
					attempted = self.translator.translate_word(word[0])
					# if it works, add it to the list to be returned
					if attempted is not None:
						attempted['Count'] = word[1]
						word_list.append(attempted)
						index += 1
				else:
					attempted={'Word':word[0], 'Count':word[1]}
					attempted['Word'] = word[0]
					attempted['Count'] = word[1]
					word_list.append(attempted)
					index += 1
			else:
				break
		return word_list

	def get_most_common(self, number_words, translate=False):
		return self._get_n_words(number_words,self.most_common_words,translate)
		
	def get_least_common(self, number_words, translate=False):
		return self._get_n_words(number_words,self.least_common_words,translate)

	def get_most_common_verbs(self,number_words, translate=False):
		# Tag words
		print("Filtering out verbs....")
		if self.tagged_words is None:
			self.tagged_words = self.class_tagger.tag(self.tokenized_words)
		if self.verbs is None:
			self.verbs = Counter([x[0] for x in self.tagged_words if x[1][0] == 'v']).most_common()

		return self._get_n_words(number_words,self.verbs,translate)

	def get_least_common_verbs(self,number_words, translate=False):
		# Tag words
		print("Filtering out verbs....")
		if self.tagged_words is None:
			self.tagged_words = self.class_tagger.tag(self.tokenized_words)
		if self.verbs is None:
			self.verbs = Counter([x[0] for x in self.tagged_words if x[1][0] == 'v']).most_common()
		
		if self.least_common_verbs is None:
			self.least_common_verbs = copy(self.verbs)
			self.least_common_verbs.reverse()
		return self._get_n_words(number_words,self.least_common_verbs,translate)
		
