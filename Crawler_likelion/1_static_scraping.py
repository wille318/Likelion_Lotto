import requests
from bs4 import BeautifulSoup as bs 

URL="http://naver.com"
res = requests.get(URL)

print(res)