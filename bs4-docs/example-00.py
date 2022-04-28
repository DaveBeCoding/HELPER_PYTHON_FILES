from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')


print('----------TITLE-----------------')
print(soup.title)

print('\n')
print('------------TITLE-NAME---------------')
print(soup.title.name)

print('\n')
print('-----------TITLE-STRING----------------')
print(soup.title.string)

print('\n')
print('-------------PARENT-NAME--------------')
print(soup.title.parent.name)

print('\n')
print('-------------<P>--------------')
print(soup.p)
print(soup.p.string)


print('\n')
print('------------p[class]---------------')
print(soup.p['class'])

print('\n')
print('--------------<a>-------------')
print(soup.a)


print('\n')
print('------------find_all(a)---------------')
print(soup.find_all('a'))

print('\n')
print('------------find(id=link3)---------------')
print(soup.find(id="link3"))
print(soup.find(id="link3").string)


print('\n')
print('------------find_all a-tags---------------')
for link in soup.find_all('a'):
    print(link.string)
    print(link.get('href'))
    print('\n')




# print(soup.prettify())
