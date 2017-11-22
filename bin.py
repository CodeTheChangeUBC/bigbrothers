#class definition of bin object and other related code
class Bin:
    company = ""
    address = ""
    city = ""
    postalCode = ""
    coordinate = ""
    name =""

    def __init__(self, company, address, city, postalCode, coordinate, name):
        self.company = company
        self.address = address + self.city + "British Columbia, Canada"
        self.city = city
        self.postalCode = postalCode
        self.coordinate = coordinate
        self.name = name

    def __str__(self):
        return "Data in this bin: \n" + "Company: " + self.company + "\nAddress: " +  self.address + "\nCity: " +  self.city + "\nName: " + self.name + "\nCoordinates: " + self.coordinate

    def getCompany(self):
        return self.company
    def getAddress(self):
        return self.address
    def getCity(self):
        return self.city
    def getPostalCode(self):
        return self.postalscode
    def getCoordinate(self):
        return self.coordinate
    def getName(self):
        return self.names
    def getContents(self):
        return  self.name + " " + self.address + " " + self.postalCode

    def setCompany(company):
        self.company = companys
    def setAddress(address):
        self.address = address
    def setCity(city):
        self.city = city
    def setPostalCode(postalcode):
        self.postalcode = postalcode
    def setCoordinate(coordinatee):
        self.coordinate = coordinate
    def setName(name):
        self.name = name
