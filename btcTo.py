from scrapy import Selector
import requests
from requests.exceptions import ConnectionError


def BTC_to(monedaCotizada):
    link = 'https://www.google.com/search?q=btc+to+'+monedaCotizada

    try:
        html = requests.get(
            link,
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
                }
            )
    except ConnectionError as error:
        return {'value': {'Symbol':'BTC'+monedaCotizada.upper(), 'Value':-1}, 'Status':['Falló',error]}

    sel = Selector( text = html.content )
    list_precio=sel.xpath(
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]/text()'
        ).extract()

    if(len(list_precio)==0):
        return {
            'value': {'Symbol':'BTC'+monedaCotizada.upper(), 'Value':-1}, 
            'Status':['Falló','len(list_precio)==0 de '+link]
            }

    return {
        'value': {'Symbol':'BTC'+monedaCotizada.upper(), 'Value': float(list_precio[0].replace(',',''))}, 
        'Status':['ok','']
        }