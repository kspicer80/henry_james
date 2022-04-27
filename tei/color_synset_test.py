from nltk.corpus import wordnet
syn = wordnet.synsets('color')[0]

print(syn.name())
print(syn.definition())
print(syn.examples())
print(syn.hypernyms())
print(syn.hypernyms()[0].hyponyms())
print(syn.root_hypernyms())
