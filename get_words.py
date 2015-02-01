from langtools.EpubTranslationList import EpubTranslationList
from langtools.print_tools import print_untranslated_to_table

book = EpubTranslationList("resources/DonQuijote.epub")
print_untranslated_to_table(book.get_chapter(25).get_least_common(5))