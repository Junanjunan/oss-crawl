import requests
from bs4 import BeautifulSoup


# 지디넷 코리아(키워드 검색: 오픈소스 / 제목만) :
url = 'https://search.zdnet.co.kr/?kwd=%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4&area=1&term='

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "lxml")
print(soup.a)