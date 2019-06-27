import re
import nltk
import numpy as np
import pandas as pd
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from gensim.models import Phrases
from gensim.corpora import Dictionary
import os

path = "data.dat"
exists = os.path.isfile(path)
if exists:
    os.remove(path)
f=open(path,"a+")
directory = os.path.join("raw-data")
root,dirs,files = next(os.walk(directory))
file_count = 0
for file in files:
    if file.endswith(".txt"):
        file_count = file_count +1
f.write(str(file_count))
f.write('\n')
for file in files:
    if file.endswith(".txt"):
        with open(directory+"/"+file, 'r') as file:
            data = file.read().replace('\n', ' ')
            print('Preprocessing data')

            input_str = data
            # Remove non-alphabetical / whitespace characters
            input_str = re.sub(r'[-.!]', ' ', input_str)
            input_str = re.sub(r'[^\s^\w]', '', input_str)
            input_str = re.sub(r'[0-9]', '', input_str)

            # Lowercase
            input_str = input_str.lower()

            # Tokenize (break up into individual document words)
            document_words = nltk.word_tokenize(input_str)

            # Lemmatize (e.g. friends -> friend, walking -> walk)
            lemmatizer = WordNetLemmatizer()
            stems = list()
            for word in document_words:
                stems.append(lemmatizer.lemmatize(word))

            # Get standard list of english stop words
            stop = stopwords.words('english')

            # Add any additional stopwords
            stop.extend(['the', 'na','u','p','wa'])

            # Strip stopwords (they have little value in this context)
            stems = list(filter(lambda x: x not in stop, stems))
            # print(stems)

            # Reset to one long string, so that vectorizer won't complain
            output = u' '.join(stems)
            # print(output)
            f.write(output)
            f.write('\n')
            #print(data)
f.close()           

print('Preprocessing done. Please view data.dat file')

    
