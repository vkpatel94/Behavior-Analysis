from lib2to3.pgen2 import token
from xml.etree import ElementTree as ET
import collections
import nltk


tree = ET.parse ('Feb27_GroupB.txt.xml')
root = tree.getroot ()

# find the turn length
e = 0
mod_tw = 0
meg_tw = 0
lynn_tw = 0
rita_tw = 0
alyssa_tw = 0
melany_tw = 0
caroline_tw = 0
ted_tw = 0
id = root[0][0][3][0][0].get('id')
print ('this is id= ', id, root[0][0][3][0][0], len(root[0][0][3][0]))
for i in range(len(root[0][0])):
    mod = root[0][0][i][0][0][0].text
    if mod == "luke":
        mod_tw = mod_tw + len(root[0][0][i][0])
        e = e + 1
turn_len = (mod_tw - (e * 7))/e
print(e, mod_tw)
print turn_len
print(len(root[0][0][0][0]))

#get the list of all the noun and participant
p = 0
List_Name = list()
List_Noun = list()

List = ['Hi', 'Ok', 'ok', 'day', 'hahaha', 'haha', 'yeah', 'day', 'Day', 'hehe', 'lol', 'bye','yeap','lot','yea','none','bc','u','yeahhhh']
for i in range (len (root[0][0])):
    for j in range (len (root[0][0][i][0])):
        if (root[0][0][i][0][j][0].text in List):
            break
        elif root[0][0][i][0][j][4].text == 'NN' and root[0][0][i][0][0][0].text != root[0][0][i][0][j][0].text and \
                        root[0][0][i][0][j][0].text != ':-RRB-' and root[0][0][i][0][j][0].text != 'PM':
            #print (p + 1, root[0][0][i][0][0][0].text, root[0][0][i][0][j][0].text)
            List_Noun.append (root[0][0][i][0][j][0].text)
            List_Name.append(root[0][0][i][0][0][0].text)
            p = p + 1

            # elif root[0][0][i][0][j][4].text =='PRP$':
            #      print(root[0][0][i][0][0][0].text , root[0][0][i][0][j][0].text)

print (List_Noun)

multi_noun=[item for item, count in collections.Counter(List_Noun).items() if count > 1]
print (multi_noun)
print(len(multi_noun), len(List_Noun))
List_Name_in=list() #all speakers who introduce the topic list
List_Noun_multi=list()
# this is to count or get all participant who introduce the topic
for i in range (len (multi_noun)):
    print(multi_noun[i])
    for j in range (len (List_Noun)):
        if(multi_noun[i]== List_Noun[j]):
            print( j,List_Name[j],List_Noun[j])
            List_Name_in.append (List_Name[j])
            List_Noun_multi.append(List_Noun[j])
            break








#print(len(List_Name_in),len(List_Noun_multi))
freq_noun=nltk.FreqDist(List_Noun_multi)
freq= nltk.FreqDist(List_Name_in)
print ([freq])
print ([freq_noun])





print ('number of sentence',len (root[0][0][0][0]))  # get the number of words in the senetence
print ('pos', root[0][0][3][0][7][4])  # pos
print ('word', root[0][0][5][0][0][0].text)  # word
print ('token',root[0][0][0][0][0])  # token
print ('sentence',root[0][0][4])  # sentence
print (root[0][0])  # sentences
print ('range',range (len (root[0][0])))  # range















'''
print(root.tag,root.attrib)
for child in root:
    print(child.tag,child.attrib)

print(root[0][0][1].text)

for superChild in root[0][0]:
    print(superChild.tag,superChild.attrib)
    
    
    
for superChild in root[0][0][0]:
    print(superChild.tag,superChild.attrib)

print(root[0][0][0][1].tag,root[0][0].text,root[0][0][2][0][0].attrib)
    
    
    

print(root[0][0].tag,root[0][0].text)

print(root.text)
Count = 0
for POS in root[0][0][2].iter('POS'):
        #print(POS.text)
        if POS.text == 'PRP':
            Count = Count + 1
        elif POS.text == 'PRP$':
            Count = Count + 1

print(Count)

id=root[0][0][2][0][0].get('id')
mod=root[0][0][2][0][0][0].text
print(id,mod)

'''
