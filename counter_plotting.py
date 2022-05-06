from collections import Counter
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

cleaned_up_counts = {'898': 0, '7118': {'prodigious': 4, 'portentous': 4, 'portentously': 1, 'prodigiously': 1}, '645': {'prodigiously': 1}, '642': {'portentous': 1}, '6354': {'prodigious': 19, 'portentous': 4, 'portentously': 1, 'prodigiously': 1}, '432': {'prodigious': 8, 'portentous': 4, 'prodigiously': 2, 'portentously': 2}, '4264': {'prodigious': 7, 'portentous': 6, 'prodigiously': 1}, '30059': {'prodigious': 9, 'portentous': 2, 'prodigiously': 1}, '29452': {'prodigious': 4, 'portentous': 2, 'portentously': 1}, '2870': 0, '2834': {'portentous': 2, 'prodigious': 1}, '2833': {'prodigiously': 1}, '2715': {'prodigiously': 2, 'prodigious': 1}, '2425': 0, '2327': {'prodigious': 1, 'portentously': 1}, '211': 0, '209': {'prodigious': 9, 'portentous': 3, 'portentously': 1}, '208': 0, '19717': {'portentously': 1, 'prodigious': 1}, '179': {'portentous': 2, 'prodigious': 1}, '178': {'portentously': 1}, '177': {'portentously': 4, 'portentous': 1, 'prodigiously': 1}, '176': {'portentous': 6, 'prodigiously': 4, 'prodigious': 2, 'portentously': 2}, '1190': {'prodigious': 2, 'portentously': 1, 'portentous': 1}, '1144': {'prodigious': 4, 'portentous': 2, 'prodigiously': 1, 'portentously': 1}, '1093': {'prodigious': 1, 'portentous': 1, 'prodigiously': 1}, '1032': {'prodigious': 1}}

x_label_dict = {209: 'The Turn of the Screw', 208: 'Daisy Miller: A Study', 2833: 'The Portrait of a Lady Volume 1', 1093: 'The Beast in the Jungle', 1190: 'The Jolly Corner', 432: 'The Ambassadors', 178: 'Confidence', 2870: 'Washington Square', 2834: 'The Portrait of a Lady Volume 2', 2715: 'The Real Thing and Other Tales', 211: 'The Aspern Papers', 4264: 'The Golden Bowl Complete', 177: 'The American', 7118: 'What Maisie Knew', 645: 'The Figure in the Carpet', 29452: 'The Wings of the Dove, Volume 1 of 2', 642: 'The Altar of the Dead', 19717: 'The Bostonians, Vol. I (of II)', 1032: 'The Pupil', 6354: 'Italian Hours', 1144: 'In the Cage', 179: 'The Europeans', 898: 'The Lesson of the Master', 30059: 'The Wings of the Dove, Volume II', 176: 'Roderick Hudson', 2425: 'A Bundle of Letters', 2327: 'Some Short Stories'}

#print(len(x_label_dict))
#print(json.dumps(x_label_dict, indent=4, sort_keys=True))

x = np.arange(0, len(x_label_dict), 1)
df = pd.DataFrame(cleaned_up_counts).T
print(df)
df.plot(y=['prodigious', 'portentous', 'portentously', 'prodigiously'], use_index=True, kind='bar')

#df.plot.bar()
plt.xticks(x, x_label_dict.values(), rotation='vertical')
plt.title("Counts of MaKenzie's Target Words across 27 Different Henry James Texts")
plt.xlabel('Text Titles')
plt.ylabel('# of Target Words Counted')
plt.show()
