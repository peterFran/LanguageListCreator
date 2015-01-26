import re, pytest, urllib, pprint
from unittest.mock import Mock
from .LanguageDictionary.SpanishDictionary import SpanishDictionary
from .Translator.SpanishTranslator import SpanishTranslator

@pytest.fixture
def dic():
	import os
	directory = os.path.dirname(__file__)
	filename = os.path.join(directory, 'dic/es.dic')
	return SpanishDictionary(filename)

def test_no_numbers(dic):
	words_containing_nums =[x for x in dic.dictionary if not re.search("\w",x)]
	assert words_containing_nums == []

def test_verbs_less_than_half(dic):
	assert len(dic.all_verbs()) < len(dic.dictionary)/5

def test_artifacts_not_null(dic):
	assert len(dic.dictionary) > 0
	assert len(dic.get_random_word()) > 0
	assert len(dic.get_random_verb()) > 0



def test_nonexistent_word_returns_none(dic):
	translator = SpanishTranslator()
	fetched_translation = translator.translate_word_full("zzzzzzz")
	assert fetched_translation == {'Error' : 'NoTranslation', 'Note' : 'No se ha encontrado ninguna traducción para zzzzzzz.\nNo translation was found for zzzzzzz.'}

def test_hola_returns_dict(dic):
	translator = SpanishTranslator()
	fetched_translation = translator.translate_word("hola")
	assert fetched_translation == "Hello!"

def test_known_awkward_case(dic):
	translator = SpanishTranslator()
	fetched_translation = translator.translate_word("enfrascar")
	assert fetched_translation is None

# def test_get_list_translations(dic):
# 	translator = SpanishTranslator()
# 	#pp = pprint.PrettyPrinter(indent=2)
# 	#pp.pprint([{word:translator.translated_word(word)} for word in [dic.get_random_verb() for i in range(0,10)]])
# 	for i in range(0,10):
# 		translated_word, word = None, None
# 		while translated_word is None:
# 			word = dic.get_random_verb()
# 			translated_word = translator.translate_word(word)
# 		print(word+" --- "+translated_word)
