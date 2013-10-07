import os, sys, inspect
from data.QueryLocalDB import LanguageDatabase
from data.WordReference import getWordDefinitionWithCheck

def daily_list(number_words, language_known, language_learning, dictionary="wiktionary"):
	dictionary_code = "esen"#get_dict_code(language_know, language_learning, dictionary)
	languagedb = LanguageDatabase()
	word_list = dict()
	for word in languagedb.getNewWords(10):
		definition = getWordDefinitionWithCheck(word, dictionary_code)
		while definition is None:
			word = languagedb.getNewWord()
			definition = getWordDefinitionWithCheck(word, dictionary_code)
		languagedb.qualify(word)
		word_list[word]=definition
	# return 3 lists
	return word_list

# def daily_list_pdf(number_words, language_known, language_learning, dictionary="wiktionary"):
# 	(word_list,words_only_list,definitions_only_list)=daily_list(number_words, language_known, language_learning, dictionary=dictionary)	
# 	latex_code = get_latex(timeframe="Daily",full=word_list,words=words_only_list,definitions=definitions_only_list)
# 	pdf_object = get_pdf_from_latex(latex_code)
# 	return pdf_object

if __name__ == '__main__':
	for i in daily_list(10,"en","es"):
		print i