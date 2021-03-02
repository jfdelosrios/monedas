from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import os.path

def USD_COP():

    if(not os.path.isfile('chromedriver.exe')):
        return {'Symbol':'USDCOP', 'Value':-1, 'Status':['Falló']}

    link='https://totoro.banrep.gov.co/analytics/saw.dll?Go&Path=%2fshared%2fWebBanco%2fES%2fTasa%20Representativa%20del%20Mercado%2flogin&NQUser=publico&NQPassword=publico123'

    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)

    try:
        driver.get(link) 
        el = WebDriverWait(driver,100).until(lambda d: d.find_element_by_xpath('//*[@id="o:go~r:report~v:compoundView!1~v:narrativeView!1ViewContainer"]/div/b/span'))
    except:
        driver.close()
        return {'Symbol':'USDCOP', 'Value':-1, 'Status':['Falló']}

    el=float(el.text.replace('.','').replace(',','.'))
        
    driver.close()

    return {'Symbol':'USDCOP', 'Value':el, 'Status':['ok']}