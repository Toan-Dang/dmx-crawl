###########
# @author ToanDang-19522357
##########
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import constant as result



DRIVER_PATH = 'chromedriver.exe'
url = "https://www.dienmayxanh.com/dien-thoai#c=42&o=9&pi=6"
# custom browser
chrome_options = Options()
chrome_options.add_argument("--incognito")
# open chrome
print('[crawl-phone]: open browser')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, executable_path=DRIVER_PATH)

def botPhone():
    driver.get(url)
    try:
        print('[crawl-phone]: start')
        print('[crawl-phone]: start load all product')
        listProduct = driver.find_elements(By.CLASS_NAME, 'main-contain')
        #name = [pro.text for pro in listProductName]
        print('[crawl-phone]: all product: ', len(listProduct))
        for item in listProduct:
            productName = item.find_element(By.TAG_NAME, 'h3').text
            try:
                price = item.find_element(By.CLASS_NAME, 'price').text
            except:
                price = '0'
            try:
                percent = item.find_element(By.CLASS_NAME, 'percent').text
            except:
                percent = '0%'
            try:
                ratings = item.find_element(By.CLASS_NAME, 'item-rating-total').text
            except:
                ratings = 0
            try:
                star = len(item.find_elements(By.CLASS_NAME, 'icon-star'))
            except:
                star = 0

            result.addResult(productName, result.getPrice(price), percent, ratings, star,'phone',result.getPhoneCategory(productName))
            print('[crawl-phone]: Done on: ', productName)

        print('[crawl-phone]: end')
        driver.quit()
    except Exception as error:
        print('[crawl-phone]: ERROR ', error)
        # close browser window
        driver.quit()

#botPhone()