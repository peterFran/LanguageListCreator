from ebooklib import epub
from bs4 import BeautifulSoup
from langtools.translator.TextTranslation import TextTranslation


class EpubTranslation(object):
	"""docstring for EpubTranslation"""
	def __init__(self, book_location):
		book = epub.read_epub(book_location)
		# Filter out pictures and the like
		self.chapters = [item for item in book.items if 'is_chapter' in dir(item)]
		self.title = book.title

	def get_chapter(self, number):
		# pass xml to ChapterTranslationList and return it
		chapter = self.chapters[number].get_content().decode('utf-8')
		return ChapterTranslation(chapter)

	
class ChapterTranslation(TextTranslation):
	"""docstring for ChapterTranslation"""
	def __init__(self, xml_chapter):
		chapter = BeautifulSoup(xml_chapter).get_text()
		TextTranslation.__init__(self, chapter)