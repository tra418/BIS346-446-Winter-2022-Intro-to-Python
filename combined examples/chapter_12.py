# Section 12.2.1 snippets
from textblob import TextBlob

text = 'Today is a beautiful day. Tomorrow looks like bad weather.'

blob = TextBlob(text)

blob


# Section 12.2.1 Self Check snippets

# Exercise 3
exercise_blob = TextBlob('This is a TextBlob')

exercise_blob


# Section 12.2.2 snippets
blob.sentences

blob.words


# Section 12.2.2 Self Check snippets

# Exercise 1
from textblob import TextBlob

ex = TextBlob('My old computer is slow. My new one is fast.')

ex.sentences

ex.words


# Section 12.2.3 snippets
blob

blob.tags


# Section 12.2.3 Self Check snippets

# Exercise 2
TextBlob('My dog is cute').tags


# Section 12.2.4 snippets
blob

blob.noun_phrases


# Section 12.2.4 Self Check snippets

# Exercise 1
TextBlob('The red brick factory is for sale').noun_phrases


# Section 12.2.5 snippets

# Getting the Sentiment of a TextBlob
blob

blob.sentiment

# Getting the polarity and subjectivity from the Sentiment Object
%precision 3

blob.sentiment.polarity

blob.sentiment.subjectivity

# Getting the Sentiment of a Sentence 
for sentence in blob.sentences:
    print(sentence.sentiment)


# Section 12.2.5 Self Check snippets

# Exercise 1
from textblob import Sentence

Sentence('The food is not good.').sentiment

Sentence('The movie was not bad.').sentiment

Sentence('The movie was excellent!').sentiment


# Section 12.2.6 snippets
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

blob

blob.sentiment

for sentence in blob.sentences:
    print(sentence.sentiment)
    

# Section 12.2.6 Self Check snippets

# Exercise 1
text = ('The food is not good. The movie was not bad. ' +
        'The movie was excellent!')  

exblob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

for sentence in exblob.sentences:
    print(sentence.sentiment)


# Section 12.2.7 snippets
blob

blob.detect_language()

spanish = blob.translate(to='es')

spanish

spanish.detect_language()

chinese = blob.translate(to='zh')

chinese

chinese.detect_language()

spanish.translate()

chinese.translate() 


# Section 12.2.7 Self Check snippets

# Exercise 1
blob = TextBlob('Today is a beautiful day.')

french = blob.translate(to='fr')

french

french.detect_language()



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.8 snippets
from textblob import Word

index = Word('index')

index.pluralize()

cacti = Word('cacti')

cacti.singularize()

from textblob import TextBlob

animals = TextBlob('dog cat fish bird').words

animals.pluralize()



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.8 Self Check snippets

# Exercise 1
from textblob import Word

Word('children').singularize()

Word('focus').pluralize()




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.9 snippets
from textblob import Word

word = Word('theyr')

word.spellcheck()

word.correct()  # chooses word with the highest confidence value

from textblob import TextBlob

sentence = TextBlob('Ths sentense has missplled wrds.')

sentence.correct()



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.9 Self Check snippets

# Exercise 2
from textblob import TextBlob

sentence = TextBlob('I canot beleive I misspeled thees werds')

sentence.correct()



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.10 snippets
from textblob import Word

word = Word('varieties')

word.stem()

word.lemmatize()



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.10 Self Check snippets

# Exercise 2
from textblob import Word

word = Word('strawberries')

word.stem()

word.lemmatize()



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.11 snippets
# NOTE: This section's Self Check snippets are included in this file
# because the self check continues the interactive session.

from pathlib import Path

from textblob import TextBlob

blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())

blob.word_counts['juliet']

blob.word_counts['romeo']

blob.word_counts['thou']

blob.words.count('joy')

blob.noun_phrases.count('lady capulet')


# Section 12.2.11 Self Check snippets

# Exercise 2
blob.word_counts['a']

blob.word_counts['an']

blob.word_counts['the']


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.12 snippets

# Getting Definitions
from textblob import Word

happy = Word('happy')

happy.definitions

# Getting Synonyms
happy.synsets

synonyms = set()

for synset in happy.synsets:
    for lemma in synset.lemmas():
        synonyms.add(lemma.name())

synonyms

# Getting Antonyms
lemmas = happy.synsets[0].lemmas()

lemmas

lemmas[0].antonyms()




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.12 Self Check snippets

# Exercise 2
from textblob import Word

word = Word('boat')

word.synsets

word.definitions


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.13 snippets
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

stops = stopwords.words('english')

from textblob import TextBlob

blob = TextBlob('Today is a beautiful day.')

[word for word in blob.words if word not in stops]




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.13 Self Check snippets

# Exercise 2
from nltk.corpus import stopwords

stops = stopwords.words('english')

from textblob import TextBlob

blob = TextBlob('TextBlob is easy to use.')

[word for word in blob.words if word not in stops]



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.14 snippets
from textblob import TextBlob

text = 'Today is a beautiful day. Tomorrow looks like bad weather.'

blob = TextBlob(text)

blob.ngrams()

blob.ngrams(n=5)



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.2.14 Self Check snippets

# Exercise 2
from textblob import TextBlob

blob = TextBlob('TextBlob is easy to use.')

blob.ngrams()


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.3.1 snippets

# Loading the Data
from pathlib import Path

from textblob import TextBlob

blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())

from nltk.corpus import stopwords

stop_words = stopwords.words('english')

# Getting the Word Frequencies
items = blob.word_counts.items()

# Eliminating the Stop Words
items = [item for item in items if item[0] not in stop_words]

# Sorting the Words by Frequency
from operator import itemgetter

sorted_items = sorted(items, key=itemgetter(1), reverse=True)

# Getting the Top 20 Words
top20 = sorted_items[1:21]

# Convert top20 to a DataFrame 
import pandas as pd

df = pd.DataFrame(top20, columns=['word', 'count'])  

df

# Visualizing the DataFrame 
axes = df.plot.bar(x='word', y='count', legend=False)

import matplotlib.pyplot as plt

plt.gcf().tight_layout()


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.3.2 snippets
# NOTE: This section's self check snippets are included in this file 
# because the interactive session continues into the self check.

# Loading the Text
from pathlib import Path

text = Path('RomeoAndJuliet.txt').read_text()

# Loading the Mask Image that Specifies the Word Cloud’s Shape
import imageio

mask_image = imageio.imread('mask_heart.png')

# Configuring the WordCloud Object
from wordcloud import WordCloud   

wordcloud = WordCloud(width=1000, height=1000, 
    colormap='prism', mask=mask_image, background_color='white')
   

# Generating the Word Cloud
wordcloud = wordcloud.generate(text)

# Saving the Word Cloud as an Image File
wordcloud = wordcloud.to_file('RomeoAndJulietHeart.png')

%matplotlib

import matplotlib.pyplot as plt

plt.imshow(wordcloud)

# Section 12.3.2 Self Check snippets

# Exercise 2
mask_image2 = imageio.imread('mask_star.png')

wordcloud2 = WordCloud(width=1000, height=1000,
    colormap='prism', mask=mask_image2, background_color='white')
    
wordcloud2 = wordcloud2.generate(text)

wordcloud2 = wordcloud2.to_file('RomeoAndJulietStar.png')



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.4 snippets
# NOTE: This section's self check snippets are included in this file 
# because the interactive session continues into the self check.

# Calculating Statistics and Readability Scores
from pathlib import Path

text = Path('RomeoAndJuliet.txt').read_text()

from textatistic import Textatistic

readability = Textatistic(text)

%precision 3

readability.dict()


# Section 12.4 Self Check snippets

# Exercise 2
readability.word_count / readability.sent_count  # sentence length

readability.char_count / readability.word_count  # word length

readability.sybl_count / readability.word_count  # syllables





##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.5 snippets
# Loading the Language Model

import spacy

nlp = spacy.load('en') 

# Creating a spaCy Doc
document = nlp('In 1994, Tim Berners-Lee founded the ' + 
    'World Wide Web Consortium (W3C), devoted to ' +
    'developing web technologies')
    
# Getting the Named Entities
for entity in document.ents:
    print(f'{entity.text}: {entity.label_}')
    



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.5 Self Check snippets

# Exercise 2
import spacy

nlp = spacy.load('en')

document = nlp('Paul J. Deitel is CEO of ' +
               'Deitel & Associates, Inc.')

for entity in document.ents:
    print(f'{entity.text}: {entity.label_}')


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.6 snippets

# Loading the Language Model and Creating a spaCy Doc
import spacy

nlp = spacy.load('en')  

# Creating the spaCy Docs
from pathlib import Path

document1 = nlp(Path('RomeoAndJuliet.txt').read_text())

document2 = nlp(Path('EdwardTheSecond.txt').read_text())

# Comparing the Books’ Similarity 
document1.similarity(document2)





##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 12.6 Self Check snippets

# Exercise 2
import spacy

nlp = spacy.load('en')  

from pathlib import Path

document1 = nlp(Path('RomeoAndJuliet.txt').read_text())

document2 = nlp(Path('Hamlet.txt').read_text())

document1.similarity(document2)

document3 = nlp(Path('Macbeth.txt').read_text())

document1.similarity(document3)

document4 = nlp(Path('KingLear.txt').read_text())

document1.similarity(document4)


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
