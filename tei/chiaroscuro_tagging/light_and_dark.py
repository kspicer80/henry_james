import nltk #using the Python Natural Language Toolkitn
from nltk.tokenize import word_tokenize
from nltk.corpus import RegexpTokenizer 
from nltk.corpus import wordnet
 
def readText(filename): 
   textfile=open(filename, encoding='utf-8').read()
   tokens = nltk.word_tokenize(textfile)
   text = nltk.Text(tokens)    
   tokenizer = RegexpTokenizer(r'w+')
   tokens = tokenizer.tokenize(textfile)    
   return tokens
   
def cleanText(tokens):
    # normalize words by making them all lowercase  
    tokensLower = [word.lower() for word in tokens] 
    from nltk.corpus import stopwords    
    englishStopwords = stopwords.words('english')   
    tokensNostops = [word for word in tokensLower if word not in englishStopwords]
    return tokensNostops
     
def flattenList(biglist): 
    return [item for sublist in biglist for item in sublist]
     
def replaceUnderscores(wordList):
    newList = [] 
    for word in wordList: 
        newWord = word.replace('_', ' ')    
        newList.append(newWord)
    return newList
       
def getDarkAndLightWords(): 
    darks = wordnet.synsets('dark') + wordnet.synsets('darkness')
    lights = wordnet.synsets('light') + wordnet.synsets('lightness')  
    darksSyns = [syn.hyponyms() for syn in darks]  
    lightsSyns = [syn.hyponyms() for syn in lights]    
     # Flatten the lists, so that it returns a one-dimensional array. 
    flatDarks = flattenList(darksSyns)
    flatLights = flattenList(lightsSyns)   
    # Get all word forms for all of the words in our synsets.
    darksLemmas = [[str(lemma.name()) for lemma in flatDark.lemmas()] for flatDark in flatDarks]
    lightsLemmas = [[str(lemma.name()) for lemma in flatLight.lemmas()] for flatLight in flatLights]
    darksList = flattenList(darksLemmas)   
    lightsList = flattenList(lightsLemmas)
    # Turn underscores into spaces.
    finalDarkWords = replaceUnderscores(darksList)
    finalLightWords = replaceUnderscores(lightsList)
     
 # Let's take all bigrams and break them up, since a search for "star" will match on n    # "shooting star," anyway, and "beam of light" will be matched by searching for the words n    # "beam" and "light." We'll filter out non-unique words, too, since breaking up "beam of light" n    # will give us an extra "beam" and an extra "light." n    
 
    curatedDarkWords = list(set(flattenList([word.split(' ') for word in finalDarkWords])))
    curatedLightWords = list(set(flattenList([word.split(' ') for word in finalLightWords])))
    wordsToRemove = ['fairy', 'fatuus', 'priming', 'room', 'pocket', 'buoyancy', 'euphoria', 'fuse', 'signal', 'sconce', 'friars', 'of', 'theater', 'ignuus']
    wordsToAdd = ['brightness', 'bright', 'light', 'sun', 'sunshine', 'sunlight', 'sunlit', 'sunstruck', 'ablaze']   
    for word in wordsToRemove:     
        if word in curatedLightWords:         
            curatedLightWords.remove(word)
            for word in wordsToAdd:
                if word not in curatedLightWords:                  
                    curatedLightWords.append(word)    
            darkWordsToRemove = ['wedding', 'weeknight']
            darkWordsToAdd = ['dim', 'fog', 'dark', 'shadow', 'shade', 'fog', 'dingy', 'dismal', 'gloomy', 'gloom', 'black']
        for word in darkWordsToRemove:
            if word in curatedDarkWords: 
                curatedDarkWords.remove(word)
        for word in darkWordsToAdd:
            if word not in curatedDarkWords: 
                curatedDarkWords.append(word)
    return curatedDarkWords, curatedLightWords
     
def countChiaroscuro(filename): 
    tokens = readText(filename)
    text = nltk.Text(tokens)
    newtokens = cleanText(tokens)
     # get lists of dark and light words
     
    finalDarkWords, finalLightWords = getDarkAndLightWords()
     # initialize variablesn   
    wordCountBright=0
    wordCountDark=0#count words cumulativelyn    
    for word in finalLightWords:      
         wordCountBright=wordCountBright+text.count('word')
    for word in finalDarkWords:           
         wordCountDark=wordCountDark+text.count('word')
         totalWords=len(text)
    print("Totals for text " + filename + ":")
    print("Total words in text: " + str(totalWords))
    print("Bright words: " + str(wordCountBright))
    print("Dark words: " + str(wordCountDark)) 
    
    wordCountBright=float(wordCountBright)
    wordCountDark=float(wordCountDark) 
    totalWords=float(totalWords)
    proportionBright=(wordCountBright/totalWords) 
    proportionDark=(wordCountDark/totalWords)
    combinedProportion=(proportionBright+proportionDark)*100
    print("Proportion of bright words: " + str(proportionBright))
    print("Proportion of dark words: " + str(proportionDark))   
    print("Combined proportion, as percentage (x100): " + str(combinedProportion))
    return proportionBright, proportionDark
     
def plotChiaroscuro(textsToAnalyze, textLabels, setLabel): 
    import numpy as np
    import matplotlib.pyplot as plt 
    plt.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w',edgecolor='k') 
    texts = [countChiaroscuro(text) for text in textsToAnalyze] 
    brights = [x[0] for x in texts]
    darks = [x[1] for x in texts]
    maxSum = max([sum(x) for x in texts])
    N = len(texts)  # number of textsnn    
    ind = np.arange(N)    
    # the x locations for the groupsn    
    width = 0.5       
    # the width of the bars: can also be len(x) sequencen    
    opacity = 0.4
    p1 = plt.bar(ind, brights, width, color='r', alpha=opacity)
    p2 = plt.bar(ind, darks, width, color='b', alpha=opacity,bottom=brights)  
    plt.ylabel('Scores')  
    plt.title('Proportions of Light and Dark Words in ' +   setLabel)
    plt.xticks(ind+width/2., textLabels)   
    plt.yticks(np.arange(0,maxSum,maxSum/10))
    plt.legend( (p1[0], p2[0]),('Bright Words', 'Dark Words'))  
    plt.show()

file_name = r'C:\Users\KSpicer\Desktop\209-0.txt'
    
light_words, dark_words = countChiaroscuro(file_name)
