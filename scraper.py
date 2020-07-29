import urllib.request
import os
from bs4 import BeautifulSoup
link = input("Enter the E-Bay Search Link that you wish to scrape from: ")
#Request:
req = urllib.request.urlopen(link)
#String of Website HTML
req_html = req.read()
#Close Request
req.close()
#HTML Parser!
req_soup = BeautifulSoup(req_html, 'html.parser')
raw_items = req_soup.findAll("li", {"class":"s-item"})
#Write raw_items to textfile
csv_file = open("./Web-Scraping/shop.csv","w")
headers = "Item Name, Item Link"
csv_file.write(headers + "\n")
for item in raw_items:
    item_name = str(item.div.div.div.a.div.img["alt"])
    item_link = str(item.div.div.div.a.div.img["src"])
    csv_file.write(item_name + "," + item_link + "\n")
csv_file.close()
#for item in raw_items: 
#    item.findAll("")