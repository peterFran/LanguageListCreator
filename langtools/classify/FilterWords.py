import pkgutil
import pickle


class FilterWords(object):
    """docstring for FilterWords"""

    def __init__(self, words):
        print("Get tagger")
        self.tagger = pickle.loads(pkgutil.get_data('langtools', 'classify/tagger/class.pickle'))
        self.words = words
        print("Begin tagging")
        self.tagged_words = self.tagger.tag(words)
        print("End tagging")

    def get(self, types=[]):
        filtered_words = []
        if len(types) == 0:
            filtered_words += [x[0] for x in self.tagged_words]
        if "v" in types:
            filtered_words += [x[0] for x in self.tagged_words if x[1][0] == 'v' and not x[0][0].isupper()]
        if "n" in types:
            filtered_words += [x[0] for x in self.tagged_words if x[1][0] == 'n' and not x[0][0].isupper()]
        return filtered_words
