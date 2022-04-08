import json
from collections import Counter
import pandas as pd
pd.set_option('display.max_rows', None)

# Introductory Matters

with open('turn_of_the_screw.book', 'r') as f:
    book_data = json.load(f)
print(book_data.keys())
print(len(book_data['characters']))
print(book_data['characters'][0].keys())
print(book_data['characters'][1]['mentions']['proper'])
print(book_data['characters'][1]['mentions']['pronoun'])


# Character Analysis

#df_entities = pd.read_csv(r"booknlp_data\turn_of_the_screw.entities", delimiter="\t")
#print(df_entities.head(200))
#print(df_entities['text'].unique())
#
#def process(filename):
    #with open(filename) as f:
        #data = json.load(f)
    #return data
#
#def get_counter_from_dependency_list(dep_list):
    #counter = Counter()
    #for token in dep_list:
        #term = token['w']
        #tokenGlobalIndex = token['i']
        #counter[term] += 1
    #return counter
#
#data = process(r'booknlp_data\turn_of_the_screw.book')
#
#def create_character_data(data, printTop):
    #character_data = dict()
    #for character in data['characters']:
        #agentList = character['agent']
        #patientList = character['patient']
        #possList = character['poss']
        #modList = character['mod']
        #character_id = character['id']
        #count = character['count']
        #referential_gender_distribution = referential_gender_prediction = 'unknown'
#
        #if character['g'] is not None and character['g'] != 'unknown':
            #referential_gender_distribution = character['g']['inference']
            #referential_gender = character['g']['argmax']
#
        #mentions = character['mentions']
        #proper_mentions = mentions['proper']
        #max_proper_mention = ''
#
        #poss_items = []
        #agent_items = []
        #patient_items = []
        #mod_items = []
#
        #if len(mentions['proper']) > 0:
            #max_proper_mention = mentions['proper'][0]['n']
#
            #for k, v in get_counter_from_dependency_list(possList).most_common(printTop):
                #poss_items.append((v, k))
#
            #for k, v in get_counter_from_dependency_list(agentList).most_common(printTop):
                #agent_items.append((v, k))
#
            #for k, v in get_counter_from_dependency_list(patientList).most_common(printTop):
                #patient_items.append((v, k))
#
            #for k, v in get_counter_from_dependency_list(modList).most_common(printTop):
                #mod_items.append((v, k))
#
            #character_data[character_id] = {
                                    #'id': character_id,
                                    #'max_proper_mention': max_proper_mention,
                                    #'referential_gender': referential_gender,
                                    #'possList': poss_items,
                                    #'agentList': agent_items,
                                    #'patientList': patient_items,
                                    #'modList': mod_items
                                    #}
    #return character_data
#
#character_data = create_character_data(data, 10)
##print(character_data)
#
#def find_verb_usage(data, analysis = ['agent', 'patient']):
    #verb_analysis = []
    #for item in analysis:
        #if item == 'agent':
            #verb_analysis.append('agentList')
        #elif item == 'patient':
            #verb_analysis.append('patientList')
    #main_agents = {}
    #main_patients = {}
    #for character in character_data:
        #temp_data = character_data[character]
        #for item in verb_analysis:
            #for verb in temp_data[item]:
                #verb = verb[1].lower()
                #if item == 'agentList':
                    #if verb not in main_agents:
                        #main_agents[verb] = [(character, temp_data['max_proper_mention'])]
                    #else:
                        #main_agents[verb].append((character, temp_data['max_proper_mention']))
                #elif item == 'patientList':
                    #if verb not in main_patients:
                        #main_patients[verb] = [(character, temp_data['max_proper_mention'])]
                    #else:
                        #main_patients[verb].append((character, temp_data['max_proper_mention']))
    #verb_usage = {'agent': main_agents, 'patient': main_patients}
    #return verb_usage
#
#verb_data = find_verb_usage(data)
#print(verb_data['agent']['said'])

# Event Analysis

#df = pd.read_csv('turn_of_the_screw.tokens', delimiter='\t')
##print(df.head())
#df = df[['sentence_ID', 'word', 'lemma', 'event']]
##print(df.head())
#events = df[~df['event'].isnull()]
#event_options = set(events.event.tolist())
##print(event_options)
#real_events = events.loc[df.event == 'EVENT']
#event_words = list(set(real_events.word.tolist()))
##print(len(event_words))
##print(event_words[:10])
#
#sentences = real_events.sentence_ID.tolist()
#events = real_events.word.tolist()
##print(sentences[:10])
#
#sentence1 = sentences[0]
#result = df[df['sentence_ID'] == int(sentence1)]
#
#words = result.word.tolist()
##print(words)
#
#resentence = ' '.join(words)
#
#def grab_event_sentences(file):
    #df = pd.read_csv(file, delimiter = '\t')
    #real_events = df.loc[df.event == 'EVENT']
    #sentences = real_events.sentence_ID.tolist()
    #event_words = real_events.word.tolist()
    #event_lemmas = real_events.lemma.tolist()
    #final_sentences = []
    #x=0
    #for sentence in sentences:
        #result = df[df['sentence_ID'] == int(sentence)]
        #words = result.word.tolist()
        #resentence = ' '.join(words)
        #final_sentences.append({
            #'event_word': event_words[x],
            #'event_lemmas': event_lemmas[x],
            #'sentence': resentence
        #})
        #x = x+1
    #return final_sentences
#
#data = grab_event_sentences('turn_of_the_screw.tokens')
##print(data[:10])
#
#new_event_centric_df = pd.DataFrame(data)
#new_event_centric_df.to_csv('test_file.events', index=False)

















































#from booknlp.booknlp import BookNLP
#
#model_params = {
                #'pipeline': 'entity,quote,supersense,event,coref',
                #'model': 'big'
#}
#
#booknlp = BookNLP('en', model_params)
#
#input_file = 'tots.txt'
#output_directory = 'tots/'
#book_id = 'turn_of_the_screw_omf'
#
#booknlp.process(input_file, output_directory, book_id)
