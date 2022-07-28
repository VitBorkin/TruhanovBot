# Running this file creates from the canz.txt the list of non lexical words and creates cenz.json file to sort chat and clean it
# Before running this file update cenz.txt with ful list of non cenzured words

import json

ar = []

with open('cenz.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

    with open('cenz.json', 'w', encoding='utf-8') as e:
        json.dump(ar, e)