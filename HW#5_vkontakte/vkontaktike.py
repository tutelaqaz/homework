# -*- coding: utf-8 -*-
# Python 2.7
import vkontakte
import datetime
import csv
import time as tm
from time import time
import ssl

def getting_users(com):
    table = 'User_id;first_name;last_name;sex;bdate;city;\n'
    city = 'Серпухов'
    for user in com[1:]:
        for attribute in user:
            if attribute == 'uid':
                user_id = user[attribute]
            if attribute == 'first_name':
                first_name = user[attribute]
                first_name = first_name.encode('utf-8')
            if attribute == 'last_name':
                last_name = user[attribute]
                last_name = last_name.encode('utf-8')
            if attribute == 'sex':
                if user[attribute] == 2:
                    sex = 'male'
                if user[attribute] == 1:
                    sex = 'female'
            if attribute == 'bdate':
                bdate = user[attribute]
        table += (str(user_id) + ';' + first_name + ';' + last_name + ';'
                  + sex + ';' + str(bdate) + ';' + city + ';\n')
        print('Done')
    return table
    
def saving_wall(uid, table):
    wall = vk.get('wall.get', owner_id = uid, count = 100, filter = 'owner')
    tm.sleep(.500)
    table = getting_wall(wall, table, uid)  
    return table
    
def getting_wall(wall, table, user_id):
    for posts in wall[1:]:
        text = ''
        for post in posts:
            if post == 'text':
                if posts[post] != '':
                    text = posts[post]
                    text = text.encode('utf-8')
            if post == 'date':
                date = posts[post]
                date = datetime.datetime.fromtimestamp(
                        int(date)).strftime('%d-%m-%Y %H:%M:%S')
        if text != '':
            table += (str(user_id) + ';' + str(date) + ';' + text + ';\n')
    return table
            
start = time()               
vk = vkontakte.API(token = input('Write your access token:')) #input your access token
com = vk.get('users.search', count = 1000, fields = 'sex, bdate, lang, city', city = 340)
table = getting_users(com)
f = open('Users_table.csv', 'w')
f.write(table)
f.close()

x = 0
uids = []
with open('Users_table.csv', 'r') as f:
    inputf = csv.reader(f, delimiter = ';')
    for row in inputf:
        if x != 0:
            uids.append(row[0])
        x += 1
wall = []

x = 0
for uid in uids:
    table = 'user_id;date;text;\n'
    try:
        table = saving_wall(uid, table)
        print(x)
        x += 1
    except ssl.SSLError:
        table = saving_wall(uid, table)
        print(x)
        x += 1
    f = open('Users_posts\user_posts_' + str(x) + '.txt', 'w')
    f.write(table)
    f.close()

print 'Evaluation time: {}'.format((time()-start))
