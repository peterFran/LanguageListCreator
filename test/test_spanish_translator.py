from langtools.translator.SpanishTranslator import SpanishTranslator
def test_nonexistent_word_returns_none():
	translator = SpanishTranslator()
	fetched_translation = translator.translate_word_full("zzzzzzz")
	assert fetched_translation == {'Error' : 'NoTranslation', 'Note' : 'No se ha encontrado ninguna traducción para zzzzzzz.\nNo translation was found for zzzzzzz.'}

def test_hola_returns_dict():
	translator = SpanishTranslator()
	fetched_translation = translator.translate_word("hola")
	assert fetched_translation == {"Word":"hola", "First Translation":'Hello!', "Second Translation":'hello', "First Compound":'¡Hola, chicos!', "First Compound Translation": 'hi, boys! hello, boys!', "Second Compound Translation":"Hello, people! Hi, folks!", "Second Compound": "¡Hola, gente!"}

def test_known_awkward_case():
	translator = SpanishTranslator()
	fetched_translation = translator.translate_word("enfrascar")
	assert fetched_translation is None

def test_utf8_word():
	translator = SpanishTranslator()
	fetched_translation = translator.translate_word("abolición")
	assert fetched_translation != None
	assert fetched_translation["First Translation"] == 'abolition'