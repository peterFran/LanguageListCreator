import re
import random
import pkgutil


class SpanishDictionary(object):
    dictionary = list()

    def __init__(self, ):
        contents = pkgutil.get_data('langtools', 'dictionary/dic/es.dic').decode('utf-8')
        self.dictionary = [line.split("/")[0] for line in contents.split("\n") if
                           not re.search("\d|\?", line, re.U) and line.split("/")[0] is not ""]

    def all_verbs(self, ):
        all_verbs = [word for word in self.dictionary if not word[0].isupper() and re.match(".*[i|e|a]r$", word)]
        return all_verbs

    def get_random_word(self):
        return self.dictionary[random.randrange(0, len(self.dictionary))]

    def get_random_verb(self):
        return self.all_verbs()[random.randrange(0, len(self.all_verbs()))]
