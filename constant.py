import module.botPhone as phone
import module.botLapTop as lap
import module.botTV as tv
import module.botFreze as fri
import module.botAir as air
import module.botWash as wash

productNameList = []
priceList = []
percentList = []
ratingList = []
starList = []
typeList = []
categoryList = []

def addResult(productName, price, percent, rating, star, type, category):
    productNameList.append(productName)
    priceList.append(price)
    percentList.append(percent)
    ratingList.append(rating)
    starList.append(star)
    typeList.append(type)
    categoryList.append(category)

def getPrice(price):
    if(len(price)>2):
        p = price[:-1] 
        return p.replace('.', '')
    return price

def getPhoneCategory(name):
    return name.split()[0]


def runPhone():
    phone.botPhone()
    print('[crawl-bot] phone thread: end')


def runLaptop():
    lap.botLaptop()
    print('[crawl-bot] laptop thread: end')


def runTV():
    tv.botTV()
    print('[crawl-bot] tivi thread: end')


def runFri():
    fri.botFri()
    print('[crawl-bot] fri thread: end')


def runAir():
    air.botAir()
    print('[crawl-bot] air thread: end')


def runWash():
    wash.botWash()
    print('[crawl-bot] wash thread: end')