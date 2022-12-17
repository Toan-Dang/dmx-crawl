###########
# @author ToanDang-19522357
##########

from threading import Thread
import constant as result
import DB as db
def main():
    try:
        print('[crawl-bot]: start')
        t1 = Thread(target=result.runPhone, args=())
        t2 = Thread(target=result.runLaptop, args=())
        t3 = Thread(target=result.runTV, args=())
        t4 = Thread(target=result.runFri, args=())
        t5 = Thread(target=result.runAir, args=())
        t6 = Thread(target=result.runWash, args=())
        t7 = Thread(target=result.runWater, args=())
        t8 = Thread(target=result.runSound, args=())
        #start thread
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        #wait other thread
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        #export
        result.export_csv()

    except Exception as error:
        print('[crawl-bot]: ERROR ', error)


if __name__ == "__main__":
    main()
