from pytest import *
from SpanishDictionary import SpanishDictionary
def test_dictionary_loads():
	dic = SpanishDictionary('/home/peter/Development/llc/LanguageListCreator/dic/es.dic')
	print(dic.dictionary)
	assert len(dic.dictionary) > 0

