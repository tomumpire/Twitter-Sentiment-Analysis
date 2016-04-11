import pickle
import re
import nltk
import os
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
target = open("classified1.hta", 'w')
html_str="""<html>
             <head>
 <style type='text/css'>
  .bold-green-font {
    font-weight: bold;
    color: green;
  }

  .bold-font {
    font-weight: bold;
  }

  .right-text {
    text-align: right;
  }

  .large-font {
    font-size: 15px;
  }

  .italic-darkblue-font {
    font-style: italic;
    color: darkblue;
  }

  .italic-purple-font {
    font-style: italic;
    color: purple;
  }

  .underline-blue-font {
    text-decoration: underline;
    color: blue;
  }

  .gold-border {
    border: 3px solid gold;
  }

  .deeppink-border {
    border: 3px solid deeppink;
  }

  .orange-background {
    background-color: orange;
  }

  .orchid-background {
    background-color: orchid;
  }

  .beige-background {
    background-color: beige;
  }

</style>
  
             <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
             <script type="text/javascript">
             google.charts.load('current', {'packages':['table']});
             google.charts.setOnLoadCallback(drawTable);
function drawTable() {
var cssClassNames = {
    'headerRow': 'italic-darkblue-font large-font bold-font',
    'tableRow': '',
    'oddTableRow': 'beige-background',
    'selectedTableRow': 'orange-background large-font',
    'hoverTableRow': '',
    'headerCell': 'gold-border',
    'tableCell': '',
    'rowNumberCell': 'underline-blue-font'};

  var options = {'showRowNumber': true, 'allowHtml': true, 'cssClassNames': cssClassNames};
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Sentiment');
        data.addColumn('string', 'Tweet');
        data.addRows(["""

target.write(html_str)

for i in range(N):
    original_line=File.next().strip()
    original_tweet=original_line
    processed_line=File1.next().strip()
    processed_tweet=processed_line
    word_features = get_word_features(get_words_in_tweet(processed_tweet))  
    classified_Tweet=classifier.classify(extract_features(processed_tweet.split()))
    original_tweet=original_tweet.replace('\'','')
    score=classified_Tweet
    if(score=='4'):
       pos=pos+1
       classified_Tweet='POSITIVE'
    
    if(score=='0'):
       negat=negat+1
       classified_Tweet='NEGATIVE'

    if(score=='2'):
       neu=neu+1
       classified_Tweet='NEUTRAL'
    target.write("['"+classified_Tweet+ "\','" +original_tweet+"'],");
    #classified1.write('\n')
   
target.seek(-1, os.SEEK_END)
target.truncate()
html_str2=""" ]);

        var table = new google.visualization.Table(document.getElementById('table_div'));

        table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
      }
    </script>
  </head>
  <body>
    <div id="table_div"></div>
  </body>
</html>"""
target.write(html_str2)
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
target.close()
