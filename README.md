LanguageListCreator
===================

The project is designed to take an EPUB book and output a lest of translated words in a given chapter.

The problem that this project is aimed to solve is the inability of a reader to fully enjoy a story if their primary concern is learning new vocabulary.

The tool outputs a list of most comminly used words in the chapter, with translations.

example usage
./epub_tools.py -f resources/DonQuijote.epub -c24 -v -q20
This returns the 20 most common verbs from the book Don Quijote

Main tools
/langtools
	/dictionary
		- SpanishDictionary.py
	/translator
		- SpanishTranslator.py
		- TextTranslation.py
	- epub_tools.py
	- print_tools.py
