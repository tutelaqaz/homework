import urllib.request
import re
import lxml.html
import os
import json


urls = [] # найденные ссылки
urlsdone = [] # обкаченные ссылки
x = 1 # links counter
dirsmade = [] # созданные директории

url = 'http://www.inmozhaisk.ru'
table = 'path;author;sex;birthday;header;created;sphere;genre_fi;type;topic;chronotop;style;audience_age;audience_level;audience_size;source;publication;publisher;publ_year;medium;country;region;language;\n'
con = urllib.request.urlopen(url)
page = con.read()
page = page.decode()
print(con.getcode())

mainPage = open('Html/main page.txt','w',encoding = 'utf-8')
mainPage.write(page)
mainPage.close()

tree = lxml.html.fromstring(page)
links = tree.xpath('.//a/@href')
for link in links:
    m = re.search('(http:)|(mailto)|(.jpg)|(.pdf)|(.gif)|(.docx?)|(.html)|(bitrix)', link)
    if m == None:
        m = re.search('^(\/\\S+(\/)?)$', link)
        if m != None:
            url2 = 'http://www.inmozhaisk.ru'+ link
            if url2 not in urlsdone:
                urlsdone.append(url2)
                con = urllib.request.urlopen(url2)
                page = con.read()
                page = page.decode()
                y = str(x)
                htmlpage = open('Html/' + y + '.txt','w',encoding = 'utf-8')
                x += 1
                htmlpage.write(page)
                htmlpage.close()
                tree = lxml.html.fromstring(page)
                links += tree.xpath('.//a/@href')
                title = tree.xpath('.//h1[@class="pagetitle"]/text()')
                date = tree.xpath('.//div[@class="news-one"]/div[@class="date"]/text()')
                text = tree.xpath('.//div[@class="text"]/p/text()')
                title = '\n'.join(title)
                text = '\n'.join(text)
                if date!= []:
                    m = re.search('(\\d){2}\.(\\d{2})\.(\\d{4})', date[0])
                    if m != None:
                        path = str('articles/' + m.group(3)+'/' + m.group(2))
                        if path not in dirsmade:
                            dirsmade.append(path)
                            os.makedirs(path)
                        article = open(path +'/' + y + '.txt','w', encoding = 'utf-8')
                        file = '@au Noname' + '\n' + '@ti ' + title + '\n' + '@da ' + m.group(0) + '\n' +'@url ' + url2 + '\n' + text
                        article.write(file)
                        article.close()
                        tablecsv = open('table.csv','w',encoding = 'utf-8')
                        table += (path + ';' + 'Noname;' + ' ; ;' + title +';' + str(m.group(0)) + ';'+ 'публицистика; ; ; ; ;нейтральный;н-возраст;н-уровень;районная;'+ url2
                          +';Новая жизнь; ;' + m.group(3) +';газета;Россия; Центральный;ru;'+ '\n')
                        tablecsv.write(table)
                        tablecsv.close()
                        path2 = str('analizedtxt/' + path)
                        path3 = str('analizedxml/' + path)
                        if path2 not in dirsmade:
                            dirsmade.append(path2)
                            os.makedirs(path2)
                        if path3 not in dirsmade:
                            dirsmade.append(path3)
                            os.makedirs(path3)
                        article2 = open(path +'/new' + y + '.txt','w', encoding = 'utf-8')
                        article2.write(text)
                        article2.close()
                        command = str('./mystem -icd' + ' ' + path +'/new' + y + '.txt'+ ' '+ path2 +'/' + y + '.txt')
                        command2 = str('./mystem -icd --format' + ' ' + 'xml' + ' ' + path +'/new' + y + '.txt'+ ' '+ path3 +'/' + y + '.xml')
                        os.system(command)
                        os.system(command2)
                        os.remove(path +'/new' + y + '.txt')
                        
        
print('The end')

