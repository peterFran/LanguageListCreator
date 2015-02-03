from ebooklib import epub
from bs4 import BeautifulSoup
from langtools.SpanishTranslator import SpanishTranslator
from nltk.tokenize import RegexpTokenizer
from collections import Counter
from copy import copy
import pickle

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




class TextTranslationList(object):
	"""docstring for ClassName"""
	def __init__(self, chapter):
		self.text = chapter
		# Tokenize the text
		
		tokenizer = RegexpTokenizer(r'\w+')
		tokenized_words = tokenizer.tokenize(self.text)
		
		# Tag words
		
		class_tagger = None
		try:
			with open('class.pickle', 'rb') as fa:
				class_tagger = pickle.load(fa)
		except FileNotFoundError as a:
		    # training data
		    print("Language Tagger does not exist in memory, recreating tagger")
		    from nltk.tag.sequential import ClassifierBasedPOSTagger
		    from nltk.corpus import cess_esp
		    class_tagger = ClassifierBasedPOSTagger(train=cess_esp.tagged_sents())

		    with open('class.pickle', 'wb') as fb:
		        pickle.dump(class_tagger, fb)


		# Get most and least common orderings
		self.most_common_words = Counter(tokenized_words).most_common()
		self.least_common_words = copy(self.most_common_words)
		self.least_common_words.reverse()

		# Tag words
		self.tagged_words = class_tagger.tag(tokenized_words)
		self.verbs = Counter([x[0] for x in self.tagged_words if x[1][0] == 'v']).most_common()
		print(self.verbs)
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

	def get_verbs(self,number_words, translate=False):
		return self._get_n_words(number_words,self.verbs,translate)
		
class ChapterTranslationList(TextTranslationList):
	"""docstring for ChapterTranslationList"""
	def __init__(self, xml_chapter):
		chapter = BeautifulSoup(xml_chapter).get_text()
		TextTranslationList.__init__(self, chapter)