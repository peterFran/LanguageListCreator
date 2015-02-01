from nltk.corpus import cess_esp as cess
from nltk.tag.hmm import HiddenMarkovModelTagger as hmm

# Read the corpus into a list, 
# each entry in the list is one sentence.
cess_sents = cess.tagged_sents()
cess_sents_simple = cess.tagged_sents(simplify_tags=True)
print(cess_sents_simple[:10])


sentence = "Hola , soy Pedro , ¿ como te llamas ?."


# Split corpus into training and testing set.
# train = int(len(cess_sents)*90/100) # 90%

# # Train the unigram tagger
# hmm_tagger = hmm(cess_sents[:train])

# # Evaluates on testing data remaining 10%
# print(hmm_tagger.evaluate(cess_sents[train+1:])*100)
# print("\n\n\nspace here \n\n\n")
# # Using the tagger.
# print(hmm_tagger.tag(nltk.word_tokenize(sentence)))