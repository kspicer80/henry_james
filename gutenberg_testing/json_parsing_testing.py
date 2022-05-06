from pathlib import Path
import json


#path = Path('henry_james_gutenberg_ids.json')
#print(path.exists())
#print(path.absolute())

#f = open(r'C:\Users\KSpicer\Documents\GitHub\henry_james\gutenberg_testing\henry_james_gutenberg_ids.json', 'r')
#data = json.loads(f.read())
#f.close()
#print(data)

with open(r'C:\Users\KSpicer\Documents\GitHub\henry_james\gutenberg_testing\henry_james_gutenberg_ids.json', 'r') as f:
    data = json.load(f)
#print(data)
##print(type(data))
#
##print(data['results'][0]['id'])
##print(data['results'][1]['id'])
#
#for i in range(len(data['results'])):
    #print(data['results'][i]['id'], data['results'][i]['title'])
#
#print(len(data['results']))

for item in data['results']:
    id = item['id']
    title = item['title']
    print(id, title)
    
#new_string = json.dumps(data, indent=2)
#print(new_string)
