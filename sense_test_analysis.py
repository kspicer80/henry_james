import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_rows', None)


df = pd.read_csv('sense_test.csv', header=0)
#print(df.head(100))
df.rename( columns={'Unnamed: 0':'token'}, inplace=True )
#print(df.head(50))
#print(df.nunique())
df = df.sort_values(by=['touch'], ascending=[False])
print(df.head(100))
#sound_counts = df[df['sound'] > .50].count()
#print(sound_counts)

df_mask=df['sound'] >= .50
sound_filtered = df[df_mask]
print(sound_filtered.shape)
print(sound_filtered.head(187))

df.mean().plot(kind='bar', color=['b', 'r', 'y', 'g'])
plt.show()