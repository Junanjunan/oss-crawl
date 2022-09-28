import requests
from datetime import datetime, date
from bs4 import BeautifulSoup


date_format = '%Y.%m.%d'

check_day = 1

url_opensource = 'https://www.ciokorea.com/search/index.php?page=1&ui_status=hide&q=%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4&month_limit=&sort=desc&property='
url_platform = 'https://www.ciokorea.com/search/index.php?page=1&ui_status=hide&q=%ED%94%8C%EB%9E%AB%ED%8F%BC&month_limit=&sort=desc&property='
url_sw = 'https://www.ciokorea.com/search/index.php?page=1&ui_status=hide&q=sw&month_limit=&sort=desc&property='
url_gpu = 'https://www.ciokorea.com/search/index.php?page=1&ui_status=hide&q=gpu&month_limit=&sort=desc&property='
url_ai = 'https://www.ciokorea.com/search/index.php?page=1&ui_status=hide&q=AI&month_limit=&sort=desc&property='
url_data = 'https://www.ciokorea.com/search/index.php?page=1&ui_status=hide&q=%EB%8D%B0%EC%9D%B4%ED%83%80&month_limit=&sort=desc&property='
url_network = 'https://www.ciokorea.com/search/index.php?page=1&ui_status=hide&q=%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC&month_limit=&sort=desc&property='
url_linux = 'https://www.ciokorea.com/search/index.php?page=1&ui_status=hide&q=%EB%A6%AC%EB%88%85%EC%8A%A4&month_limit=&sort=desc&property='

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

f = open(f"cio_{date.today()}.txt", "w", encoding='utf-8')

for url in url_list:

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "lxml")

    # card_body_list = soup.find_all("div", attrs={"class":"card-body"})
    row_list = soup.find_all("div", attrs={"class":"d-lg-flex"})

    for row in row_list:
        keyword = row.find("h4", attrs={"class":"card-title"}).find("span", attrs={"class":"font-color-primary-1"})
        if keyword is None:
            continue
        
        try:
            date = row.find("small", attrs={"class":"font-lato"}).text
            today = datetime.now()
            news_date_str = date.split(" ")[1]
            news_date = datetime.strptime(news_date_str, date_format)
            period = (today - news_date).days
            if period == check_day:            
                title = row.find("h4", attrs={"class":"card-title"}).find("a").text
                link = row.find("h4", attrs={"class":"card-title"}).find("a")["href"]
                full_link = f'https://www.ciokorea.com{link}'
                f.write(f'{full_link}\n')
                f.write(f'{title}\n')
                f.write('\n')
        except:
            pass

f.close()