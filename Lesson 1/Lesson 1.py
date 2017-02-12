import requests

with open('google.html', 'w') as d:
    r = requests.get('http://www.google.com')
    for i in r.text:
        d.write(i)