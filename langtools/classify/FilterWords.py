from langtools.classify.tagger import TaggerFactory

class FilterWords(object):
    """docstring for FilterWords"""

    def __init__(self, words):
        self.tagger = TaggerFactory.factory("cess")
        self.words = words
        self.tagged_words_list = None

    def filtered_words(self, types=[]):

        """
        Returns a list of words filtered based on the
        :param types:
        :return:
        """
        filtered_words = []
        if len(types) == 0:
            return self.words
        else:
            filtered_words += [x[0] for x in self.tagged_words if x[1][0] in types and not x[0][0].isupper()]
        return filtered_words

    @property
    def tagged_words(self):
        """
        returns a list of tagged words
        :return:
        """
        if self.tagged_words_list is None:
            self.tagged_words_list = self.tagger.tag(self.words)
        return self.tagged_words_list