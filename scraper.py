#this file contains all the functions concerned with scraping
#html table sites
#google map sites
#get data
#misc scraper

import googlemaps
import requests
import json
from bs4 import BeautifulSoup
from bin import Bin
#import urllib2
from bs4 import UnicodeDammit
from contextlib import closing
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
import simplekml

kml = simplekml.Kml()

#Google API information
googleApiKey = "AIzaSyAOyu_oSTIsdrxgYm6Fby0DckoZGMdJECA"
gmaps = googlemaps.Client(key=googleApiKey)

list = []

#Salvation Army Thrift Store - done
try:
    print("Salvation Army")
    url1 = "https://www.thriftstore.ca/british-columbia/drop-bin-locations"
    r1 = requests.get(url1)
    print("Salvation army request")
    soup1 = BeautifulSoup(r1.content,"lxml")
    filtered1 = soup1.find_all("tr")

    for td in filtered1:
        inter = td.find_all("span")
        count = 0
        addBin = Bin("", "", "", "", "", "")
        while (count <= 3):
            value = inter[count].text.strip()
            if(count == 0):
                addBin.name = value
            elif (count == 1):
                addBin.company = value
            elif (count == 2):
                addBin.address = value
            else:
                addBin.city = value
            count += 1
        list.append(addBin)
except requests.exceptions.RequestException as e:
    print (e)

#WORKING
#Inclusion BC & CPABC Clothing
'''
#InclusionBC
try:
    url2 = "http://www.google.com/maps/d/kml?mid=1kqVfqYiPtnqrO8L5zC_yVkAiwB0&forcekml=1"
    r2 = requests.get(url2)
    soup2 = BeautifulSoup(r2.content,"lxml")
    filtered2 = soup2.find_all("placemark")
    print("Inclusion BC")
    for item in filtered2:
        addBin = Bin("", "", "", "", "", "")
        addBin.address = item.find_all("name")[0].text.strip()
        addBin.coordinate = item.find_all("coordinates")[0].text.strip()
        addBin.company = "Inclusion BC"
        list.append(addBin)
except requests.exceptions.RequestException as e:
    print (e)

#Cerebral Palsy
try:
    url3 = "https://www.google.com/maps/d/kml?mid=1ekVOoKgoAW2vIjiDh3DmP4OU04g&forcekml=1"
    r3 = requests.get(url3)
    soup3 = BeautifulSoup(r3.content,"lxml")
    filtered3 = soup3.find_all("placemark")
    print("Cerebral Palsy Association of British Columbia")
    for item in filtered3:
        addBin = Bin("", "", "", "", "", "")
        addBin.address = item.find_all("name")[0].text.strip()
        addBin.coordinate = item.find_all("coordinates")[0].text.strip()
        addBin.company = "Cerebral Palsy Association of British Columbia"
        list.append(addBin)
except requests.exceptions.RequestException as e:
    print (e)

#WORKING
#Diabetes Canada
try:
    print("Diabetes Canada")
    url1 = "http://www.diabetes.ca/dropBoxes/phpsqlsearch_genxml.php?&lat=49.2057&lng=-122.9110&radius=50"
    r1 = requests.get(url1)

    soup1  = BeautifulSoup(r1.content,"lxml")

    filtered = soup1.find_all("marker",{"type":"Drop Box"})

    for item in filtered:
        addBin = Bin("", "", "", "", "", "")
        addBin.address = item['address']
        addBin.company = "Diabetes Canada"
        list.append(addBin)
except requests.exceptions.RequestException as e:
    print (e)


#WORKING
#Big Brothers
print("Big Brothers")
url = "https://www.bigbrothersvancouver.com/clothing-donation/donation-bins/"
browser = webdriver.PhantomJS()
browser.get(url)
time.sleep(1)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
filtered1 = soup.find_all("div", {"class":"location_secondary"})
for item in filtered1:
    #print(item)
    item_street = item.find_all("span", {"class": "slp_result_street"})
    item_city = item.find_all("span", {"class": "slp_result_citystatezip"})
    addBin = Bin("", "", "", "", "", "")
    addBin.address = item_street[0].text.strip() + " " +item_city[0].text.strip()
    addBin.company = "Big Brothers"
    list.append(addBin)

browser.close()

#Develop BC
print("develop bc")

url = "http://www.develop.bc.ca/donate/"
with closing(PhantomJS()) as browser:
   browser.get(url)
   html = browser.page_source
#r = urllib2.urlopen("http://www.bcchauxiliary.com/our-businesses/clothing-donation-bin-program/")
#html = r.read()

#gmaps = googlemaps.Client(key="AIzaSyDqGPoS9GUio0FZndRTdnvNDFIatMHGeus")

url = "http://www.develop.bc.ca/donate/"
browser = webdriver.PhantomJS()
browser.get(url)
time.sleep(1)
html = browser.page_source

soup = BeautifulSoup(html, "lxml")
individual_results = soup.find_all("div", {"class":"results_wrapper"})

for result in individual_results:
   address = ""
   address_components = result.find_all("span", {"class":"slp_result_address"})
   for address_component in address_components:
       address += address_component.get_text()
       if('slp_result_citystatezip' in address_component.get("class")):
           address += ", "

print(address)

'''
print("getting here")

#geoencoding
for item in list:
    if item.getCoordinate():
        coordinateRaw = item.getCoordinate()
        coordinate = coordinateRaw.split(",")
        reverse_geocode_result = gmaps.reverse_geocode((coordinate[1],coordinate[0]))
        item.coordinate = str(reverse_geocode_result[0]['geometry']['location']['lng']) + ", " + str(reverse_geocode_result[0]['geometry']['location']['lat']) + ", 0"
        item.address= reverse_geocode_result[0]['formatted_address'] #save the returned address
        kml.newpoint(name=item.getCompany(), coords=[(item.getCoordinate())])  # lon, lat, optional height
        print(item.getCompany())
        print(item.getAddress())
        print(item.getCoordinate())

    elif item.getAddress():
        address = item.getAddress()
        geocode_result = gmaps.geocode(address)
        item.coordinate = str(geocode_result[0]['geometry']['location']['lng'])  + ", " + str(geocode_result[0]['geometry']['location']['lat']) + ", 0"
        item.address = geocode_result[0]['formatted_address'] #save the returned address
        kml.newpoint(name=item.getCompany(), coords=[(item.getCoordinate())])  # lon, lat, optional height
        print(item.getCompany())
        print(item.getAddress())
        print(item.getCoordinate())



print(kml)
kml.save("plot.kml")

#for item in list:
  #  print(item)
