import urllib.request
import os
from bs4 import BeautifulSoup
link = input("Enter the Website Link that you wish to scrape from: ")
#Ebay Item Listings
if "ebay" in link:
    #Indicate to user that the program is running...
    print("\nLooking for items on E-bay...")
    #Request:
    req = urllib.request.urlopen(link)
    #String of Website HTML
    req_html = req.read()
    #Close Request
    req.close()
    #HTML Parser!
    req_soup = BeautifulSoup(req_html, 'html.parser')
    #Sales-event Page Specifically
    if "sales-events" in link:
        raw_items = req_soup.findAll("li", {"class":"s-item"})
    #Search Bar Link Pages Specifically
    elif "sch" in link:
        raw_items = req_soup.findAll("li", {"class":"s-item s-item--watch-at-corner"})
    #Get price/other info div that are found on both pages:
    price_list_html = req_soup.findAll("span", {"class":"s-item__price"})
    #Get shipping price
    shipping_price_html = req_soup.findAll("span", {"class":"s-item__shipping s-item__logisticsCost"})
    #Prepare CSV File
    csv_file = open("./Web-Scraping/shop.csv","w")
    headers = "Item Name, Item Link, Item Price, Shipping Price"
    csv_file.write(headers + "\n")
    #Write to CSV File.
    item_names = []
    item_links = []
    item_prices = []
    shipping_prices = []
    for item in raw_items:
        item_names.append(str(item.div.div.div.a.div.img["alt"]).replace(",",""))
        item_links.append(str(item.div.div.div.a["href"]).replace(",",""))
    for item in price_list_html:
        item_prices.append(str(item.text))
    for item in shipping_price_html:
        shipping_prices.append((str(item.text)))
    if(len(item_prices) == len(item_links) == len(item_names) == len(shipping_prices)):
        for i in range(len(item_names)):
            csv_file.write(item_names[i] + "," + item_links[i] + "," + item_prices[i] + "," + shipping_prices[i] + "\n")
    else:
        for i in range(len(item_names)):
            csv_file.write(item_names[i] + "," + item_links[i] + "," + item_prices[i] + "," + "COULD NOT COMPUTE\n")
    csv_file.close()