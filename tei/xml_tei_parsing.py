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
for element in all_seg_tags:
     #= collections.Counter(element.attrib.values())
    counts = []
    counts.append(element.attrib.values())
    #print(element.attrib.values())
    print(counts)
    for count in counts:
        counting = collections.Counter(count)
    print(counting)
    #counts = collections.Counter(attrib_counts)
    #print(counts)
    #print(element.attrib)


#print(all_seg_tags)

#for chapter in tree.iterfind('.//tei:div[@type="chapter"]', NSMAP):
    #tag = chapter.findall('.//tei:div[@type="paragraph"]/seg', NSMAP)
    #print(tag)

#def character_network(tree):
    #G = nx.Graph()
    #for chapter in tree.iterfind('.//tei:div[@type="chapter"]', NSMAP):
        #speakers = chapter.findall('.//tei:said', NSMAP)
        #print(len(speakers))
        #for i in range(len(speakers) - 1):
            #try:
                #speaker_i = speakers[i].attrib['who']
                #speaker_j = speakers[i + 1].attrib['toWhom']
                #if G.has_edge(speaker_i, speaker_j):
                    #G[speaker_i][speaker_j]['weight'] += 1
                #else:
                    #G.add_edge(speaker_i, speaker_j, weight=1)
            #except KeyError:
                #continue
    #return G
#
##G = character_network(tree.getroot())
#print(f"Number of nodes = {G.number_of_nodes()}, Number of Edges = #{G.number_of_edges()}")
##print(G.edges())
#interactions = collections.Counter()
#for speaker_i, speaker_j, data in G.edges(data=True):
    #interaction_count = data['weight']
    #interactions[speaker_i] += interaction_count
    #interactions[speaker_j] += interaction_count
#
##print(interactions)
#
#nodesizes = [interactions[speaker] * 5 for speaker in G]
#
#fig = plt.figure(figsize=(15, 15))
#pos = nx.spring_layout(G, k=5, iterations=200)
#nx.draw_networkx_edges(G, pos, alpha=0.4)
#nx.draw_networkx_nodes(G, pos, node_size=nodesizes, alpha=0.4)
#nx.draw_networkx_labels(G, pos, font_size=14)
#plt.axis('off')
#plt.show()
