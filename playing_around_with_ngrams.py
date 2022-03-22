import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize

with open('209-0.txt', encoding='utf-8') as f:
    text = f.read()

james_tokens = list(word_tokenize(text))
james_words = [word for word in james_tokens if word.isalpha()]

james_text = nltk.Text(james_words)
#james_text.collocations(25)

jamesFirstSixWords = " ".join(james_words[0:6])
#print("First Six Words: ", jamesFirstSixWords)

jamesBigrams = list(nltk.ngrams(james_words, 2))
#print(jamesBigrams[:5])

james4grams = list(nltk.ngrams(james_words, 4))
james4gramsFreqs = nltk.FreqDist(james4grams)
for words, count in james4gramsFreqs.most_common(15):
    print(count, " ".join(list(words)))

james4gramsTokens = [' '.join(gram) for gram in james4grams]
#nltk.Text(james4gramsTokens).dispersion_plot([('I don t know')])
#plt.show()

ngramsFreqs = []
for length in range(2, len(james_words)):
    ngrams = list(nltk.ngrams(james_words, length))
    freqs = nltk.FreqDist(ngrams)
    freqs = [(ngram, count) for ngram, count in freqs.items() if count > 1]
    if len(freqs) > 0:
        ngramsFreqs = freqs
    else:
        break

for ngram, count in ngramsFreqs:
    print("ngram of ", len(ngram), " words occuring ", count, " times ", " ".join(list(ngram)))

james4gramsSegments = np.array_split(james4gramsTokens, 10)
print([len(segment) for segment in james4gramsSegments])

at_the_end_ofCounts = [list(segment).count(('at the end of')) for segment in james4gramsSegments]
print(at_the_end_ofCounts)

line = plt.plot(at_the_end_ofCounts, label='at the end of')
plt.ylim(0)
plt.legend(handles=line)
#plt.show()
#nltk.Text(james4gramsTokens).dispersion_plot([('at the end of')])

xaxis = range(0, len(at_the_end_ofCounts))
bar = plt.bar(xaxis, at_the_end_ofCounts, label='at the end of')
plt.legend(handles=[bar])
#plt.show()

searches = ['at the end of', 'the rest of the']
lines = []
for search in searches:
    line, = plt.plot([list(segment).count(search) for segment in james4gramsSegments], label=search)
    lines.append(line)
plt.legend(handles=lines)
#plt.show()

the_rest_of_theCounts = [list(segment).count('the rest of the') for segment in james4gramsSegments]

print(np.corrcoef(at_the_end_ofCounts, the_rest_of_theCounts)[0,1])

james4gramsMostFrequent = [" ".join(words) for words, count in james4gramsFreqs.most_common(10)] # get a list of top 
print(james4gramsMostFrequent)

james4gramsSegmentsCounts = {} # build a dictionary of counts for each search item
for search in james4gramsMostFrequent:
    james4gramsSegmentsCounts[search] = [list(segment).count(search) for segment in james4gramsSegments]

at_the_end_ofCorrelations = {} # build a dictionary of correlation values for "at the end of""
for ngram, counts in james4gramsSegmentsCounts.items():
    at_the_end_ofCorrelations[ngram] = np.corrcoef(james4gramsSegmentsCounts["at the end of"], counts)[0,1]

at_the_end_ofCorrelationFreqs = nltk.FreqDist(at_the_end_ofCorrelations)
plt.clf()
print(at_the_end_ofCorrelationFreqs.most_common())
at_the_end_ofCorrelationFreqs.plot()
