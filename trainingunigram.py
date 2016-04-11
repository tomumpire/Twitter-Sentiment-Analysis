#from __future__ import absolute_import, division, print_function, unicode_literals
import csv
import nltk
import pickle
import codecs
#import sys  
File=open('trainingdata2016.csv')
Reader = csv.reader(File)
Data = list(Reader)
tweets = []
#reload(sys)
#sys.setdefaultencoding('Cp1252')
row_count = sum(1 for row in Data)
#print row_count
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    #print (all_words)
    return all_words

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

for row in range(row_count):
    string=(Data[row][1])
    string1=nltk.word_tokenize(string.decode('utf-8')) 
    tweets.append((string1,Data[row][0]))
    
File.close();
#print sum(1 for row in tweets)
#print tweets

word_features = get_word_features(get_words_in_tweets(tweets))
training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)
f = open('my_classifier.pickle008', 'wb')
pickle.dump(classifier, f)
f.close()

#tweet = 'william dafoe'
#print classifier.classify(extract_features(tweet.split()))



