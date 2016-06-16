# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 22:16:22 2016

@author: tutela
"""

import re

def finding(letters):
    letters4 = letters
    if letters in dic_translat:
        WRITING
        if len(letters3) != 0:
            letters3.reverse()
            finding(letters3)
    else:
        if len(letters) != 0:
            letters3 += letters.pop()
            finding(letters)
        else:
            WRITING Letters4
            letters = []
dic_translat = {}
dic_transcr = {}
mass = {'ignor_cancel' : '>', 'Done' : '<'}
punct = ['!', '\"', ';', ':', '?', '(',')', '-', '.', ',', '“', '”','！', '？', '：', '。', ' ']
f = open('cedict_ts.u8', 'r', encoding = 'utf-8')
for line in f:
    m = re.search('\s(\S*)\s\[[^\n]', line)
    m2 = re.search('\[(.*)\][^/]', line)
    m3 = re.search('/(.*)/[^\n]', line)
    if m != None:
        word = m.group(1)
        if m2 != None:
            transcr = m2.group(1)
            dic_transcr[word] = transcr
        if m3 != None:
            translat = m3.group(1)
            dic_translat[word] = translat
    else:
        print('Error: Word is Not found')
f.close  

file = open('stal.xml', 'r', encoding = 'utf-8')
text = file.read()
with open('translation.xml', 'w', encoding = 'utf-8') as tran:
    for letter in text:
        if state == 'ignor_cancel':
            state = 'check'
        if letter == '>':
            state = 'ignor_cancel'
        if letter == '<':
            state = 'Done'
        if letter in punct:
            state = 'write'
            
        if state == 'check':
            letters += letter
            
        if letter == ' ':
            state = 'write'
            
        if state == 'write':
            state = 'check'
            if letter2 in dic_translat:
                
              
