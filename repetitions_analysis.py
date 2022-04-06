from more_itertools import pairwise
import nltk
from nltk.tokenize import word_tokenize
from nltk.draw.dispersion import dispersion_plot
from nltk.text import Text
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
pd.options.display.width = 0
pd.set_option('display.max_rows', None)

def find_neighbors(list, close_number=int()):
    results = []
    chunk = []
    for n1, n2 in pairwise(list):
        if n2 - n1 <= close_number:
            chunk.append(n1)
        elif chunk:
            chunk.append(n1)
            results.append(chunk)
            chunk = []
    return(results)

def clean(seq_string):
    return list(map(int, seq_string.split(',')))

def to_integers(column_value):
    if not isinstance(column_value, int):
        return [int(v) for v in column_value.split(',')]
    else:
        return column_value

def flatten_list(t):
    return [item for sublist in t for item in sublist]

#test_string = '[0, 5, 6, 7, 10, 15]'
#cleaned_string = clean(test_string)
#print(cleaned_string)

#df[cols_to_check] = df[cols_to_check].replace({';':''}, regex=True)

df = pd.read_csv('repetition_counts_no_stopwords.csv', encoding='utf-8')
#print(df.head())
df.rename(columns = {'Unnamed: 0': 'token'}, inplace=True)
#print(df.head())
#print(df.dtypes)
df['indices'] = df['indices'].str.replace('\[', '')
df['indices'] = df['indices'].str.replace('\]', '')
#print(df.head())
df.loc[:, 'indices'] = df.loc[:, 'indices'].apply(to_integers)
#print(df.head())
#print(df.dtypes)

#df['colname'] = df['colname'].str.replace(',', '').astype(float)

#df['indices'] = df['indices'].apply(lambda x: clean(x))
#df['indices'] = df['indices'].astype(int)
#df['indices'] = pd.to_numeric(df['indices'])
df['neighbors_within_5'] = df['indices'].apply(lambda x: find_neighbors(x, 5))
df['neighbors_within_5'] = df['neighbors_within_5'].apply(lambda x: flatten_list(x))
#print(df.neighbors.value_counts().sort_index())

df['neighbors_within_10'] = df['indices'].apply(lambda x: find_neighbors(x, 10))
df['neighbors_within_10'] = df['neighbors_within_10'].apply(lambda x: flatten_list(x))

df['neighbors_within_50'] = df['indices'].apply(lambda x: find_neighbors(x, 50))
df['neighbors_within_50'] = df['neighbors_within_50'].apply(lambda x: flatten_list(x))

df['neighbors_within_100'] = df['indices'].apply(lambda x: find_neighbors(x, 100))
df['neighbors_within_100'] = df['neighbors_within_100'].apply(lambda x: flatten_list(x))

#df = df.sort_values(by='number_of_repetitions', ascending=False)
df['number_within_5'] = df.neighbors_within_5.map(len)
df['number_within_10'] = df.neighbors_within_10.map(len)
df['number_within_50'] = df.neighbors_within_50.map(len)
df['number_within_100'] = df.neighbors_within_100.map(len)

df = df.sort_values(by = ['number_within_5', 'number_within_10', 'number_within_50', 'number_within_100'], ascending = [False, False, False, False])

df_of_lengths = df[['token', 'number_of_repetitions', 'number_within_5', 'number_within_10', 'number_within_50', 'number_within_100']]
df["token"] = df['token'].str.replace('[^\w\s]','')

subset_for_strip_plot = df_of_lengths.iloc[0:100, 0]
subset_for_strip_plot_list = subset_for_strip_plot.tolist()
#print(len(subset_for_strip_plot_list))

#with open('209-0.txt', encoding='utf-8') as f:
    #data = f.read()
#
#tokens = word_tokenize(data)
#tots_text = nltk.Text(tokens)
#targets = subset_for_strip_plot_list
#dispersion_plot(tots_text, targets, ignore_case=True, title='Test Dispersion Plot')

#print(subset_for_strip_plot.head(100))
#print(subset_for_strip_plot.head(50))

#plt.figure(figsize=(22, 6))
#subset_plot = sns.stripplot(x = subset_for_strip_plot.index, y = subset_for_strip_plot.values, data=subset_for_strip_plot, palette="Set2", #size=10, marker='D', edgecolor='gray', alpha=.50)
#plt.show()
