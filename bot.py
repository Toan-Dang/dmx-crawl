###########
# @author ToanDang-19522357
##########

import pandas as pd
from threading import Thread
import constant as result
import time
def export_csv():
    print('[crawl-bot]: export product to csv')
    df = pd.DataFrame({'productName': result.productNameList, 'type': result.typeList, 'category': result.categoryList, 
    'price': result.priceList, 'percent': result.percentList, 'rating': result.ratingList, 'star': result.starList})
    print('[crawl-bot]: data', df)
    df.to_csv('Product.csv', index=False)

def main():
    try:
        print('[crawl-bot]: start')
        t1 = Thread(target=result.runPhone, args=())
        t2 = Thread(target=result.runLaptop, args=())
        t3 = Thread(target=result.runTV, args=())
        t4 = Thread(target=result.runFri, args=())
        t5 = Thread(target=result.runAir, args=())
        t6 = Thread(target=result.runWash, args=())
        #start thread
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        #wait other thread
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        #export
        export_csv()

    except:
        print('[crawl-bot]: ERROR')



if __name__ == "__main__":
    main()
