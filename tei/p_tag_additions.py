import lxml
import lxml.etree




tree = lxml.etree.parse(lww_xml)
print(tree.getroot().find('.//{http://www.tei-c.org/ns/1.0}title').text)
print(tree.getroot().find('title'))

NSMAP = {'tei': 'http://www.tei-c.org/ns/1.0'}
print(tree.getroot().find('.//tei:title', namespaces=NSMAP).text)

def character_network(tree):
    G = nx.Graph()
    for chapter in tree.iterfind('.//tei:div[@type="chapter"]', NSMAP):
        speakers = chapter.findall('.//tei:said', NSMAP)
        print(len(speakers))
        for i in range(len(speakers) - 1):
                try:
                    speaker_i = speakers[i].attrib['who']
                    speaker_j = speakers[i + 1].attrib['toWhom']
                    if G.has_edge(speaker_i, speaker_j):
                        G[speaker_i][speaker_j]['weight'] += 1
                    else:
                        G.add_edge(speaker_i, speaker_j, weight=1)
                except KeyError:
                    continue
    return G