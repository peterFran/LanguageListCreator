import arrow
from QueryLocalDB import get_lists
#TODO Finish this
def get_all_lists(language="*"):
	time_object = arrow.now()
	previous_month_lists = get_lists(language, time_object.timestamp, time_object.replace(months=-1).timestamp)
	dictionary_code = get_dict_code(language_know, language_learning, dictionary)
	word_list = get_unused_words(number_words, language_learning)
	word_dict = get_word_list(dictionary, dictionary_language_code, word_list)
	words_dict = get_wor
	return previous_month_lists

def get_previous_month_pdf(language="*"):
	previous_month_lists = get_all_lists(language)
	latex_code = get_latex(timeframe="Monthly Review", full=word_list)
        pdf_object = get_pdf_from_latex(latex_code)
