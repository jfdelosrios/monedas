from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException, TimeoutException


def USD_COP():

    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    option.add_argument('--headless')
    
    try:
        driver = webdriver.Chrome(options=option)
    except SessionNotCreatedException as error:
        return {'value': {'Symbol':'USDCOP', 'Value':-1}, 'Status': ['Falló',error]}    
    except WebDriverException as error:
        return {'value': {'Symbol':'USDCOP', 'Value':-1}, 'Status': ['Falló',error]}

    try:
        driver.get(
            'https://totoro.banrep.gov.co/analytics/saw.dll?Go&Path=%2fshared%2fWebBanco%2fES%2fTasa%20Representativa%20del%20Mercado%2flogin&NQUser=publico&NQPassword=publico123'
        ) 
    except WebDriverException as error:
        driver.close()
        return {'value': {'Symbol':'USDCOP', 'Value':-1}, 'Status': ['Falló',error]}
       
    try:
        el = WebDriverWait(driver,10).until(lambda d: d.find_element_by_xpath(
            '//*[@id="o:go~r:report~v:compoundView!1~v:narrativeView!1ViewContainer"]/div/b/span'
            ))
    except TimeoutException as error:
        driver.close()
        return {'value': {'Symbol':'USDCOP', 'Value':-1}, 'Status': ['Falló',str(error)+' TimeoutException']}    
  
    el=float(el.text.replace('.','').replace(',','.'))
        
    driver.close()

    return {'value': {'Symbol':'USDCOP', 'Value':el}, 'Status':['ok', '']}