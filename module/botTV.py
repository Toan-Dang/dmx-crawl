###########
# @author ToanDang-19522357
##########

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import constant as result
import time


DRIVER_PATH = 'chromedriver.exe'
# custom browser
chrome_options = Options()
chrome_options.add_argument("--incognito")
# open chrome
print('[crawl-tv]: open browser')
driver = webdriver.Chrome( options=chrome_options, executable_path=DRIVER_PATH)
url = "https://www.dienmayxanh.com/tivi#c=1942&o=9&pi=15"


def botTV():
    driver.get(url)
    time.sleep(30)

    try:
        print('[crawl-TV]: start')
        print('[crawl-TV]: start load all product')
        listProduct = driver.find_elements(By.CLASS_NAME, 'main-contain')
        #name = [pro.text for pro in listProductName]
        print('[crawl-TV]: all product: ', len(listProduct))
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

            result.addResult(productName, result.getPrice(price), 
                             result.getPercent(percent), ratings, star, 'Tivi', result.getPhoneCategory(productName))
            print('[crawl-TV]: Done on: ', productName)

        print('[crawl-TV]: end')
        driver.quit()
    except Exception as error:
        print('[crawl-TV]: ERROR ', error)
        # close browser window
        driver.quit()

#botTV()
