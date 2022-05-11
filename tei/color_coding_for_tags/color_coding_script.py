import json
import random

with open(r'tei\color_coding_for_tags\color_code_data.json') as read_file:
    data = json.load(read_file)
    #data = dict(ChainMap(*data))

print(data)
print(len(data))

all_tags = ['touch-figurative',
'fire',
'repetition',
'touch-figurative touch-literal',
'vision-physical',
'touch-physical',
'taste-figurative',
'vision-figurative',
'delay',
'sound-physical',
'writing',
'weather-figurative',
'delay sound-physical',
'sound-figurative sound-literal',
'writing letters',
'weather',
'interruptions',
'letters',
'fire touch-physical',
'colors-brown',
'fire-figurative',
'reading',
'book reading',
'colors-red',
'colors-golden',
'vision',
'sound',
'colors-white',
'colors-gold',
'colors-blue',
'reading romance books',
'epistle',
'letter reading-figurative',
'touch',
'vision-figurative touch-figurative',
'sound-figurative sound-physical vision-physical',
'colors-rose',
'fire delay',
'master-nonknowledge',
'delay-hesitation',
'reading-figurative',
'vision-physical vision-figurative',
'reading books',
'imaginative play',
'colors-black',
'vision-figurative vision-physical',
'colors',
'smell-figurative',
'sound-physical vision-physical',
'colors-pink',
'sound-figurative',
'vision-literal',
'sound-physical sound-figurative',
'colors-gray',
'sight-figurative',
'colors-crimson',
'letters writing',
'vision-physical touch-figurative',
'smell-physical',
'sound-figurative sound-physical',
'reading writing letters',
'fire-figurative delay',
'reading letters',
'vison-physical',
'physical-figurative',
'sexuality',
'touch-physical sound-physical',
'sexuality-figurative',
'fire-figurative vision-figurative',
'sealed senses',
'colors-green',
'vision-physical touch-physical',
'sound-physical repetition']

print(len(all_tags))

color_names = []
for key in data.values():
    print(key)
    color_names.append(key)

print(color_names)
    
zipped_list = zip(all_tags, random.choice(color_names))
print(list(zipped_list))
    
