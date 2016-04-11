import pickle
import re
import nltk
pos=negat=neu=0
def get_words_in_tweet(tweet):
   wordList = re.sub("[^\w]", " ",tweet).split()
  # print wordList
   return wordList
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


f = open('my_classifier.pickle008', 'rb')
classifier = pickle.load(f)
open('classified.txt', 'w').close()
open('pre_processing.txt', 'w').close()
execfile('pre_processing.py')
File=open("twitDB46.txt")

File1=open("pre_processing.txt")
N=50

for i in range(N):
    original_line=File.next().strip()
    original_tweet=original_line
    processed_line=File1.next().strip()
    processed_tweet=processed_line
    word_features = get_word_features(get_words_in_tweet(processed_tweet))  
    classified_score=classifier.classify(extract_features(processed_tweet.split()))
    score=classified_score
    if(score=='4'):
       pos=pos+1
       classified_score='POSITIVE'
    
    if(score=='0'):
       negat=negat+1
       classified_score='NEGATIVE'

    if(score=='2'):
       neu=neu+1
       classified_score='NEUTRAL '
       
    classified_Tweet= classified_score+ ":  "+original_tweet
    saveFile=open('classified.txt','a')
    saveFile.write(classified_Tweet)
    saveFile.write('\n')
    
posfile=open('poscount.txt','w')
posfile.write(str(pos))
posfile.close()
negfile=open('negcount.txt','w')
negfile.write(str(negat))
negfile.close()
neutralfile=open('neutralcount.txt','w')
neutralfile.write(str(neu))
neutralfile.close()
f.close();
File.close();
File1.close();
saveFile.close()
