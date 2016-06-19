# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 17:29:56 2016

@author: Tutelaqaz
"""

import os
import re

class Catching_PR(object):
    def __init__(self, text_name, made_text_name):
        self.text_name = text_name
        self.made_text_name = made_text_name
        self.cases = {}
    def my_stem(self):
        command = str('mystem.exe -nlid ' + str(self.text_name) +' ' 
                        + str(self.made_text_name))
        os.system(command)
        
    def searching(self):
        x = 0
        case = []
        word = ''
        with open(str(self.made_text_name), 'r', encoding = 'utf-8') as f:
            for line in f:
                if x == 1:
                    m = re.findall('=S,[А-я]+,(неод|од)=([А-я]+),[А-я]+\|?', line)
                    if m != None:
                        x = 0
                        for l in m:
                            case.append(l[1])
                        if word in self.cases:
                            case += (self.cases[word])
                            self.cases[word] = case
                            case = []
                        else:
                            self.cases[word] = case
                            case = []
                    else:
                        x = 0
                else:
                    m = re.search('([А-я]+)(=PR=)', line)
                    if m != None:
                        x += 1
                        word = m.group(1)
                    else:
                        x = 0
        return self.cases
        
class Analisys(object):
    def __init__(self):
        self.one_case_PR = {}
    def deleting_PR(self, cases):
        words = []
        for word in cases:
            if cases[word] == []:
                words.append(word)
        for word in words:
            del cases[word]
        return cases
        
    def making_rating(self, cases):
        cases_rating = {}
        x = 0
        for PR in cases:
            case_mass = cases[PR]
            if len(case_mass) > 1:
                for case in case_mass:
                    if case in case_mass:
                        x += 1
                        cases_rating[case] = x
                    else:
                        x = 0
            else:
                case = case_mass[0]
                cases_rating[case] = 1
            cases[PR] = cases_rating
            cases_rating = {}
            x = 0
        return cases
    
    def choosing_case(self, cases):
        for PR in cases:
            x = 0
            case_rating = cases[PR]
            for case in case_rating:
                number = case_rating[case]
                if number > x:
                    x = number
                    one_case = case
            self.one_case_PR[PR] = one_case
        return self.one_case_PR

class Repairing(Catching_PR):
    def __init__(self, text_name, made_text_name):
        super().__init__(text_name, made_text_name)
        
    def changing_text(self, one_case_PR, changed_text):
        x = 0
        word = ''
        with open(str(self.made_text_name), 'r', encoding = 'utf-8') as f:
            file = open(str(changed_text), 'w', encoding = 'utf-8')
            for line in f:
                if x == 1:
                    searching_string = '([А-я]+=S,[А-я]+,(неод|од)=)[А-я]+(,[А-я]+)'
                    m = re.search(searching_string, line)
                    x = 0
                    if m != None:
                        part1 = m.group(1)
                        part2 = m.group(3)
                        case = one_case_PR[word]
                        line = str(part1) + str(case) + str(part2) + '\n'
                        file.write(line)
                    else:
                        file.write(line)
            
                else:
                    file.write(line)
                    m = re.search('([А-я]+)(=PR=)', line)
                    if m != None:
                        x += 1
                        word = m.group(1)
                    else:
                        x = 0
            file.close()
    