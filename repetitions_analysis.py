from more_itertools import pairwise
import pandas as pd
pd.options.display.width = 0

def find_neighbors(list, close_number=int()):
    results = []
    chunk = []
    list.sort()
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

df = pd.read_csv('repetition_counts.csv', encoding='utf-8')
print(df.head())
df = df.rename(columns = {0: 'token'})
print(df.columns)
