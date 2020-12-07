import requests, bs4

exampleHTML = open('example.html')
soup = bs4.BeautifulSoup(exampleHTML.read())
elements = soup.select('#author')
print(elements[0].getText())