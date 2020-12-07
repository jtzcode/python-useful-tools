import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
#print(res.text[:250])
res.raise_for_status()
bookFile = open('罗密欧与朱丽叶.txt', 'wb')
for chunk in res.iter_content(100000):
    bookFile.write(chunk)
bookFile.close()