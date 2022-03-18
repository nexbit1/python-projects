import requests
import os


API_KEY = os.environ.get('apikey')
long_url = input('PASTE YOUR URL: ')
# with open('long_url', mode='a') as data: expand doesnt work😠in pyshortners
#     data.write(long_url)
response = requests.get(url=f'http://cutt.ly/api/api.php?key={API_KEY}&short={long_url}').json()['url']
print(f'Your short URL: {response["shortLink"]}')

import pyshorteners

#chilpit
x = pyshorteners.Shortener()
y = x.chilpit.short('long_url')





