import sys, webbrowser, bs4, requests

print('Googling results for you...')

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

