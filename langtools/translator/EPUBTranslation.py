from ebooklib import epub
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer

from langtools.translator.TextTranslation import TextTranslation


class EPUB(object):
    """docstring for EPUB"""

    def __init__(self, book_location):
        book = epub.read_epub(book_location)
        # Filter out pictures and the like
        self.chapters = [item for item in book.items if 'is_chapter' in dir(item)]
        self.title = book.title

    def get_chapter(self, number):
        # pass xml to ChapterTranslationList and return it
        xml_chapter = self.chapters[number].get_content().decode('utf-8')
        chapter = BeautifulSoup(xml_chapter).get_text()
        # Tokenize the text
        tokenizer = RegexpTokenizer(r'\w+')
        return tokenizer.tokenize(chapter)


class EPUBTranslation(EPUB):
    """docstring for EpubTranslation"""

    def get_chapter(self, number):
        # pass xml to ChapterTranslationList and return it
        xml_chapter = self.chapters[number].get_content().decode('utf-8')
        chapter = BeautifulSoup(xml_chapter).get_text()
        return TextTranslation(chapter)


