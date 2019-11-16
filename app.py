import requests
from url_parser import UrlParser

url = 'http://www.ffmpeg.org/releases/'
res = requests.get(url)
res.raise_for_status()
html = res.text
parser = UrlParser()
result = parser.parse(html)
print(result)
