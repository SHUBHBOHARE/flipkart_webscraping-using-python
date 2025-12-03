import requests
from bs4 import BeautifulSoup
import pandas as pd
product_name =[]
prices=[]
rating=[]
description =[]
headers=({'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'})
for i in range(2,8):
  r= requests.get("https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i),headers=headers)
#print(r.text)
  soup= BeautifulSoup(r.text,"html.parser")
  np=soup.find("a",class_ = "jgg0SZ").get("href")
 #print(np)
  cnp ="https://www.flipkart.com"+ np
  print(cnp)

#names= soup.find_all("div",{"class" : "RG5Slk"})
#print(names)

#for i in names:
 #   name =i.text
  #  product_name.append(name)
    
#print(product_name)

#prices =  soup.find_all("div",{"class" : "hZ3P6w DeU9vF"}) 
#print(prices)

#for i in prices:
 #   name = i.text
  #  prices.append(name)
    
#print(prices)

#desc =soup.find_all("ul",class_="HwRTzP")
#for i in desc:
 #   name= i.text
  #  description.append(name)
    
#print(description)
  box= soup.find("div",class_ = "QSCKDh dLgFEE")
    
  names = box.find_all("div", {"class": "RG5Slk"})
  for i in names:
    product_name.append(i.text)

#print(product_name)   


  prices_list = box.find_all("div", {"class": "hZ3P6w DeU9vF"})
  for i in prices_list:
    prices.append(i.text)

#print(prices)        


  desc_list = box.find_all("ul", class_="HwRTzP")
  for i in desc_list:
    description.append(i.text)

#print(description)   
  

  ratings= box.find_all("div",class_="MKiFS6")

  for i in ratings:
    name= i.text
    rating.append(name)

#rint(rating)

df= pd.DataFrame({"prodouct name" : product_name,"prices" : prices,"description" : description,"rating" : rating})
print(df)

df.to_csv("C:/Users/shubh/OneDrive/Desktop/flipkart_webscraping.csv")
