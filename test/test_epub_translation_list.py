from langtools.translator.EPUBTranslation import EPUBTranslation


def test_epub_stemming():
    book = EPUBTranslation("resources/DonQuijote.epub")
    print(book.get_chapter(25).get_least_common(5))