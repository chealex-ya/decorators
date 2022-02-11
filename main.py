import requests
import bs4

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

HEADERS = {
'Cookie': '_ym_uid=1633840118649521693; _ym_d=1633840118; _ga=GA1.2.1207969728.1633840118; hl=ru; fl=ru; __gads=ID=fbde59705326758d-22c7b662f1ca00fa:T=1633840121:S=ALNI_MahfEzLPxwp9azFqBMQmFuThoPnhw; _fbp=fb.1.1639551335100.1227118989; habr_web_home=ARTICLES_LIST_ALL; visited_articles=588661:599791; _gid=GA1.2.1513276948.1644437506; _ym_isad=2',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 YaBrowser/22.1.0.2500 Yowser/2.5 Safari/537.36'
}

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    words = set(article.text.split())
    if KEYWORDS & words:
        date_tag = article.find('span', class_="tm-article-snippet__datetime-published")
        date = date_tag.time.attrs['title']
        title = article.find('h2')
        a_tag = title.find('a')
        href = a_tag.attrs['href']
        url = 'https://habr.com' + href
        print(date)
        print(title.text)
        print(url)
        print(words)
        print('-------')


