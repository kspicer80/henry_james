import lxml
import lxml.etree
import networkx as nx
import matplotlib.pyplot as plt
import collections
nsmap = {'tei': 'http://www.tei-c.org/ns/1.0'}

tots_xml = r"tei\hj_tots_tei.xml"

tree = lxml.etree.parse(tots_xml)
#print(tree.getroot().find('.//{http://www.tei-c.org/ns/1.0}title').text)
#print(tree.getroot().find('title'))

all_seg_tags = tree.findall(".//tei:seg", namespaces=nsmap)
#print(all_seg_tags)

for element in all_seg_tags:
    element_tags = []
    element_tags.append(element.attrib.values())
    
#print(element_tags)

def get_tags(tags): 
    tag_list = []
    for tag in tags:
        tag_list.append(tag.attrib)
    return tag_list

all_tags = get_tags(all_seg_tags)
#print(all_tags)

counts = collections.Counter(x['ana'] for x in all_tags)    
print(counts)
