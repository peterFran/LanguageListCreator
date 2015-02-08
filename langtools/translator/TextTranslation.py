from collections import Counter

from itertools import groupby

from nltk.tokenize import RegexpTokenizer

from langtools.translator.SpanishTranslator import SpanishTranslator
from langtools.classify.FilterWords import FilterWords


class TextTranslation(object):
    """docstring for ClassName"""

    def __init__(self, chapter):
        """

        :param chapter:
        """
        self.text = chapter

        # Tokenize the text
        tokenizer = RegexpTokenizer(r'\w+')
        self.token_words = tokenizer.tokenize(self.text)

        # Get verbs nouns etc
        self.tagger = FilterWords(self.token_words)

        # Get translator object
        self.translator = SpanishTranslator()

    def translate_n_words(self, number_words, ordered_tokens):
        """

        :param number_words:
        :param ordered_tokens:
        :return:
        """
        index = 0
        word_list = []
        # Loop over the words in sorted dict
        for word in ordered_tokens:
            # If we haven't got enough words yet
            if index < number_words:
                # try to get a translation
                attempted = self.translator.translate_word(word[0])
                # if it works, add it to the list to be returned
                if attempted is not None:
                    attempted['Count'] = word[1]
                    word_list.append(attempted)
                    index += 1
            else:
                break
        return word_list

    def get(self, number_words, types=[], ordered=False, translate=False, reverse=False):
        """

        :param number_words:
        :param types:
        :param translate:
        :param reverse:
        :return:
        """
        words = self.tagger.get(types)
        tagged_words = [(k, len(list(g))) for k, g in groupby(words)]
        if ordered is True:
            tagged_words = Counter(words).most_common()
        if reverse is True:
            tagged_words.reverse()

        if translate is True:
            return self.translate_n_words(number_words, tagged_words)
        else:
            return [{'Word': word[0], 'Count': word[1]} for word in tagged_words][:number_words]