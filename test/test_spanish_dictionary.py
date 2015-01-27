from langtools.SpanishDictionary import SpanishDictionary
import pytest, re
@pytest.fixture
def dic():
	dic = SpanishDictionary()
	assert len(dic.dictionary) > 0
	return dic

def test_no_numbers(dic):
	words_containing_nums =[x for x in dic.dictionary if not re.search("\w",x)]
	assert words_containing_nums == []

def test_verbs_less_than_half(dic):
	assert len(dic.all_verbs()) < len(dic.dictionary)/5

def test_artifacts_not_null(dic):
	assert len(dic.dictionary) > 0
	assert len(dic.get_random_word()) > 0
	assert len(dic.get_random_verb()) > 0







