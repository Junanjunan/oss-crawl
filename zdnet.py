import requests
from datetime import datetime, date
from bs4 import BeautifulSoup


date_format = '%Y.%m.%d'

check_day = 1

url_opensource = 'https://search.zdnet.co.kr/?kwd=%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4&area=1&term='
url_platform = 'https://search.zdnet.co.kr/?kwd=%ED%94%8C%EB%9E%AB%ED%8F%BC&area=1&term='
url_sw = 'https://search.zdnet.co.kr/?kwd=sw&area=1&term='
url_gpu = 'https://search.zdnet.co.kr/?kwd=gpu&area=1&term='
url_ai = 'https://search.zdnet.co.kr/?kwd=ai&area=1&term='
url_data = 'https://search.zdnet.co.kr/?kwd=%EB%8D%B0%EC%9D%B4%ED%84%B0&area=1&term='
url_network = 'https://search.zdnet.co.kr/?kwd=%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC&area=1&term='
url_linux = 'https://search.zdnet.co.kr/?kwd=%EB%A6%AC%EB%88%85%EC%8A%A4&area=1&term='

url_list = [
    url_opensource,
    url_platform,
    url_sw,
    url_gpu,
    url_ai,
    url_data,
    url_network,
    url_linux,
    ]


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

f = open(f"zdnet_{date.today()}.txt", "w", encoding='utf-8')

for url in url_list:

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "lxml")

    assetText_list = soup.find_all("div", attrs={"class":"assetText"})

    for assetText in assetText_list:
        mark = assetText.find("mark")
        
        if mark is None:
            continue
        
        try:
            date = assetText.find("p", attrs={"class":"byline"}).find("span").text
            today = datetime.now()
            news_date_str = date.split(" ")[0]
            news_date = datetime.strptime(news_date_str, date_format)
            period = (today - news_date).days
            if period == check_day:            
                link = assetText.find("a")["href"]
                title = assetText.find("h3").text
                f.write(f'{link}\n')
                f.write(f'{title}\n')
                f.write('\n')
        except:
            pass
f.close()