import spacy
import numpy
import sklearn.neighbors as nbs
import pickle
import random
import sys

#load NLP tool spaCy
print("Loading spaCy...")
nlp=spacy.load("en_core_web_lg")
print("spaCy loaded.")

print({nlp.vocab[word].prob for word in nlp.vocab.strings})

#get plaintext words as list from spacy vocab. ensure they have wordvector, are lowercase, and aren't too rare
#{prob:# words} ~ {-15:32k, -16:50k, -17:77k, -18:147k, -19:183k, -20:302k}
#as of spaCy v3.0, word probabilities require spacy-lookup-data
print("Total number of words=",len(nlp.vocab.strings))
print("Getting words...")
words = [word for word in nlp.vocab.strings if nlp.vocab.has_vector(word) and word.islower()]
print("Retrieved ",len(words),"words with vectors.")

#get wordvectors for all words as numpy array
print("Total number of wordvectors=",len(nlp.vocab.vectors))
print("Getting wordvectors...")
wordvecs = numpy.array([nlp.vocab.get_vector(word) for word in words])
print("Retrieved=",len(wordvecs),"wordvectors.")

#ensure the list of words corresponds to the list of wordvectors
assert len(words) == len(wordvecs)
spot_check = random.choice(range(0,len(words)))
assert numpy.array_equal(nlp(words[spot_check]).vector,wordvecs[spot_check])
print("Spot check passed.")

#pickle the entire vocab
with open('words.pkl', 'wb') as f:
		pickle.dump(words,f,protocol=pickle.HIGHEST_PROTOCOL)
print("Dumped vocab words to pickle file vocab.pkl")

#place all wordvectors in balltree, and pickle entire tree
tree = nbs.BallTree(wordvecs)
with open('balltree.pkl', 'wb') as f:
		pickle.dump(tree,f,protocol=pickle.HIGHEST_PROTOCOL)
print("Dumped wordvector BallTree to pickle file balltree.pkl")

#place all wordvectors in balltree, and pickle entire tree
dict = dict(zip(words,wordvecs))
with open('dict.pkl', 'wb') as f:
		pickle.dump(dict,f,protocol=pickle.HIGHEST_PROTOCOL)
print("Dumped word2vec dictionary in dict.pkl")
