import nltk
from nltk.corpus import brown, movie_reviews, reuters
from nltk.corpus import webtext


nltk.download('webtext')
nltk.download('nps_chat')



posts = nltk.corpus.nps_chat.xml_posts()


posts = nltk.corpus.nps_chat.xml_posts()[:10000]

def DA_features(post):
     features = {}
     for word in nltk.word_tokenize(post):
         features['contains({})'.format(word.lower())] = True
     return features

featuresets = [(DA_features(post.text), post.get('class'))
                for post in posts]
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
# classifier = SklearnClassifier(LogisticRegression())
# classifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))


DiaAct_A = []
DiaAct_B = []
users = []
textsp =  []
textsp1 =  []
countA = {}
countB = {}
DisA = {}
DisB = {}
with open('Feb27_GroupA.txt', 'r') as groupA:
    for line in groupA:
        user = line.split('PM):')[0]
        userf = user.split(' (')[0]
        text = line.split('PM):')[1]
        textsp.append(text)
        users.append(userf)
        DiaAct_A.append(classifier.classify(DA_features(text)))
        if (classifier.classify(DA_features(text)) == "ynQuestion" or classifier.classify(DA_features(text)) == "whQuestion"):
            u = userf
            if(u in countA):
                countA[u] = countA[u] + 1
            else:
                countA[u] = 1
groupA.close()

print ('Directive index',countA)

with open('Feb27_GroupB.txt', 'r') as groupB:
    for line in groupB:
        user = line.split('PM):')[0]
        userf = user.split(' (')[0]
        text = line.split('PM):')[1]
        textsp1.append(text)
        users.append(userf)
        DiaAct_B.append(classifier.classify(DA_features(text)))
        if (classifier.classify(DA_features(text)) == "ynQuestion" or classifier.classify(DA_features(text)) == "whQuestion"):
            u = userf
            if(u in countB):
                countB[u] = countB[u] + 1
            else:
                countB[u] = 1
groupB.close()

print ('Directive index:',countB)


with open('Feb27_GroupA.txt', 'r') as groupA:
    for line in groupA:
        user = line.split('PM):')[0]
        userf = user.split(' (')[0]
        text = line.split('PM):')[1]
        textsp.append(text)
        users.append(userf)
        DiaAct_A.append(classifier.classify(DA_features(text)))
        if (classifier.classify(DA_features(text)) == "Reject" or classifier.classify(DA_features(text)) == "nAnswer"):
            u = userf
            if(u in DisA):
                DisA[u] = DisA[u] + 1
            else:
                DisA[u] = 1
groupA.close()

print ('Disagreement',DisA)

with open('Feb27_GroupB.txt', 'r') as groupB:
    for line in groupB:
        user = line.split('PM):')[0]
        userf = user.split(' (')[0]
        text = line.split('PM):')[1]
        textsp1.append(text)
        users.append(userf)
        DiaAct_B.append(classifier.classify(DA_features(text)))
        if (classifier.classify(DA_features(text)) == "Reject" or classifier.classify(DA_features(text)) == "nAnswer    "):
            u = userf
            if(u in DisB):
                DisB[u] = DisB[u] + 1
            else:
                DisB[u] = 1
groupB.close()

print ('Disagreement:',DisB)


print DiaAct_A
print DiaAct_B



