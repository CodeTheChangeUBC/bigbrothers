# this file contains all the functions concerned with scraping
# html table sites
# google map sites
# get data
# misc scraper
import googlemaps
import requests
import os
from bs4 import BeautifulSoup
from bin import Bin
from selenium import webdriver
import time
import simplekml
# Google API information
googleApiKey = "AIzaSyAOyu_oSTIsdrxgYm6Fby0DckoZGMdJECA"
gmaps = googlemaps.Client(key=googleApiKey)

list = []
bigbrothers = []
salvationarmy = []
inclusionbc = []
cerebralpalsy = []
diabetescanada = []

def openinterface ():
    path = "file://" +os.path.abspath("test.html")
    print(path)
    driver = webdriver.Firefox()
    driver.get(path)

def geocode (companyname,lst):
    kml = simplekml.Kml()
    for item in lst:
        if item.getCoordinate():
            coordinateRaw = item.getCoordinate()
            coordinate = coordinateRaw.split(",")
            reverse_geocode_result = gmaps.reverse_geocode(
                (coordinate[1], coordinate[0]))
            item.coordinate = str(reverse_geocode_result[0]['geometry']['location']['lng']) + ", " + str(
                reverse_geocode_result[0]['geometry']['location']['lat']) + ", 0"
            # save the returned data
            item.address = reverse_geocode_result[0]['formatted_address']
            coordinate = item.getCoordinate().split(",")
            pnt = kml.newpoint(name=item.getCompany(), description=item.getContents(), coords=[
                         (coordinate[0], coordinate[1], coordinate[2])])  # lon, lat, optional height

        elif item.getAddress():
            address = item.getAddress()
            geocode_result = gmaps.geocode(address)
            item.coordinate = str(geocode_result[0]['geometry']['location']['lng']) + ", " + str(
                geocode_result[0]['geometry']['location']['lat']) + ", 0"
            # save the returned data
            item.address = geocode_result[0]['formatted_address']
            coordinate = item.getCoordinate().split(",")
            pnt = kml.newpoint(name=item.getCompany(), coords=[
                         (coordinate[0], coordinate[1], coordinate[2])], description=item.getContents())  # lon, lat, optional height
    print("saving file  " + companyname + ".kml")
    kml.save("generatedkml/"+companyname+".kml")
    print("SAVED")

# Salvation Army Thrift Store
try:
    print("Salvation Army")
    url1 = "https://www.thriftstore.ca/british-columbia/drop-bin-locations"
    r1 = requests.get(url1)
    print("Salvation army request")
    soup1 = BeautifulSoup(r1.content, "lxml")
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
                addBin.address = value + "British Columbia, Canada"
            else:
                addBin.city = value
            count += 1
        list.append(addBin)
        salvationarmy.append(addBin)
    geocode("SalvationArmy", salvationarmy)
except requests.exceptions.RequestException as e:
    print(e)


# InclusionBC
try:
    url2 = "http://www.google.com/maps/d/kml?mid=1kqVfqYiPtnqrO8L5zC_yVkAiwB0&forcekml=1"
    r2 = requests.get(url2)
    soup2 = BeautifulSoup(r2.content, "lxml")
    filtered2 = soup2.find_all("placemark")
    print("Inclusion BC")
    for item in filtered2:
        addBin = Bin("", "", "", "", "", "")
        addBin.address = item.find_all("name")[0].text.strip()
        addBin.coordinate = item.find_all("coordinates")[0].text.strip()
        addBin.company = "Inclusion BC"
        list.append(addBin)
        inclusionbc.append(addBin)
    geocode("InclusionBC", inclusionbc)
except requests.exceptions.RequestException as e:
    print(e)

# Cerebral Palsy
try:
    url3 = "https://www.google.com/maps/d/kml?mid=1ekVOoKgoAW2vIjiDh3DmP4OU04g&forcekml=1"
    r3 = requests.get(url3)
    soup3 = BeautifulSoup(r3.content, "lxml")
    filtered3 = soup3.find_all("placemark")
    print("Cerebral Palsy Association of British Columbia")
    for item in filtered3:
        addBin = Bin("", "", "", "", "", "")
        addBin.address = item.find_all("name")[0].text.strip()
        addBin.coordinate = item.find_all("coordinates")[0].text.strip()
        addBin.company = "Cerebral Palsy Association of British Columbia"
        list.append(addBin)
        cerebralpalsy.append(addBin)
    geocode("CerebralPalsy", cerebralpalsy)
except requests.exceptions.RequestException as e:
    print(e)

# Diabetes Canada
try:
    print("Diabetes Canada")
    url1 = "http://www.diabetes.ca/dropBoxes/phpsqlsearch_genxml.php?&lat=49.2057&lng=-122.9110&radius=50"
    r1 = requests.get(url1)
    soup1 = BeautifulSoup(r1.content, "lxml")
    filtered = soup1.find_all("marker", {"type": "Drop Box"})
    for item in filtered:
        addBin = Bin("", "", "", "", "", "")
        addBin.address = item['address']
        addBin.company = "Diabetes Canada"
        list.append(addBin)
        diabetescanada.append(addBin)
    geocode("DiabetesCanada", diabetescanada)
except requests.exceptions.RequestException as e:
    print(e)

# Big Brothers
print("Big Brothers")
url = "https://www.bigbrothersvancouver.com/clothing-donation/donation-bins/"
browser = webdriver.PhantomJS()
browser.get(url)
time.sleep(1)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
filtered1 = soup.find_all("div", {"class": "location_secondary"})
for item in filtered1:
    item_street = item.find_all("span", {"class": "slp_result_street"})
    item_city = item.find_all("span", {"class": "slp_result_citystatezip"})
    addBin = Bin("", "", "", "", "", "")
    addBin.address = item_street[0].text.strip() + " " + item_city[0].text.strip()
    addBin.company = "Big Brothers"
    list.append(addBin)
    bigbrothers.append(addBin)
geocode("BigBrothers", bigbrothers)
browser.close()

# Develop BC
print("develop bc broken af")
'''
url = "http://www.develop.bc.ca/donate/"
browser = webdriver.PhantomJS()
browser.get(url)
time.sleep(1)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
print(soup)
individual_results = soup.find_all("div", {"class": "results_wrapper"})
print(individual_results)
for result in individual_results:
    address = ""
    address_components = result.find_all(
        "span", {"class": "slp_result_address"})
    for address_component in address_components:
        address += address_component.get_text()
        if('slp_result_citystatezip' in address_component.get("class")):
            address += ", "
    print(address)
'''
for item in list:
    print(item)
