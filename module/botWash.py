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
# custom browser
chrome_options = Options()
chrome_options.add_argument("--incognito")
# open chrome
print('[crawl-wash]: open browser')
driver = webdriver.Chrome(service=Service(ChromeDriverManager(
).install()), options=chrome_options, executable_path=DRIVER_PATH)
url = "https://www.dienmayxanh.com/may-giat#c=1944&o=9&pi=11"


def botWash():
    driver.get(url)
    try:
        print('[crawl-wash]: start')
        print('[crawl-wash]: start load all product')
        listProduct = driver.find_elements(By.CLASS_NAME, 'main-contain')
        print('[crawl-wash]: all product: ', len(listProduct))
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
                ratings = item.find_element(
                    By.CLASS_NAME, 'item-rating-total').text
            except:
                ratings = 0
            try:
                star = len(item.find_elements(By.CLASS_NAME, 'icon-star'))
            except:
                star = 0

            result.addResult(productName, result.getPrice(
                price), percent, ratings, star, 'washing machine', result.getPhoneCategory(productName))
            print('[crawl-wash]: Done on: ', productName)

        print('[crawl-wash]: end')
        driver.quit()
    except Exception as error:
        print('[crawl-wash]: ERROR ', error)
        # close browser window
        driver.quit()


