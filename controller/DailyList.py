from GetWordLists import get_word_list
from DictionaryOps import get_dict_code, strip_definitions, strip_words
from get_latex import get_latex
from QueryLocalDB import add_list

def daily_list(number_words, language_known, language_learning, dictionary="wiktionary"):
	dictionary_code = get_dict_code(language_know, language_learning, dictionary)
	word_list = get_unused_words(number_words, language_learning)
	word_dict = get_word_list(dictionary, dictionary_language_code, word_list)
	add_list(word_list)
	words_list = strip_definitions(word_list)
	definitions_only_list = strip_words(word_dict)
	# return 3 lists
	return word_dict,word_list,definitions_only_list

def daily_list_pdf(number_words, language_known, language_learning, dictionary="wiktionary"):
	(word_list,words_only_list,definitions_only_list)=daily_list(number_words, language_known, language_learning, dictionary=dictionary)	
	latex_code = get_latex(timeframe="Daily",full=word_list,words=words_only_list,definitions=definitions_only_list)
	pdf_object = get_pdf_from_latex(latex_code)
	return pdf_object
