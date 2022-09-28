import requests
from datetime import datetime, date
from bs4 import BeautifulSoup


date_format = '%Y.%m.%d'

check_day = 1

url_opensource = 'https://www.itworld.co.kr/search/?q=%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4'
url_platform = 'https://www.itworld.co.kr/search/?q=%ED%94%8C%EB%9E%AB%ED%8F%BC'
url_sw = 'https://www.itworld.co.kr/search/?q=sw'
url_gpu = 'https://www.itworld.co.kr/search/?q=gpu'
url_ai = 'https://www.itworld.co.kr/search/?q=ai'
url_data = 'https://www.itworld.co.kr/search/?q=%EB%8D%B0%EC%9D%B4%ED%83%80'
url_network = 'https://www.itworld.co.kr/search/?q=%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC'
url_linux = 'https://www.itworld.co.kr/search/?q=%EB%A6%AC%EB%88%85%EC%8A%A4'

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

f = open(f"itworld_{date.today()}.txt", "w", encoding='utf-8')

for url in url_list:

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "lxml")

    card_body_list = soup.find_all("div", attrs={"class":"card-body"})

    for card_body in card_body_list:
        print(card_body)
        keyword = card_body.find("h5", attrs={"class":"card-title"}).find("span", attrs={"class":"font-color-primary-1"})
        print(keyword)
        print("-----")
        if keyword is None:
            continue
        
        try:
            date = card_body.find("small", attrs={"class":"font-lato"}).text
            today = datetime.now()
            news_date_str = date.split(" ")[1]
            news_date = datetime.strptime(news_date_str, date_format)
            period = (today - news_date).days
            if period == check_day:            
                title = card_body.find("h5", attrs={"class":"card-title"}).find("a").text
                link = card_body.find("h5", attrs={"class":"card-title"}).find("a")["href"]
                full_link = f'https://www.itworld.co.kr{link}'
                f.write(f'{full_link}\n')
                f.write(f'{title}\n')
                f.write('\n')
        except:
            pass

f.close()