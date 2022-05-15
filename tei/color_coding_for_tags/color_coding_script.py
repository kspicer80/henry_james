from pathlib import Path
import json
import random

#data_file = Path('tei\color_coding_for_tags\color_code_data.json')
#print
#with open(data_file) as read_file:
    #data = json.load(read_file)
    ##data = dict(ChainMap(*data))
#
#print(data)
#print(len(data))

all_tags = ['touch-figurative',
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
'fire-figurative',
'reading',
'book reading',
'vision',
'sound',
'colors-white',
'reading romance books',
'epistle',
'letter reading-figurative',
'touch',
'vision-figurative touch-figurative',
'sound-figurative sound-physical vision-physical',
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
'sound-figurative',
'vision-literal',
'sound-physical sound-figurative',
'sight-figurative',
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
'vision-physical touch-physical',
'sound-physical repetition']

sorted = sorted(all_tags)
print(*sorted, sep='\n')
#print(len(all_tags))

#color_names = []
#for key in data.keys():
    #print(key)
    #color_names.append(key)
#
#print(color_names)
#
#color_choices = []
#for i in range(len(all_tags)):
    #color_choices.append(random.choice(color_names))
#
#
#zipped_list = zip(all_tags, color_choices)
#zipped_dict = dict(zipped_list)
#
## So much better—obviously—then typing them all out individually ...
#for key, value in zipped_dict.items():
    #print(f"<xsl:template match=\"//TEI//text//body//div//seg[@ana=\'{key}\']\"><font color=\'{value}\'><xsl:apply-templates/></font></xsl:template>")
