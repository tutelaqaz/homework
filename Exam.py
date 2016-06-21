# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:25:46 2016

@author: Tutelaqaz
"""
import csv
import re
def periods_finding():
    
    x = 0
    dates = {}
    periods = {'50-60': [], '60-70': [], '70-80': [], '80-90': [], '90-00': [], 
           '00-10': [], '10-15': []}
    perioni = []
    with open('source_post1950_wordcount.csv', 'r', encoding = 'utf-8') as file:
        inputfile = csv.reader(file, delimiter = ';')
        for row in inputfile:
            if x != 0:
                path = row[0]
                date = row[5]
                dates[path] = date
            else:
                x +=1         
    for path in dates:
        m = re.search('-1960', str(dates[path]))
        m2 = re.search('-1970', str(dates[path]))
        m3 = re.search('-1980', str(dates[path]))
        m4 = re.search('-1990', str(dates[path]))
        m5 = re.search('-2000', str(dates[path]))
        m6 = re.search('-2010', str(dates[path]))
        m7 = re.search('-2015', str(dates[path]))
        if m != None:
            periods['50-60'].append(path)
            perioni.append(path)
        if m2 != None:
            periods['60-70'].append(path)
            perioni.append(path)
        if m3 != None:
            periods['70-80'].append(path)
            perioni.append(path)
        if m4 != None:
            periods['80-90'].append(path)
            perioni.append(path)
        if m5 != None:
            periods['90-00'].append(path)
            perioni.append(path)
        if m6 != None:
            periods['00-10'].append(path)
            perioni.append(path)
        if m7 != None:
            periods['10-15'].append(path)
            perioni.append(path)
    return periods
    
def lenghts_finding():
    lenghts = {}
    x = 0
    more_than_100k = {}
    more_than_90k = {}
    more_than_80k = {}
    more_than = {}
    with open('source_post1950_wordcount.csv', 'r', encoding = 'utf-8') as file:
        inputfile = csv.reader(file, delimiter = ';')
        for row in inputfile:
            if x != 0:
                path = row[0]
                leng = row[22]
                lenghts[path] = leng
            else:
                x +=1
        for path in lenghts:
            words = lenghts[path]
            if words != 'none':
                if int(words) > 100000:
                    more_than_100k[path] = words
                elif int(words) < 100000 and int(words) > 90000:
                    more_than_90k[path] = words
                elif int(words) < 90000 and int(words) > 80000:
                    more_than_80k[path] = words
                elif int(words) < 80000 and int(words) > 0:
                    more_than[path] = words
    return lenghts, more_than_100k, more_than_90k, more_than_80k, more_than

def sphere_finding():
    spheres = {}
    x = 0
    with open('source_post1950_wordcount.csv', 'r', encoding = 'utf-8') as file:
        inputfile = csv.reader(file, delimiter = ';')
        for row in inputfile:
            if x != 0:
                sphere = row[6]
                path = row[0]
                if sphere in spheres:
                    spheres[sphere].append(path)
                else:
                    spheres[sphere] = []
                    spheres[sphere].append(path)
            else:
                x += 1
    num_of_spheres = {}
    for sphere in spheres:
        num = len(sphere)
        num_of_spheres[sphere] = num
    procent = 0
    for sphere in num_of_spheres:
        procent += num_of_spheres[sphere]
    procent = procent / 100
    procent_of_sphere = {}
    for sphere in num_of_spheres:
        procent_of_sphere[sphere] = num_of_spheres[sphere] / procent
    return spheres, num_of_spheres, procent_of_sphere  
periods = periods_finding()
lenghts, more_than_100k, more_than_90k, more_than_80k, more_than = lenghts_finding()
spheres, num_of_spheres, procent_of_spheres = sphere_finding()

