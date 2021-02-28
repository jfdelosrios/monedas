from scrapy import Selector
import requests


def BTC_to(monedaCotizada):
    link = 'https://www.google.com/search?q=btc+to+'+monedaCotizada

    try:
        html = requests.get(
            link,
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
            )
    except:
        return {'status':['falló'], 'value': -1, 'monedaBase':'BTC', 'monedaCotizada': monedaCotizada.upper()}

    sel = Selector( text = html.content )
    list_precio=sel.xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]/text()').extract()

    if(len(list_precio)==0):
        return {'status':['no cargó'], 'value': -1, 'monedaBase':'BTC', 'monedaCotizada': monedaCotizada.upper()}

    return {'status':['ok'], 'value': float(list_precio[0].replace(',','')), 'monedaBase':'BTC', 'monedaCotizada': monedaCotizada.upper()}