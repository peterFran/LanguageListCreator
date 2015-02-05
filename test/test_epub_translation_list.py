from langtools.translator.EpubTranslation import EpubTranslation

def test_epub_stemming():
	book = EpubTranslation("resources/DonQuijote.epub")
	print(book.get_chapter(25).get_least_common(5))