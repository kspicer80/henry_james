from pathlib import Path
from collections import Counter
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = Path('texts')
files = Path(path).glob('*.txt')
files = sorted(files)
#print(files)

filenames_list = []

for file in files:
    filename = file.stem
    filenames_list.append(filename)

newer_dict = {'1875_roderick_hudson': Counter({'portentous': 6, 'prodigiously': 4, 'prodigious': 2, 'portentously': 2}), '1877_the_american': Counter({'portentously': 4, 'portentous': 1, 'prodigiously': 1}), '1878_daisy_miller': Counter(), '1878_the_europeans': Counter({'portentous': 2, 'prodigious': 1}), '1879_a_bundle_of_letters': Counter(), '1879_confidence': Counter({'portentously': 1}), '1880_washington_square': Counter(), '1881_portrait_of_a_lady_vol_1': Counter({'prodigiously': 1}), '1881_portrait_of_a_lady_vol_2': Counter({'portentous': 2, 'prodigious': 1}), '1886_the_bostonians_vol_1': Counter({'portentously': 1, 'prodigious': 1}), '1886_the_bostonians_vol_2': Counter({'portentous': 1, 'prodigious': 1}), '1888_the_aspern_papers': Counter(), '1888_the_lesson_of_the_master': Counter(), '1891_the_pupil': Counter({'prodigious': 1}), '1892_the_real_thing_and_other_tales': Counter({'prodigiously': 2, 'prodigious': 1}), '1895_the_altar_of_the_dead': Counter({'portentous': 1}), '1896_the_figure_in_the_carpet': Counter({'prodigiously': 1}), '1897_what_maisie_knew': Counter({'prodigious': 4, 'portentous': 4, 'portentously': 1, 'prodigiously': 1}), '1898_in_the_cage': Counter({'prodigious': 4, 'portentous': 2, 'prodigiously': 1, 'portentously': 1}), '1898_turn_of_the_screw': Counter({'prodigious': 9, 'portentous': 3, 'portentously': 1}), '1902_some_short_stories': Counter({'prodigious': 1, 'portentously': 1}), '1902_wings_of_the_dove_vol_1': Counter({'prodigious': 4, 'portentous': 2, 'portentously': 1}), '1902_wings_of_the_dove_vol_2': Counter({'prodigious': 9, 'portentous': 2, 'prodigiously': 1}), '1903_the_ambassadors': Counter({'prodigious': 8, 'portentous': 4, 'prodigiously': 2, 'portentously': 2}), '1903_the_beast_in_the_jungle': Counter({'prodigious': 1, 'portentous': 1, 'prodigiously': 1}), '1904_the_golden_bowl': Counter({'prodigious': 7, 'portentous': 6, 'prodigiously': 1}), '1908_the_jolly_corner': Counter({'prodigious': 2, 'portentously': 1, 'portentous': 1}), '1909_italian_hours': Counter({'prodigious': 19, 'portentous': 4, 'portentously': 1, 'prodigiously': 1}), '1916_notes_on_novelists': Counter({'prodigious': 11, 'prodigiously': 4, 'portentous': 4, 'portentously': 1})}

converted_newer_dict = dict(newer_dict)
#print(json.dumps(converted_newer_dict, indent=4))
print(len(converted_newer_dict))
#with open('makenzies_target_words.json', 'w') as outfile:
    #json.dump(converted_newer_dict, outfile)

#print(len(x_label_dict))
#print(json.dumps(x_label_dict, indent=4, sort_keys=True))

x = np.arange(0, len(filenames_list), 1)
df = pd.DataFrame(newer_dict).T
df.plot(y=['prodigious', 'prodigiously', 'portentous', 'portentously'], use_index=True, kind='bar')

#df.plot.bar()
plt.xticks(x, filenames_list, rotation='vertical')
plt.title("Counts of MaKenzie's Target Words across 29 Different Henry James Texts")
plt.xlabel('Text Titles')
plt.ylabel('# of Target Words Counted')
plt.show()

turn_counts = {'209': {'prodigious': 9, 'portentous': 3, 'portentously': 1}}
turn_label_dict = {'209': "Turn of the Screw"}

x = np.arange(len(turn_label_dict))
df_turn = pd.DataFrame(turn_counts).T
df_turn.plot(y=['prodigious', 'portentous', 'portentously'], use_index=True, kind='bar')
plt.show()
