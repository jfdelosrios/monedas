from banrep import USD_COP
from btcTo import BTC_to
import locale
import pandas as pd
import time
from os import system


def ciclo():

    pares=[
        USD_COP(),
        BTC_to('usd'),
        BTC_to('cop')
        ]
   
    df = pd.DataFrame([i['value'] for i in pares])

    df['Status']=[i['Status'][0] for i in pares]

    df['Value']=df['Value'].apply(lambda x: locale.format_string('%.2f', x, grouping=True))
    pd.options.display.max_rows=df.shape[1]

    system('cls') 

    print(*(i['Status'][1] for i in pares if(i['Status'][1] != '')), sep='\n')
    print('')

    print(df)
    
    time.sleep(60)

    ciclo()


if __name__=='__main__':

    locale.setlocale(locale.LC_ALL, 'es_co')

    print('Cargando...')
    ciclo()