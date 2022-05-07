from collections import Counter
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

cleaned_up_counts = {
    '898': {'prodigious': 0, 'portentous': 0, 'portentously': 0, 'prodigiously': 0},
    '7118': {'prodigious': 4, 'portentous': 4, 'portentously': 1, 'prodigiously': 1},
    '645': {'prodigiously': 1}, '642': {'portentous': 1},
    '6354': {'prodigious': 19, 'portentous': 4, 'portentously': 1, 'prodigiously': 1},
    '432': {'prodigious': 8, 'portentous': 4, 'prodigiously': 2, 'portentously': 2},
    '4264': {'prodigious': 7, 'portentous': 6, 'prodigiously': 1},
    '30059': {'prodigious': 9, 'portentous': 2, 'prodigiously': 1},
    '29452': {'prodigious': 4, 'portentous': 2, 'portentously': 1},
    '2870': {'prodigious': 0, 'portentous': 0, 'portentously': 0, 'prodigiously': 0},
    '2834': {'portentous': 2, 'prodigious': 1},
    '2833': {'prodigiously': 1}, '2715': {'prodigiously': 2, 'prodigious': 1},
    '2425': {'prodigious': 0, 'portentous': 0, 'portentously': 0, 'prodigiously': 0},
    '2327': {'prodigious': 1, 'portentously': 1},
    '211': {'prodigious': 0, 'portentous': 0, 'portentously': 0, 'prodigiously': 0},
    '208': {'prodigious': 0, 'portentous': 0, 'portentously': 0, 'prodigiously': 0},
    '19717': {'portentously': 1, 'prodigious': 1},
    '179': {'portentous': 2, 'prodigious': 1},
    '178': {'portentously': 1},
    '177': {'portentously': 4, 'portentous': 1, 'prodigiously': 1},
    '176': {'portentous': 6, 'prodigiously': 4, 'prodigious': 2, 'portentously': 2},
    '1190': {'prodigious': 2, 'portentously': 1, 'portentous': 1},
    '1144': {'prodigious': 4, 'portentous': 2, 'prodigiously': 1, 'portentously': 1},
    '1093': {'prodigious': 1, 'portentous': 1, 'prodigiously': 1},
    '1032': {'prodigious': 1},
    '209': {'prodigious': 9, 'portentous': 3, 'portentously': 1}}

newer_dict = {'1916_notes_on_novelists': Counter({'prodigious': 11, 'prodigiously': 4, 'portentous': 4, 'portentously': 1}), '1909_italian_hours': Counter({'prodigious': 19, 'portentous': 4, 'portentously': 1, 'prodigiously': 1}), '1908_the_jolly_corner': Counter({'prodigious': 2, 'portentously': 1, 'portentous': 1}), '1904_the_golden_bowl': Counter({'prodigious': 7, 'portentous': 6, 'prodigiously': 1}), '1903_the_beast_in_the_jungle': Counter({'prodigious': 1, 'portentous': 1, 'prodigiously': 1}), '1903_the_ambassadors': Counter({'prodigious': 8, 'portentous': 4, 'prodigiously': 2, 'portentously': 2}), '1902_wings_of_the_dove_vol_2': Counter({'prodigious': 9, 'portentous': 2, 'prodigiously': 1}), '1902_wings_of_the_dove_vol_1': Counter({'prodigious': 4, 'portentous': 2, 'portentously': 1}), '1902_some_short_stories': Counter({'prodigious': 1, 'portentously': 1}), '1898_turn_of_the_screw': Counter({'prodigious': 9, 'portentous': 3, 'portentously': 1}), '1898_in_the_cage': Counter({'prodigious': 4, 'portentous': 2, 'prodigiously': 1, 'portentously': 1}), '1897_what_maisie_knew': Counter({'prodigious': 4, 'portentous': 4, 'portentously': 1, 'prodigiously': 1}), '1896_the_figure_in_the_carpet': Counter({'prodigiously': 1}), '1895_the_altar_of_the_dead': Counter({'portentous': 1}), '1892_the_real_thing_and_other_tales': Counter({'prodigiously': 2, 'prodigious': 1}), '1891_the_pupil': Counter({'prodigious': 1}), '1888_the_lesson_of_the_master': Counter(), '1888_the_aspern_papers': Counter(), '1886_the_bostonians_vol_2': Counter({'portentous': 1, 'prodigious': 1}), '1886_the_bostonians_vol_1': Counter({'portentously': 1, 'prodigious': 1}), '1881_portrait_of_a_lady_vol_2': Counter({'portentous': 2, 'prodigious': 1}), '1881_portrait_of_a_lady_vol_1': Counter({'prodigiously': 1}), '1880_washington_square': Counter(), '1879_confidence': Counter({'portentously': 1}), '1879_a_bundle_of_letters': Counter(), '1878_the_europeans': Counter({'portentous': 2, 'prodigious': 1}), '1878_daisy_miller': Counter(), '1877_the_american': Counter({'portentously': 4, 'portentous': 1, 'prodigiously': 1}), '1875_roderick_hudson': Counter({'portentous': 6, 'prodigiously': 4, 'prodigious': 2, 'portentously': 2})}

converted_newer_dict = dict(newer_dict)
print(converted_newer_dict)

x_label_dict = {
    '208': 'Daisy Miller: A Study',
    '2833': 'The Portrait of a Lady Volume 1',
    '1093': 'The Beast in the Jungle',
    '1190': 'The Jolly Corner',
    '432': 'The Ambassadors',
    '178': 'Confidence',
    '2870': 'Washington Square',
    '2834': 'The Portrait of a Lady Volume 2',
    '2715': 'The Real Thing and Other Tales',
    '211': 'The Aspern Papers',
    '4264': 'The Golden Bowl Complete',
    '177': 'The American',
    '7118': 'What Maisie Knew',
    '645': 'The Figure in the Carpet',
    '29452': 'The Wings of the Dove, Volume 1 of 2',
    '642': 'The Altar of the Dead',
    '19717': 'The Bostonians, Vol. I (of II)',
    '1032': 'The Pupil',
    '6354': 'Italian Hours',
    '1144': 'In the Cage',
    '179': 'The Europeans',
    '898': 'The Lesson of the Master',
    '30059': 'The Wings of the Dove, Volume II',
    '176': 'Roderick Hudson',
    '2425': 'A Bundle of Letters',
    '2327': 'Some Short Stories',
    '209': 'The Turn of the Screw'}

#print(len(x_label_dict))
#print(json.dumps(x_label_dict, indent=4, sort_keys=True))

x = np.arange(0, len(x_label_dict), 1)
df = pd.DataFrame(cleaned_up_counts).T
df.plot(y=['prodigious', 'portentous', 'portentously', 'prodigiously'], use_index=True, kind='bar')

#df.plot.bar()
plt.xticks(x, x_label_dict.values(), rotation='vertical')
plt.title("Counts of MaKenzie's Target Words across 27 Different Henry James Texts")
plt.xlabel('Text Titles')
plt.ylabel('# of Target Words Counted')
plt.show()

turn_counts = {'209': {'prodigious': 9, 'portentous': 3, 'portentously': 1}}
turn_label_dict = {'209': "Turn of the Screw"}

x = np.arange(len(turn_label_dict))
df_turn = pd.DataFrame(turn_counts).T
df_turn.plot(y=['prodigious', 'portentous', 'portentously'], use_index=True, kind='bar')
plt.show()
