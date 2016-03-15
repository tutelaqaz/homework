import urllib.request
import re
import lxml.html

urls = [] # найденные ссылки
urlsdone = [] # обкаченные ссылки
urlsshit = [] # говняные ссылки
urlshit = ' '
archives = [] 
url = 'http://www.belrab.ru/news/index.php'
con = urllib.request.urlopen(url)
page = con.read()
page = page.decode('cp1251')
print(con.getcode())

mainPage = open('main page.txt','w',encoding = 'utf-8')
mainPage.write(page)
mainPage.close()

#articles = open('articles.txt','w',encoding = 'utf-8')
tree = lxml.html.fromstring(page)
links = tree.xpath('.//a/@href')
for link in links:
    m = re.search('(http:)|(mailto)', link)
    if m == None:
        m = re.search('(\.\.)(\/\\S*)', link)
        if m != None:
            url2 = 'http://www.belrab.ru'+ m.group(2)
            m = re.search('(.jpg)$|(.JPG)$', url2)
            if m == None:
                if url2 not in urlsdone:
                    urlsdone.append(url2)
                    print(url2)
                    con = urllib.request.urlopen(url2)
                    page = con.read()
                    page = page.decode('cp1251')
                    tree = lxml.html.fromstring(page)
                    links +=(tree.xpath('.//a/@href'))
        else:
            m = re.search('(winner)|(news)', link)
            if m == None:
                url2 = 'http://www.belrab.ru/articles/'+ link
                m = re.search('(.jpg)$', url2)
                if m == None:
                    if url2 not in urlsdone:
                        urlsdone.append(url2)
                        print(url2)
                        con = urllib.request.urlopen(url2)
                        page = con.read()
                        page = page.decode('cp1251')
                        tree = lxml.html.fromstring(page)
                        links +=(tree.xpath('.//a/@href'))
            else:
                urlsshit.append(link)
                m = re.search('news', link)
                if m != None:
                    url2 = 'http://www.belrab.ru/archive/'+ link
                    if url2 not in urlsdone:
                        urlsdone.append(url2)
                        print(url2)
                        con = urllib.request.urlopen(url2)
                        page = con.read()
                        page = page.decode('cp1251')
                        tree = lxml.html.fromstring(page)
                        archives +=(tree.xpath('.//a/@href'))
                        for link in archives:
                            m = re.search('(http:)|(mailto)|(winner)', link)
                            if m == None:
                                url2 = 'http://www.belrab.ru/archive/'+ link
                                m = re.search('(.jpg)$|(.JPG)$', url2)
                                if m == None:
                                    if url2 not in urlsdone:
                                        urlsdone.append(url2)
                                        print(url2)
                                        con = urllib.request.urlopen(url2)
                                        page = con.read()
                                        page = page.decode('cp1251')
                                        tree = lxml.html.fromstring(page)
                                        archives +=(tree.xpath('.//a/@href'))
        
        
            
    

#text = tree.xpath('.//div[@class="sgray"]/text()')[0]
#author
#topic
#data
#print(text)
print(urlsshit)
mainPage.close()
print('The end')
