# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 19:19:16 2016

@author: Tutelaqaz
"""
from Catching_PR import Catching_PR
from Catching_PR import Analisys
from Catching_PR import Repairing

text_name = input('Input the name of the text for stemming:')
made_text_name = input('Input the name of the stemmed text:')
#text_name = 'Remark.txt'
#made_text_name = 'made_text.txt'
sp = Catching_PR(text_name, made_text_name)
sp.my_stem()
cases = sp.searching()

an = Analisys()
cases = an.deleting_PR(cases)
cases = an.making_rating(cases)
one_case_PR = an.choosing_case(cases)

rep = Repairing(text_name, made_text_name)
#changed_text = 'repaired.txt'
changed_text = input('Input the name of the changed text:')
rep.changing_text(one_case_PR, changed_text)



            

