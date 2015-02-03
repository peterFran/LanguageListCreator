from nltk.corpus import cess_esp as cess
from nltk import RegexpTokenizer
import nltk
import pickle

# My sentences
sentence = "hola, hola, soy Pedro ¿como te llamas?."
tokenizer = RegexpTokenizer(r'\w+')
tokenized_words = tokenizer.tokenize(sentence)

# Dec train/test
train = None
test = None
cess_sents = cess.tagged_sents()
try:
    with open('test_pickles/test_data.pickle', 'rb') as fa:
        div = pickle.load(fa)
        train = cess_sents[:div]
        test = cess_sents[div+1:]
except FileNotFoundError as a:
    # training data
    print("dumping train/test")
    div = len(cess_sents)*90//100
    train = cess_sents[:div]
    test = cess_sents[div+1:]

    with open('test_pickles/test_data.pickle', 'wb') as fb:
        pickle.dump(div, fb)

#####
#
# 1 ubt tagger
#
#####
def backoff_tagger(tagged_sents, tagger_classes, backoff=None):
    if not backoff:
        backoff = tagger_classes[0](tagged_sents)
        del tagger_classes[0]
 
    for cls in tagger_classes:
        tagger = cls(tagged_sents, backoff=backoff)
        backoff = tagger
 
    return backoff
print("started ubt")
from nltk import UnigramTagger, TrigramTagger, RegexpTokenizer
ubt_tagger = None
try:
    with open('test_pickles/ubt.pickle', 'rb') as fa:
        ubt_tagger = pickle.load(fa)
except FileNotFoundError as a:
    # training data
    print("dumping ubt")
    ubt_tagger = backoff_tagger(train, [nltk.tag.UnigramTagger, nltk.tag.BigramTagger, nltk.tag.TrigramTagger])

    with open('test_pickles/ubt.pickle', 'wb') as fb:
        pickle.dump(ubt_tagger, fb)
#print(ubt_tagger.evaluate(test))
print(ubt_tagger.tag(tokenized_words))

#####
#
# 2 brill tagger
#
#####
# from nltk.tag_util import train_brill_tagger
# brill_tagger = None
# try:
#     with open('test_pickles/brill.pickle', 'rb') as fa:
#         brill_tagger = pickle.load(fa)
# except FileNotFoundError as a:
#     # training data
#     print("dumping brill")
#     brill_tagger = train_brill_tagger(ubt_tagger, train)

#     with open('test_pickles/brill.pickle', 'wb') as fb:
#         pickle.dump(brill_tagger, fb)
# print(brill_tagger.evaluate(test))

#####
#
# 3 classified tagger
#
#####
from nltk.tag.sequential import ClassifierBasedPOSTagger
print("started classified")
class_tagger = None
try:
    with open('test_pickles/class.pickle', 'rb') as fa:
        class_tagger = pickle.load(fa)
except FileNotFoundError as a:
    # training data
    print("dumping class")
    class_tagger = ClassifierBasedPOSTagger(train=train)

    with open('test_pickles/class.pickle', 'wb') as fb:
        pickle.dump(class_tagger, fb)
#print(class_tagger.evaluate(test))
print(class_tagger.tag(tokenized_words))
####
#
# 4 TnT
#
####
print("started tnt")
from nltk.tag import tnt
tnt_tagger = None

try:
    with open('test_pickles/tnt.pickle', 'rb') as fa:
        tnt_tagger = pickle.load(fa)
except FileNotFoundError as a:
    # training data
    print("dumping tnt")
    tnt_tagger = tnt_tagger = tnt.TnT()
    tnt_tagger.train(train)

    with open('test_pickles/tnt.pickle', 'wb') as fb:
        pickle.dump(tnt_tagger, fb)

#print(tnt_tagger.evaluate(test))
print(tnt_tagger.tag(tokenized_words))