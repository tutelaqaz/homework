import os
import re
def wikiextractor_usage():
    command = "python2 /home/tutela/Project_Python/Wikiextractor/WikiExtractor.py -o /home/tutela/Project_Python/Wikiextractor/ /home/tutela/Project_Python/Wikiextractor/tpiwiki-20160305-pages-meta-current.xml"
           
    os.system(command)

    words = []
    wordlist = {}
    f = open('/home/tutela/Project_Python/Wikiextractor/AA/wiki_00','r', encoding  = 'utf-8')
    for line in f:
        wordsinline= line.split()
        words += wordsinline
    f.close()
    for word in words:
        word = word.lower()
        word = word.strip('.,!\;[]?«»:\'\/<>~{}()\"-_=+@#$%^&*|\\')
        m = re.search('(url)|(id)|(title)|(http)|(\\d)', word)
        if m == None:
            if word in wordlist:
                wordlist[word] += 1
            else:
                wordlist[word] = 1
    return wordlist

def diction_sorting(wordlist):
    l = lambda x: x[1]
    sorted_wordlist = sorted(wordlist.items(), key=l, reverse=True)
    return sorted_wordlist

def writing(sorted_wordlist):          
    file = open('Dictionary.txt', 'w', encoding = 'utf-8')
    for k in sorted_wordlist:
        file.write(k[0])
        file.write(' ')
        file.write(str(k[1]))
        file.write('\n')
    file.close()
    return

wordlist = wikiextractor_usage()
sorted_wordlist = diction_sorting(wordlist)
writing(sorted_wordlist)

print('The end')
