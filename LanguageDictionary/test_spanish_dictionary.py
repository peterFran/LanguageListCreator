import re, pytest, urllib, pprint
from SpanishDictionary import SpanishDictionary

@pytest.fixture
def dic():
	import os
	directory = os.path.dirname(__file__)
	filename = os.path.join(directory, '../dic/es.dic')
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
	assert len(dic.get_random_word_translated()) > 0
	assert len(dic.get_random_word_translated()) > 0

def test_random_translated_word_exists(dic):
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(dic.get_random_word_translated())


