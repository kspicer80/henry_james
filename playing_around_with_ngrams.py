import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk import bigrams
import itertools
import seaborn as sns

# simple home-made ngram function:
def n_grams(tokens, n):
    return[tokens[i:i+n] for i in range(len(tokens)-n+1)]

with open('209-0.txt', encoding='utf-8') as f:
    text = f.read()

james_tokens = list(word_tokenize(text))
james_words = [word for word in james_tokens if word.isalpha()]
print(james_words)

james_text = nltk.Text(james_words)
#james_text.collocations(25)

jamesFirstSixWords = " ".join(james_words[0:6])
#print("First Six Words: ", jamesFirstSixWords)

jamesBigrams = list(nltk.ngrams(james_words, 2))
#print(jamesBigrams[:5])

james4grams = list(nltk.ngrams(james_words, 4))
james4gramsFreqs = nltk.FreqDist(james4grams)
#for words, count in james4gramsFreqs.most_common(150):
    #print(count, " ".join(list(words)))

james4gramsTokens = [' '.join(gram) for gram in james4grams]
#nltk.Text(james4gramsTokens).dispersion_plot([('He was the same')])
#plt.show()

james5grams = list(nltk.ngrams(james_words, 5))
james5gramsFreqs = nltk.FreqDist(james5grams)
for words, count in james5gramsFreqs.most_common(150):
    print(count, " ".join(list(words)))

ngramsFreqs = []
for length in range(2, len(james_words)):
    ngrams = list(nltk.ngrams(james_words, length))
    freqs = nltk.FreqDist(ngrams)
    freqs = [(ngram, count) for ngram, count in freqs.items() if count > 1]
    if len(freqs) > 0:
        ngramsFreqs = freqs
    else:
        break

#for ngram, count in ngramsFreqs:
    #print("ngram of ", len(ngram), " words occuring ", count, " times ", " ".join(list(ngram)))

james4gramsSegments = np.array_split(james4gramsTokens, 50)
#print([len(segment) for segment in james4gramsSegments])

at_the_end_ofCounts = [list(segment).count(('at the end of')) for segment in james4gramsSegments]
#print(at_the_end_ofCounts)

line = plt.plot(at_the_end_ofCounts, label='at the end of')
plt.ylim(0)
plt.legend(handles=line)
#plt.show()
#nltk.Text(james4gramsTokens).dispersion_plot([('at the end of')])

xaxis = range(0, len(at_the_end_ofCounts))
bar = plt.bar(xaxis, at_the_end_ofCounts, label='at the end of')
plt.legend(handles=[bar])
#plt.show()

searches = ['he was the same']
lines = []
for search in searches:
    line, = plt.plot([list(segment).count(search) for segment in james4gramsSegments], label=search)
    lines.append(line)
plt.legend(handles=lines)
#plt.show()

the_rest_of_theCounts = [list(segment).count('the rest of the') for segment in james4gramsSegments]

#print(np.corrcoef(at_the_end_ofCounts, the_rest_of_theCounts)[0,1])

james4gramsMostFrequent = [" ".join(words) for words, count in james4gramsFreqs.most_common(10)]
#print(james4gramsMostFrequent)

james4gramsSegmentsCounts = {}
for search in james4gramsMostFrequent:
    james4gramsSegmentsCounts[search] = [list(segment).count(search) for segment in james4gramsSegments]

at_the_end_ofCorrelations = {}
for ngram, counts in james4gramsSegmentsCounts.items():
    at_the_end_ofCorrelations[ngram] = np.corrcoef(james4gramsSegmentsCounts["at the end of"], counts)[0,1]

at_the_end_ofCorrelationFreqs = nltk.FreqDist(at_the_end_ofCorrelations)
plt.clf()
#print(at_the_end_ofCorrelationFreqs.most_common())
#at_the_end_ofCorrelationFreqs.plot()

# Co-occurnce Matrix Creation
def co_occurence_matrix(corpus):
    vocab = set(corpus)
    vocab = list(vocab)
    vocab_to_index = {word:i for i, word in enumerate(vocab)}
    bi_grams = list(bigrams(corpus))
    bigram_freq = nltk.FreqDist(bi_grams).most_common(len(bi_grams))
    co_occurence_matrix = np.zeros((len(vocab), len(vocab)))
    for bigram in bigram_freq:
        current = bigram[0][1]
        previous = bigram[0][0]
        count = bigram[1]
        pos_current = vocab_to_index[current]
        pos_previous = vocab_to_index[previous]
        co_occurence_matrix[pos_current][pos_previous] = count
    co_occurence_matrix = np.matrix(co_occurence_matrix)
    return co_occurence_matrix, vocab_to_index

#merged = list(itertools.chain.from_iterable(james_tokens))
#print(merged)
matrix, vocab_to_index = co_occurence_matrix(james_tokens)
CoMatrixFinal = pd.DataFrame(matrix, index=vocab_to_index, columns=vocab_to_index)
print(CoMatrixFinal.head())
sns.heatmap(CoMatrixFinal)
plt.show()
