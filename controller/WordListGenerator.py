# coding=UTF-8

import os, sys, inspect
from data.QueryLocalDB import LanguageDatabase
from data.WordReference import WordReferenceDefinition

def daily_list(number_words, language_known, language_learning, dictionary="wiktionary"):
	dictionary_code = language_learning+language_known
	languagedb = LanguageDatabase(language_learning)
	wordRef = WordReferenceDefinition()
	wordRef.READABLE = True
	word_list = list()
	for word in languagedb.getNewWords(number_words):
		definition = wordRef.getWordDefinitionWithCheck(word, dictionary_code)
		while definition is None:
			word = languagedb.getNewWord()
			definition = wordRef.getWordDefinitionWithCheck(word, dictionary_code)
		languagedb.qualify(word)
		word_list.append(definition)
	# return 3 lists
	return word_list

def periodic_revision(language_learning, days=0,weeks=0,months=0,years=0):
	languagedb = LanguageDatabase(language_learning)
	return languagedb.getWordsInPeriod(d=days+weeks*7,m=months,y=years)

# def daily_list_pdf(number_words, language_known, language_learning, dictionary="wiktionary"):
# 	(word_list,words_only_list,definitions_only_list)=daily_list(number_words, language_known, language_learning, dictionary=dictionary)	
# 	latex_code = get_latex(timeframe="Daily",full=word_list,words=words_only_list,definitions=definitions_only_list)
# 	pdf_object = get_pdf_from_latex(latex_code)
# 	return pdf_object

if __name__ == '__main__':
	for i in daily_list(10,"en","es"):
		print i
