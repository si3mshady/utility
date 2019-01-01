import sqlite3,json,urllib.request

class SIGNS:
	def __init__(self,streetNumber,streetName,city,state,url,apikey):	
		self.streetNumber = streetNumber
		self.streetName = streetName
		self.city = city
		self.state = state
		self.url = url 
		self.apikey = apikey
		self.mainUrl = url + str(streetNumber) + "+" + streetName + ",+" + city + ",+" + state + apikey	

	
def getAddressValues():
	results = []
	signs = ['Street Number: ','Street Name: ','City: ','State: ']
	print("Please Enter the following values:")
	for i in range(len(signs)):
		val = str(input(signs[i]))
		results.append(val)
	return results

def getCursor():
	database_file = '''SIGNS_TABLEx.db'''
	global database
	database = sqlite3.connect(database_file)
	c = database.cursor()
	database = sqlite3.row_factory = sqlite3.Row	
	return c

def getSignsTable():
	create_table = '''CREATE TABLE IF NOT EXISTS Signs (
	addressID INTEGER PRIMARY KEY NOT NULL,
	streetNumber INTEGER NOT NULL,
	streetName TEXT NOT NULL,
	city TEXT NOT NULL,
	state TEXT NOT NULL,
	lat NUMERIC NULL,
	lng NUMERIC  NULL);'''
	c = getCursor()
	if c.execute(create_table):
		print("'Signs' Table is available")
	else:
		print("Unable to create 'Signs' table")

def insertAddress(stnum,stname,city,state,lat,lng):
	insert = "INSERT INTO Signs (streetNumber,streetName,city,state,lat,lng) VALUES (?,?,?,?,?,?);"
	c = getCursor()
	if c.execute(insert,(int(stnum),str(stname),str(city),str(state),float(lat),float(lng))):
		print(str(stnum) + " " + stname + " " + city + " " + state + " " + str(lat) + " " + str(lng) +  " has been entered into Database.")
	else:
		print("Error in inserting " + str(stnum) + " " + stname + " " + city + " " + " " + state + " " +  str(lat) + " " + str(lng) + " into Database.")

def main():	
	apikey = open("apikey.txt").read().strip()
	baseUrl = '''https://maps.googleapis.com/maps/api/geocode/json?address='''	
	latitudeList = longitudeList =[]
	getSignsTable()
	sigue = True 
	while sigue:
		address = getAddressValues()
		sign = SIGNS(int(address[0]),str(address[1]),str(address[2]),str(address[3]),url=baseUrl,apikey=apikey)		
		response  = urllib.request.urlopen(sign.mainUrl).read()
		clean = json.loads(response)
		lat = float(clean['results'][0]['geometry']['bounds']['northeast']['lat'])
		latitudeList.append(lat)
		lng = float(clean['results'][0]['geometry']['bounds']['northeast']['lng'])
		longitudeList.append(lng)
		latitudeList.append(lat)
		insertAddress(int(address[0]),str(address[1]),str(address[2]),str(address[3]),float(lat),float(lng))
		response = input("Continue? (Y/N) ")
		if response.lower() == "n":
			sigue = False
			print("Goodbye!")
		
	
if __name__== "__main__":
	main()

	#buring the midnightOil learning Python 3  Database Programming for the Campain of Carol King Arnold from Elliott Arnold  
