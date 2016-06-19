# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 22:16:22 2016

@author: tutela
"""

import re
import lxml.html

def dictionary_maker():
    dic_translat = {}
    dic_transcrib = {}
    f = open('cedict_ts.u8', 'r', encoding = 'utf-8')
    for line in f:
        m = re.search('\s(\S*)\s\[[^\n]', line)
        m2 = re.search('\[(.*?)\][^/]', line)
        m3 = re.search('(/.*/)[^\n]', line)
        if m != None:
            word = m.group(1) 
            if m2 != None:
                transcrib = m2.group(1)
                dic_transcrib[word] = transcrib
            if m3 != None:
                translat = m3.group(1)
                translat = re.sub('/', ', ', translat)
                dic_translat[word] = translat
                    
                
        else:
            print('Error: Word is Not found')
    f.close
    return dic_transcrib, dic_translat
  
def translating(dic_transcrib, dic_translat):
    with open('translated.xml', 'w', encoding = 'utf-8') as file:
        x = 0
        header = '<html>\n<head>\n</head>\n<body>\n'
        file.write(header)
        for sentence in sentences:
            to_write = '<se>'
            word = ''
            for letter in sentence:
                if x == 1:
                    init = word
                    word += letter
                    if word in dic_translat:
                        x = 1
                    else:
                        x = 0
                        word = ''
                        transcr = dic_transcrib[init]
                        translat = dic_translat[init]
                        to_write += ('<w><ana lex=\"' + str(init) + '\" transcr=\"' 
                                        + str(transcr) + '\" sem=\"' + str(translat)
                                        + '\"/>' + str(init) + '</w>\n')
                if x == 0:
                    if letter not in dic_translat:
                        to_write += str(letter)
                    if letter in dic_translat:
                        init = letter
                        word += letter
                        x = 1
            to_write += '</se>\n'
            to_write = re.sub('\", ', '\"', to_write)
            to_write = re.sub('\, "', '\"', to_write)
            file.write(to_write)
            
        finish = '</body>\n</html>\n'
        file.write(finish)
    return

dic_transcrib, dic_translat = dictionary_maker()
file = open('stal.xml', 'r', encoding = 'utf-8')
text = file.read()
file.close()
tree = lxml.html.fromstring(text)
sentences = tree.xpath('.//se//text()')
translating(dic_transcrib, dic_translat)

print('Done')
 
    
    
    
    
    
    
    
    
    
    
    
           

