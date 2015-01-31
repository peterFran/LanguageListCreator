from ebooklib import epub
from bs4 import BeautifulSoup
from langtools.SpanishTranslator import SpanishTranslator
from nltk.tokenize import RegexpTokenizer
from collections import Counter
from copy import copy

class EpubTranslationList(object):
	"""docstring for EpubTranslationList"""
	def __init__(self, book_location):
		super(EpubTranslationList, self).__init__()
		book = epub.read_epub(book_location)
		# Filter out pictures and the like
		self.chapters = [item for item in book.items if 'is_chapter' in dir(item)]
		self.title = book.title

	def get_chapter(self, number):
		# pass xml to ChapterTranslationList and return it
		chapter = self.chapters[number].get_content().decode('utf-8')
		return ChapterTranslationList(chapter)

class ChapterTranslationList(object):
	"""docstring for ChapterTranslationList"""
	def __init__(self, xml_chapter):
		super(ChapterTranslationList, self).__init__()

		# Tokenize the text
		self.text = BeautifulSoup(xml_chapter).get_text()
		tokenizer = RegexpTokenizer(r'\w+')
		tokenized_words = tokenizer.tokenize(self.text)

		# Get most and least common orderings
		self.most_common_words = Counter(tokenized_words).most_common()
		self.least_common_words = copy(self.most_common_words)
		self.least_common_words.reverse()

		# Get translator object
		self.translator = SpanishTranslator()

	def get_most_common(self, number_words):
		index = 0
		translated_words = []
		# Loop over the words in sorted dict
		for word in self.most_common_words:
			# If we haven't got enough words yet
			if index < number_words:
				# try to get a translation
				attempted = self.translator.translate_word(word[0])
				# if it works, add it to the list to be returned
				if attempted is not None:
					attempted['count'] = word[1]
					translated_words.append(attempted)
					index += 1
			else:
				break
		return translated_words
		
	def get_least_common(self, number_words):
		index = 0
		translated_words = []
		# Loop over the words in sorted dict
		for word in self.least_common_words:
			# If we haven't got enough words yet
			if index < number_words:
				# try to get a translation
				attempted = self.translator.translate_word(word[0])
				# if it works, add it to the list to be returned
				if attempted is not None:
					attempted['count'] = word[1]
					translated_words.append(attempted)
					index += 1
			else:
				break
		return translated_words
		
