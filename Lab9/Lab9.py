## David Zheng
## Lab 9

import random
import os


nouns = ['cat', 'dog', 'bug', 'man', 'woman', 'friend', 'fish', 'bird', 'cow', 'horse']

verbs = ['slept', 'napped', 'jumped', 'skipped', 'ran', 'sat', 'snored', 'ate', 'screamed', 'blinked']

fn1 = 'adverbs.txt'
fh1 = open(fn1, mode = 'r')
adverbstxt = fh1.readlines()
for e in adverbstxt:
    adverbs = e.split(', ')
fh1.close()


fn2 = 'adjectives.txt'
fh2 = open(fn2, mode = 'r')
adjectives = fh2.readlines()
fh2.close()


    
def MakeSentence(nouns, verbs, adverbs, adjectives):
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    adverb = adverb.strip()
    adjective = random.choice(adjectives)
    adjective = adjective.strip()
    ##Construct the full sentence from selected words
    sentence = 'The %s %s %s %s.' % (adjective, noun, verb, adverb)
    
    return sentence

output1 = open('output1.txt' ,'w')
output2 = open('output2.txt' ,'w')
sentences = []
for j in range(5):
    s = MakeSentence(nouns, verbs, adverbs, adjectives)
    n = str(j + 1)
    s2 = str(s + ' ')
    s3 = (n + '. ' + s2 + '\n')
    output1.write(s3)
    output2.write(s2)
    print(s3)
    
output1.close()
output2.close()


