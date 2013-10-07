import os, sys, inspect
from data.QueryLocalDB import LanguageDatabase
from data.WordReference import WordReferenceDefinition

def daily_list(number_words, language_known, language_learning, dictionary="wiktionary"):
	dictionary_code = "esen"#get_dict_code(language_know, language_learning, dictionary)
	languagedb = LanguageDatabase()
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

# def daily_list_pdf(number_words, language_known, language_learning, dictionary="wiktionary"):
# 	(word_list,words_only_list,definitions_only_list)=daily_list(number_words, language_known, language_learning, dictionary=dictionary)	
# 	latex_code = get_latex(timeframe="Daily",full=word_list,words=words_only_list,definitions=definitions_only_list)
# 	pdf_object = get_pdf_from_latex(latex_code)
# 	return pdf_object

if __name__ == '__main__':
	for i in daily_list(10,"en","es"):
		print i
