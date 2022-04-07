import pandas as pd

df = pd.read_csv(r'booknlp_data\turn_of_the_screw.tokens', delimiter='\t')
#print(df.head())
df = df[['sentence_ID', 'word', 'lemma', 'event']]
#print(df.head())
events = df[~df['event'].isnull()]
event_options = set(events.event.tolist())
#print(event_options)
real_events = events.loc[df.event == 'EVENT']
event_words = set(real_events.word.tolist())
print(len(event_words))















































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
