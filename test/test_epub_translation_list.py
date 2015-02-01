from langtools.EpubTranslationList import EpubTranslationList

def test_epub_stemming():
	book = EpubTranslationList("resources/DonQuijote.epub")
	print(book.get_chapter(25).get_least_common(5))