import urllib.request
import re
import lxml.html

urls = [] # найденные ссылки
urlsdone = [] # обкаченные ссылки
urlsshit = [] # говняные ссылки
urlshit = ' '
archives = []
url = 'http://www.belrab.ru/archive/art.php?id_item=751&id_article=8108'
con = urllib.request.urlopen(url)
page = con.read()
page = page.decode('cp1251')
print(con.getcode())

mainPage = open('main page.txt','w',encoding = 'utf-8')
mainPage.write(page)
mainPage.close()

#articles = open('articles.txt','w',encoding = 'utf-8')
tree = lxml.html.fromstring(page)
title = tree.xpath('.//p/h3/@align="center"/text()')
data = tree.xpath('.//p/@class="ptext"/text()')
author = tree.xpath('.//p/@class="ptext"/text()')
text = tree.xpath('.//p/@class="txt2"/text()')

        
        
            
    

#text = tree.xpath('.//div[@class="sgray"]/text()')[0]
#author
#topic
#data
#print(text)
print(title, data, author, text)
mainPage.close()
print('The end')
