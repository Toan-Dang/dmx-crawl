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
import time


DRIVER_PATH = 'chromedriver.exe'
# custom browser
chrome_options = Options()
chrome_options.add_argument("--incognito")
# open chrome
print('[crawl-fri]: open browser')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, executable_path=DRIVER_PATH)
url = "https://www.dienmayxanh.com/tu-lanh#c=1943&o=9&pi=11"


def botFri():

    driver.get(url)
    time.sleep(30)

    try:
        print('[crawl-fri]: start')
        print('[crawl-fri]: start load all product')
        listProduct = driver.find_elements(By.CLASS_NAME, 'main-contain')
        print('[crawl-fri]: all product: ', len(listProduct))
        for item in listProduct:
            productName = item.find_element(By.TAG_NAME, 'h3').text
            try:
                price = item.find_element(By.CLASS_NAME, 'price').text
            except:
                price = '0'
            try:
                percent = item.find_element(By.CLASS_NAME, 'percent').text
            except:
                percent = '0'
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
                price), result.getPercent(percent), ratings, star, 'fridge', result.getPhoneCategory(productName))
            print('[crawl-fri]: Done on: ', productName)

        print('[crawl-fri]: end')
        driver.quit()
    except Exception as error:
        print('[crawl-fri]: ERROR ', error)
        # close browser window
        driver.quit()

# botPhone()
