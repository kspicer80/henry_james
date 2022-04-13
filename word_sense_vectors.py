import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_rows', None)
import spacy
nlp = spacy.load('en_core_web_lg')

with open('209-0.txt', encoding='utf-8') as f:
    data = f.read()

senseDocs = [nlp(w) for w in ['sight', 'sound', 'touch', 'smell']]

def whichSense(word):
    doc = nlp(word)
    return {sense: doc.similarity(sense) for sense in senseDocs}

nlp_of_file = nlp(data)
#dictionary = {whichSense(w.text) for w in testWords}

df = pd.DataFrame([whichSense(w.text) for w in nlp_of_file], index=nlp_of_file)
df.columns = ['sight', 'sound', 'touch', 'smell']
df = df.sort_values(by=['sight', 'sound'], ascending=[False, False])
df.plot(kind='bar')
plt.show()
#print(df.head(100))
#df.to_csv('sense_test.csv')

#pd.DataFrame(data=[*dict.values()], columns=['firstcolumn','secondcolumn', 'thirdcolumn'])

#print(df.head())
#print(df.columns)
#print(list(df))
