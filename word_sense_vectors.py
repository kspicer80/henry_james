import pandas as pd
pd.set_option('display.max_rows', None)
import spacy
nlp = spacy.load('en_core_web_lg')

with open('209-0.txt', encoding='utf-8') as f:
    data = f.read()

senseDocs = [nlp(w) for w in ['sight']]

def whichSense(word):
    doc = nlp(word)
    return {sense: doc.similarity(sense) for sense in senseDocs}

nlp_of_file = nlp(data)
#dictionary = {whichSense(w.text) for w in testWords}

df = pd.DataFrame([whichSense(w.text) for w in nlp_of_file], index=nlp_of_file)
df.columns = ['sight']
df = df.sort_values(by=['sight'], ascending=False)
print(df.dtypes)
print(df.head(100))

#pd.DataFrame(data=[*dict.values()], columns=['firstcolumn','secondcolumn', 'thirdcolumn'])

#print(df.head())
#print(df.columns)
#print(list(df))
