from bs4 import  BeautifulSoup
import requests
import csv
import  pandas as pd

#getting the html


webpage = requests.get("https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off").text

#converting it into a parsable object
source = BeautifulSoup(webpage,"lxml")

# print(source.prettify())

containers = source.find_all("div",class_="_1-2Iqu row")

# print(BeautifulSoup.prettify(box_main[0]))
container = containers[0]

#To Collect Names
names = []
name_list =[]
names = source.find_all("div",class_="_3wU53n")

for i in range(len(names)):
    name = str(names[i]).split(")")
    name = str(name[0])
    name = str(name).split(">")
    name = str(name[1])
    name = str(name)+")"
    name_list.append(name)
# print(name_list)

#For Collecting Prices
price_list = []
prices = source.find_all("div",class_="_1vC4OE _2rQ-NK")
price =[]
for i in range(len(prices)):
    price=str(prices[i]).split(">")
    price = str(price[1])
    price = price.split("<")
    price = price[0]
    price_list.append(price)

# print(price_list)


#to Collect Ratings

rating_list = []
ratings = source.find_all("div", class_="hGSR34")
for i in range(len(ratings)):
    if i< 24:
        rating =  str(ratings[i]).split(">")
        rating = rating[1]
        rating = rating.split("<")[0]
        rating_list.append(rating)
    else:
        break

# print(rating_list)

# print(len(name_list),len(price_list),len(rating_list))
pd.DataFrame({'Name':name_list,'Price':price_list,'Rating':rating_list}).to_csv('Iphone.csv')










