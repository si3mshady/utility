import sqlite3,json,gmplot,urllib.request
#from urllib.request import urlopen as URL


#create a class that holds address objects check 
#create a class that holds gmplot objects 
#create a database that holds address  check 

#create database 
#create address object 
#enter address object into database 
#retrive address from database 

#enter address into database 
#retrive address from database then 


class SIGNS:
	def __init__(self,streetNumber,streetName,city,state,url,apikey):	
		self.streetNumber = streetNumber
		self.streetName = streetName
		self.city = city
		self.state = state
		self.url = url 
		self.apikey = apikey
		self.mainUrl = url + streetNumber + "+" + streetName + ",+" + city + ",+" + state + apikey	

	
def main():	
	apikey = open("apikey.txt").read().strip()
	baseUrl = '''https://maps.googleapis.com/maps/api/geocode/json?address='''	
	latitudeList = longitudeList =[]
	database_file = '''signs.db'''
	db = sqlite3.connect(database_file)
	c = db.cursor()


	createDB = '''DROP TABLE IF EXISTS SIGNS; CREATE TABLE Signs (
	addressID INTEGER PRIMARY KEY NOT NULL,
	streetNumber TEXT NOT NULL,
	streetName TEXT NOT NULL,
	city TEXT NOT NULL ,
	state TEXT NOT NULL)'''
	c.execute(createDB)
	print("Connected to Signs Database.")
	
	start = True
	while start:
		address = getAddressValues()
		sign = SIGNS(address[0],address[1],address[2],address[3],url=baseUrl,apikey=apikey)

		insert = '''INSERT INTO Signs (streetNumber,streetName,city,state) VALUES (?,?,?,?)'''
		c.execute(insert,(str(address[0]),str(address[1]),str(address[2]),str(address[3]))
		#print(str(address[0]) + " " + str(address[1]) + " " + str(address[2]) + " " + str(address[3]) + " " + "was entered into database sucessfully.")

		response  = urllib.request.urlopen(sign.mainUrl).read()
		clean = json.loads(response)
		lat = clean['results'][0]['geometry']['bounds']['northeast']['lat']
		lng = clean['results'][0]['geometry']['bounds']['northeast']['lng']
		print("lat",lat)
		print("lng",lng)
	

main()
