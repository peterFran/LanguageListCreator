#!/usr/bin/env python
from langtools.translator.EPUBTranslation import EPUBTranslation
from langtools.print_tools import print_list_to_terminal, print_untranslated_to_table
from optparse import OptionParser
# create a subclass and override the handler methods

parser = OptionParser()
parser.add_option("-f", "--file",
                  dest="filename",
                  help="location of EPUB",
                  action="store",
                  type="string",
                  default=None)
parser.add_option("-c", "--chapter",
                  action="store",
                  dest="chapter",
                  help="Which chapter would you like to load",
                  type="int",
                  default=None)
parser.add_option("-r", "--reverse",
                  dest="reverse",
                  help="see least common words",
                  action="store_true",
                  default=False)
parser.add_option("-q", "--quantity",
                  action="store",
                  dest="quantity",
                  type="int",
                  help="number of words you'd like to see.",
                  default=5)
parser.add_option("-t", "--translate",
                  action="store_true",
                  dest="translate",
                  help="flag to attempt translations",
                  default=False)
parser.add_option("-v", "--verbs",
                  action="store_true",
                  dest="verbs",
                  help="flag to show verbs",
                  default=False)
parser.add_option("-n", "--nouns",
                  action="store_true",
                  dest="nouns",
                  help="flag to show nouns",
                  default=False)
parser.add_option("-o", "--ordered",
                  action="store_true",
                  dest="ordered",
                  help="flag to order by most common",
                  default=False)
parser.add_option("-s", "--start",
                  action="store",
                  dest="start",
                  type="int",
                  help="starting point",
                  default=0)

(options, args) = parser.parse_args()
if options.filename is not None:
    book = EPUBTranslation(options.filename)
    if options.chapter is None:
        print("Imported {0}, please select which chapter to read".format(book.title))

        for index, item in enumerate(book.chapters):
            print("{0}. {1}".format(index, item.get_name()))
    else:
        chapter = book.get_chapter(options.chapter)
        words = []
        types = []

        if options.verbs is True:
            types.append("v")
        elif options.nouns is True:
            types.append("n")
        words = chapter.get(options.quantity, start=options.start, types=types, ordered=options.ordered,
                            translate=options.translate, reverse=options.reverse)
        if options.translate:
            print_list_to_terminal(words)
        else:
            print_untranslated_to_table(words)

if __name__ == "__main__":
    from langtools.translator.EPUBTranslation import EPUBTranslation

    book = EPUBTranslation("../resources/ElJuegoDelAngel.epub")
    chapter = book.get_chapter(0)
    words = chapter.get(3, 3, ['n'], False, True, False)