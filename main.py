from banrep import USD_COP
from btcTo import BTC_to
import locale
import pandas as pd
import time
from os import system
import os.path

def ciclo():

    global cont

    df = pd.DataFrame([
        USD_COP(),
        BTC_to('usd'),
        BTC_to('cop')
        ])

    df['value']=df['value'].apply(lambda x: locale.format_string('%.2f', x, grouping=True))

    system('cls') 

    #print(str(cont))
    cont=cont+1

    if(not os.path.isfile('chromedriver.exe')):
        print('Error. Descargue chromedriver.exe de http://chromedriver.chromium.org/downloads , peguelo en la carpeta del programa y reinicie el programa.')

    print('')

    print(df[['monedaBase','monedaCotizada','value','status']])
    
    time.sleep(50)

    ciclo()


if __name__=='__main__':

    locale.setlocale(locale.LC_ALL, 'es_co')

    cont=0

    print('Cargando...')
    ciclo()