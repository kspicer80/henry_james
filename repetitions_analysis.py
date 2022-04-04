from more_itertools import pairwise
import pandas as pd
pd.options.display.width = 0

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

df = pd.read_csv('repetition_counts.csv', encoding='utf-8')
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
df['neighbors'] = df['indices'].apply(lambda x: find_neighbors(x, 10))
df['neighbors'] = df['neighbors'].apply(lambda x: flatten_list(x))
#print(df.neighbors.value_counts().sort_index())
df = df.sort_values(by='number_of_repetitions', ascending=False)
df['length'] = df.neighbors.map(len)
#print(df.shape)
print(df.head(100))
