
# coding: utf-8


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize


#with open('Feb27_GroupA.txt') as o:
#    print(o.read())

text_file = open('Feb27_GroupA.txt').read()

# sentence = sent_tokenize(text_file)
# print sentence



tokens = nltk.word_tokenize(text_file)
print tokens

filtered_tokens = [word for word in tokens if word not in stopwords.words('english') and word not in ['?','!',')',',',':','(','-','.','PM']]

print filtered_tokens

filtered_tokens


freq = nltk.FreqDist(filtered_tokens)
print freq.most_common(100)