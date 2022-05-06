from pathlib import Path
import glob
import spacy
nlp = spacy.load('en_core_web_lg', disable=['ner', 'parser'])
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

directory = Path('texts')
print(directory.is_dir())

target_words = ['prodigious', 'prodigiously', 'prodigiousness', 'portentous', 'portentously']

dict_counts = {}

files = Path(directory).glob('*.txt')
files = sorted(files, reverse=True)
#print(files)
for file in files:
    filename = file.stem
    print(f"Processing {filename} now ...")
    with open(file) as f:
        file = f.read()
        nlp.max_length = len(file) + 100
        nlp_contents = nlp(file)
        words = [token.text for token in nlp_contents if not token.is_stop and not token.is_punct]
        in_target = [token for token in words if token in target_words]
        dict_counts[filename] = Counter(in_target)

print(dict_counts)
    
#data_folder = r'C:\Users\KSpicer\Documents\GitHub\henry_james\texts'

#all_globbed_files = #glob.glob(r'C:\Users\KSpicer\Documents\GitHub\henry_james\texts\*.txt')
#print(all_globbed_files)

#for file in all_globbed_files:
    #with open(file) as f:
        #file = f.read()
        #filename = file.split('.')[0]
        #nlp_contents = nlp(file)
        #words = [token.text for token in nlp_contents if not token.is_stop and #not token.is_punct]
        #in_target = [token for token in words if token in target_words]
        #target_word_freq = Counter(in_target)
        #print(f"In {filename} the counts are as follows: {target_word_freq}")
        
        
        
