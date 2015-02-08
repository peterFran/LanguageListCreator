import json
from urllib.parse import quote
from urllib.request import urlopen
from urllib.request import URLError


class SpanishTranslator(object):
    def __init__(self, wordreference_api_key='8a8bc'):
        self.url = "http://api.wordreference.com/0.8/{0}/json/esen/".format(wordreference_api_key) + "{0}"

    def translate_word_full(self, word):
        # Use quote method to percent encode, after first encoding utf with hex
        word_url = self.url.format(quote(word))
        try:
            # Get the JSON from the web server
            raw_json_result = urlopen(word_url).read().rstrip()
            result = json.loads(raw_json_result.decode())
            return result
        except URLError as e:
            return None
        except ValueError as e:
            return None

    def translate_word(self, word):
        word_object = self.translate_word_full(word)
        word_dict = {"Word": word, "First Translation": None, "Second Translation": None, "First Compound": None,
                     "First Compound Translation": None, "Second Compound": None, "Second Compound Translation": None}
        # Get primary
        try:
            word_dict['First Translation'] = word_object['term0']['PrincipalTranslations']['0']['FirstTranslation'][
                'term']
        except KeyError as k:
            return None

        # Get secondary translations
        try:
            word_dict['Second Translation'] = word_object['term0']['PrincipalTranslations']['1']['FirstTranslation'][
                'term']
        except KeyError as k:
            pass

        # Get compounds
        try:
            word_dict["First Compound"] = word_object['original']['Compounds']['0']['OriginalTerm']['term']
            word_dict["First Compound Translation"] = word_object['original']['Compounds']['0']['FirstTranslation'][
                'term']
            word_dict["Second Compound"] = word_object['original']['Compounds']['1']['OriginalTerm']['term']
            word_dict["Second Compound Translation"] = word_object['original']['Compounds']['1']['FirstTranslation'][
                'term']
        except KeyError as k:
            pass

        return word_dict