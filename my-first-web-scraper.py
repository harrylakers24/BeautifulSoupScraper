from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card'
 #opening up connection grabbing page
 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})

for container in containers: 

    model = container.findAll('a', 'item-title')
    product_name = model[0].text

    print("product_name: " + product_name)