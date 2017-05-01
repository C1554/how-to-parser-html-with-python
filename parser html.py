
#coding:utf8
# Beautiful Soup
#python 第三方库，用于从HTML或XML中提取数据
#官网：https://www.crummy.com/software/BeautifulSoup/
#安装并测试beautifulsoup4
#安装：pip install beautifulsoup4
#测试：import bs4
import re
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#based on html webpage string create BeautifulSoup object  html_doc(html document string)  'html.parser'(html parser)
soup=BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

print '获取所有的链接'
#find all 'a' label node
links=soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()

print '获取lacie的链接'
#find 'a' label node , but link comform to "http://XXXXX" form node
link_node=soup.find('a',href="http://example.com/lacie")
print link_node.name,link_node['href'],link_node.get_text()

print '正则匹配'
link_node=soup.find('a',href=re.compile(r"ill"))
print link_node.name,link_node['href'],link_node.get_text()


print '获取p段落文字'
#find all 'p' label and class is "title" and character is python's node
p_node=soup.find('p',class_="title")
print p_node.name,p_node.get_text()




