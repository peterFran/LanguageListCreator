from langtools.translator.EPUBTranslation import EPUBTranslation


def test_epub_stemming():
    book = EPUBTranslation("resources/DonQuijote.epub")
    assert len(book.get_chapter(25).get(10)) == 10
