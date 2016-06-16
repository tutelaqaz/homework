# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 12:39:49 2016

@author: tutela
"""

import pymysql
import csv

x = 0
users_name = {}
users_sex = {}
users_bdate = {}
with open('Users_table.csv', 'r', encoding = 'utf-8') as file:
    inputfile = csv.reader(file, delimiter = ';')
    for row in inputfile:
        if x != 0:
           user_id = row[0]
           users_name[user_id] = row[1], row[2]
           users_sex[user_id] = row[3]
           users_bdate[user_id] = row[4]
        x += 1

		
password = input('Input the password:')
conn = pymysql.connect(host = 'localhost', user = 'guest1', passwd = password, db = 'guest1_MalashinaAV', charset = 'utf8')

cur = conn.cursor()
cur.execute('CREATE TABLE users_name (user_id INT(10), first_name VARCHAR(100), ' +
            'last_name VARCHAR(200), PRIMARY KEY (user_id)) DEFAULT CHARSET = utf8;')

for user in users_name:
    user_id = user
    name = users_name[user]
    first_name = name[0]
    last_name = name[1]

    cur.execute('INSERT INTO users_name (user_id, first_name, last_name)VALUES (' + str(user_id) + ', \'' + str(first_name) + 
                '\', \'' + str(last_name) + '\');')
cur.execute('CREATE TABLE users_sex (user_id INT(10), sex VARCHAR(10), ' +
            'PRIMARY KEY (user_id), FOREIGN KEY(user_id) REFERENCES ' +
            'users_name(user_id)) DEFAULT CHARSET = utf8;')

for user in users_sex:
    user_id = user
    sex = users_sex[user]

    cur.execute('INSERT INTO users_sex (user_id, sex)VALUES (' + str(user_id) + ', \'' + str(sex) + '\');')

cur.execute('CREATE TABLE users_bdate (user_id INT(10), bdate VARCHAR(20), ' +
            'PRIMARY KEY(user_id), FOREIGN KEY(user_id) REFERENCES ' +
            'users_name(user_id)) DEFAULT CHARSET = utf8;')

for user in users_bdate:
    user_id = user
    bdate = users_bdate[user]
    cur.execute('INSERT INTO users_bdate (user_id, bdate)VALUES (' + str(user_id) + ', \'' + str(bdate) + '\');')

print(cur.description)
cur.close()
conn.close()
