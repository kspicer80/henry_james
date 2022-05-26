from pathlib import Path
import json
from lxml import etree
import networkx as nx
import matplotlib.pyplot as plt
import collections
nsmap = {'tei': 'http://www.tei-c.org/ns/1.0'}

def childTexts(node):
    texts={}
    for child in list(node):
        texts[child.tag] = child.text
    return texts  
        
tots_xml = r'C:\Users\KSpicer\Documents\GitHub\henry_james\tei\hj_tots_tei.xml'

tree = etree.parse(tots_xml)
#print(tree.getroot().find('.//{http://www.tei-c.org/ns/1.0}title').text)
#print(tree.getroot().find('title'))

all_seg_tags = tree.findall(".//tei:seg[@ana]", namespaces=nsmap)
#print(all_seg_tags, len(all_seg_tags))
all_tags = tree.findall(".//tei:*", namespaces=nsmap)
#print(all_tags, len(all_tags))

import xml.etree.ElementTree as ET
# load and parse the file
xmlTree = ET.parse(tots_xml)
elemList = []
for elem in xmlTree.iter():
    elemList.append(elem.tag)

# now I remove duplicities - by convertion to set and back to list
elemList = list(set(elemList))

# Just printing out the result
#print(*elemList, sep='\n')
#for element in all_seg_tags:
    #element_tags = []
    #element_tags.append(element.attrib.values())
#
#print(element_tags)

def get_tags(tags):
    tag_list = []
    for tag in tags:
        tag_list.append(tag.attrib)
    return tag_list

all_tags = get_tags(all_seg_tags)
unique_seg_tags = list({v['ana']:v for v in all_tags}.values())
#print(*all_tags, sep='\n')
#print(*unique_seg_tags, sep='\n')

#counts = collections.Counter(x['ana'] for x in all_tags)
#print(counts)

#print(json.dumps(counts, indent=4))

#with open('ana_seg_tags.json', 'w') as outfile:
    #json.dump(counts, outfile)

#import xml.etree.ElementTree as ET
#
#tree = ET.parse('hj_tots_tei.xml')
#root = tree.getroot()
##print(root.tag)
##print(root.attrib)
#
#for child in root.iter():
    #print(child.tag, child.attrib)
#
#print(set([elem.tag for elem in root.iter() if '//.tei:elem.tag' == 'said']))

#for element in root.iter('div'):
    #print(element.text)
