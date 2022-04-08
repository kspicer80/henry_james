import pandas as pd

df = pd.read_csv('turn_of_the_screw.tokens', delimiter='\t')
#print(df.head())
df = df[['sentence_ID', 'word', 'lemma', 'event']]
#print(df.head())
events = df[~df['event'].isnull()]
event_options = set(events.event.tolist())
#print(event_options)
real_events = events.loc[df.event == 'EVENT']
event_words = list(set(real_events.word.tolist()))
#print(len(event_words))
#print(event_words[:10])

sentences = real_events.sentence_ID.tolist()
events = real_events.word.tolist()
#print(sentences[:10])

sentence1 = sentences[0]
result = df[df['sentence_ID'] == int(sentence1)]

words = result.word.tolist()
#print(words)

resentence = ' '.join(words)

def grab_event_sentences(file):
    df = pd.read_csv(file, delimiter = '\t')
    real_events = df.loc[df.event == 'EVENT']
    sentences = real_events.sentence_ID.tolist()
    event_words = real_events.word.tolist()
    event_lemmas = real_events.lemma.tolist()
    final_sentences = []
    x=0
    for sentence in sentences:
        result = df[df['sentence_ID'] == int(sentence)]
        words = result.word.tolist()
        resentence = ' '.join(words)
        final_sentences.append({
            'event_word': event_words[x],
            'event_lemmas': event_lemmas[x],
            'sentence': resentence
        })
        x = x+1
    return final_sentences

data = grab_event_sentences('turn_of_the_screw.tokens')
#print(data[:10])

new_event_centric_df = pd.DataFrame(data)
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
