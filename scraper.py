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
<<<<<<< HEAD
from fastkml import kml
'''
k = kml.KML()
ns = '{http://www.opengis.net/kml/2.2}'
# Create a KML Document and add it to the KML root object
d = kml.Document(ns, 'docid', 'doc name', 'doc description')
k.append(d)

# Create a KML Folder and add it to the Document
f = kml.Folder(ns, 'fid', 'f name', 'f description')
d.append(f)

# Create a KML Folder and nest it in the first Folder
nf = kml.Folder(ns, 'nested-fid', 'nested f name', 'nested f description')
f.append(nf)

# Create a second KML Folder within the Document
f2 = kml.Folder(ns, 'id2', 'name2', 'description2')
d.append(f2)

# Create a Placemark with a simple polygon geometry and add it to the
# second folder of the Document
p = kml.Placemark(ns, 'id', 'name', 'description')
f2.append(p)

# Print out the KML Object as a string
print(k.to_string(prettyprint=True))
'''

#Google API information
googleApiKey = "AIzaSyCr90UZMD3fl6SLE7cHIDvWF4yofQdWIgk"
gmaps = googlemaps.Client(key=googleApiKey)

list = []
'''
#Salvation Army Thrift Store - done
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
'''
'''
#WORKING
#Inclusion BC & CPABC Clothing
print("Inclusion BC and CPABC Clothing")
url2 = "http://www.google.com/maps/d/kml?mid=1kqVfqYiPtnqrO8L5zC_yVkAiwB0&forcekml=1"
url3 = "https://www.google.com/maps/d/kml?mid=1ekVOoKgoAW2vIjiDh3DmP4OU04g&forcekml=1"
r2 = requests.get(url2)
r3 = requests.get(url3)

soup2 = BeautifulSoup(r2.content,"lxml")
soup3 = BeautifulSoup(r3.content,"lxml")

filtered2 = soup2.find_all("placemark")
filtered3 = soup3.find_all("placemark")

print("Inclusion BC")
for item in filtered2:
	addBin = Bin("", "", "", "", "", "")
	addBin.address = item.find_all("name")[0].text.strip()
	addBin.coordinate = item.find_all("coordinates")[0].text.strip()
	addBin.company = "Inclusion BC"
	list.append(addBin)

print("Cerebral Palsy Association of British Columbia")
for item in filtered3:
	addBin = Bin("", "", "", "", "", "")
	addBin.address = item.find_all("name")[0].text.strip()
	addBin.coordinate = item.find_all("coordinates")[0].text.strip()
	addBin.company = "Cerebral Palsy Association of British Columbia"
	list.append(addBin)


for item in list:
	if item.address:
		list.remove(item)
'''
'''
#WORKING
#Diabetes Canada
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
'''
'''
#WORKING
#Big Brothers
=======
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
>>>>>>> d74249ab8f556b96f5bd7d4bb99ecdda04e04152
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
<<<<<<< HEAD
'''
'''
Traceback (most recent call last):
  File "scraper.py", line 193, in <module>
    item.coordinate = geocode_result[0]['geometry']['location']
IndexError: list index out of range
'''

#Develop BC
print("develop bc")

#r = urllib2.urlopen("http://www.bcchauxiliary.com/our-businesses/clothing-donation-bin-program/")
#html = r.read()

#gmaps = googlemaps.Client(key="AIzaSyDqGPoS9GUio0FZndRTdnvNDFIatMHGeus")

url = "http://www.develop.bc.ca/find-a-clothing-bin/"
=======

# Develop BC
print("develop bc broken af")
'''
url = "http://www.develop.bc.ca/donate/"
>>>>>>> d74249ab8f556b96f5bd7d4bb99ecdda04e04152
browser = webdriver.PhantomJS()
browser.get(url)
time.sleep(1)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
<<<<<<< HEAD
individual_results = soup.find_all("script")
=======
>>>>>>> d74249ab8f556b96f5bd7d4bb99ecdda04e04152

print(soup)
individual_results = soup.find_all("div", {"class": "results_wrapper"})
print(individual_results)
for result in individual_results:
<<<<<<< HEAD
   resultString = result.string
   #print(resultString)
   search = 'mapData'
   if resultString is not None:
   	if search in resultString:
   		addressesString = resultString
startString = addressesString.find('[')
endString = addressesString.rfind(']')
jsonString = addressesString[startString:endString +1]

json_1 = json.loads(jsonString)

for j in json_1:
	addBin = Bin("", "", "", "", "", "")
	splitted = j["location"]["address"].split(",")

	addBin.address = splitted[0]
	addBin.city = splitted[1]
	addBin.company = "Develop BC"
	list.append(addBin)



#geoencoding
for item in list:
	if item.getCoordinate():
		coordinateRaw = item.getCoordinate()
		coordinate = coordinateRaw.split(",")
		reverse_geocode_result = gmaps.reverse_geocode((coordinate[1],coordinate[0]))
		print(item.getCompany())
		print(reverse_geocode_result[0]['formatted_address'])


	elif item.getAddress():
		address = item.getAddress()
		geocode_result = gmaps.geocode(address)
		item.coordinate = geocode_result[0]['geometry']['location']
		print(item.getCompany())
		print(geocode_result[0]['formatted_address'])




=======
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
>>>>>>> d74249ab8f556b96f5bd7d4bb99ecdda04e04152
