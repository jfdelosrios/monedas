from banrep import USD_COP
from btcTo import BTC_to
import locale
import pandas as pd
import time
from os import system
import os.path


def ciclo():

    df = pd.DataFrame([
        USD_COP(),
        BTC_to('usd'),
        BTC_to('cop')
        ])

    df['Value']=df['Value'].apply(lambda x: locale.format_string('%.2f', x, grouping=True))
    pd.options.display.max_rows=df.shape[1]

    system('cls') 

    if(not os.path.isfile('chromedriver.exe')):
        print('Error. Descargue chromedriver.exe de http://chromedriver.chromium.org/downloads , peguelo en la carpeta del programa y reinicie el programa.')

        print('')

    print(df)
    
    time.sleep(50)

    ciclo()


if __name__=='__main__':

    locale.setlocale(locale.LC_ALL, 'es_co')

    print('Cargando...')
    ciclo()