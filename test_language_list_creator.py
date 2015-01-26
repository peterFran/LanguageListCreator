import re, pytest, pprint
from LanguageListCreator.LanguageListCreator import LanguageListCreator
def test_length_list_correct():
	llc = LanguageListCreator()
	assert len(llc.random_verbs(10)) ==10
	assert len(llc.random_verbs(0)) == 0
	