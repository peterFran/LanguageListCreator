from ebooklib import epub
from bs4 import BeautifulSoup
from langtools.SpanishTranslator import SpanishTranslator


class EpubTranslationList(object):
	"""docstring for EpubTranslationList"""
	def __init__(self, book_location):
		super(EpubTranslationList, self).__init__()
		book = epub.read_epub(book_location)
		items = [item for item in book.items if 'is_chapter' in dir(item)]
		self.chapters = [(index, items) for enumerate(items)]
		self.title = book.title

	def get_chapter(self, number):
		chapter = items[number].get_content().decode('utf-8')
		return ChapterTranslationList(chapter)


class ChapterTranslationList(object):
	"""docstring for ChapterTranslationList"""
	def __init__(self, xml_chapter):
		super(ChapterTranslationList, self).__init__()
		self.text = BeautifulSoup(chapter).get_text()
		tokenizer = RegexpTokenizer(r'\w+')
		tokenized_words = tokenizer.tokenize(self.text)
		word_count = dict()
		# Get counts for word in chapters
		for word in tokenized_words:
			if word not in word_count:
				word_count[word]=0
			else:
				word_count[word] +=1
		self.counted_words = Counter(word_count).most_common()

	def get_most_common(self, number):
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
		
		
