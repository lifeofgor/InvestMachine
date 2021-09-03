from django.shortcuts import render
from .models import ModelsNewsPage
from django.views.generic import DetailView
from bs4 import BeautifulSoup
import requests


HOST = 'https://quote.rbc.ru/'
URL = 'https://quote.rbc.ru/?utm_source=topline'
HEADERS = {
    'accept' : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'user-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203"
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_new_url(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="q-item__wrap l-col-center-590")
    cards = []
    for el in items:
        cards.append(el)
    return cards

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="l-col-center-590 article__content")
    cards = []
    for el in items:
        full = []
        cout = 0
        elemenFull = el.find('div', class_="article__text article__text_free").find_all('p')
        for elem in elemenFull:
            if cout != 4:
                full.append(elem.get_text(strip=True))
                cout += 1
            else:
                continue
        try:
            cards.append(
                {
                    'title': el.find('div', class_="article__header__title").get_text(strip=True),
                    'preview': el.find('div', class_="article__text__overview" ).find('span').get_text(strip=True),
                    'full_text': ''.join(full),
                    'data': el.find('span', class_="article__header__date").get_text(strip=True),
                    'img': el.find('div', class_="article__main-image__wrap").find('img').get('src')
                }
            )
        except AttributeError:
            break
    return cards

def get_info(URL,mas_url):
    new_urls = []
    for el in mas_url:
        new_url = el.find('a', class_="q-item__link").get('href')
        new_urls.append(new_url)
    res = []
    for i in range(len(new_urls)):
        URL = new_urls[i]
        html = get_html(URL)
        res.extend(get_content(html.text))
    return res


def AboutOurCompany(request):
    return render(request, 'main/aboutPage.html')

def NewsPage(request):
    news = ModelsNewsPage.objects.order_by('-data')
    return render(request, 'main/NewsPage.html', {'news': news})

class NewsDetailView(DetailView):
    model = ModelsNewsPage
    template_name = 'main/details.html'
    context_object_name = 'article'


def save_in_bd(result_pars):
    for i in range(len(result_pars)):
        bb = ModelsNewsPage(title=result_pars[i]['title'], preview=result_pars[i]['preview'],
                                      full_text=result_pars[i]['full_text'], img=result_pars[i]['img'])
        bb.save()

html = get_html(URL)
mas_url = get_new_url(html.text)
result_pars = get_info(URL, mas_url)
save_in_bd(result_pars)

