from langtools.LanguageListCreator import LanguageListCreator
def test_length_list_correct():
	llc = LanguageListCreator()
	assert len(llc.random_verbs(10)) ==10
	assert len(llc.random_verbs(0)) == 0

def test_same_verb_not_produced_twice():
	llc = LanguageListCreator()
	assert llc.random_verbs(1) is not llc.random_verbs(1)

def test_required_fields_present():
	llc = LanguageListCreator()
	word = llc.random_verbs(1)[0]
	assert "Original Word" in word
	assert "First Translation" in word
	assert "Second Translation" in word
	assert "First Compound" in word
	assert "First Compound Translation" in word
	assert "Second Compound" in word
	assert "Second Compound Translation" in word
