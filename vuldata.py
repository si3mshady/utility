from urllib.request import urlopen as URL
from bs4 import BeautifulSoup as soup
import re,sqlite3

def gotVulns():
	database_file   = 'cve.db'

	db = sqlite3.connect(database_file)

	print("Connected to CVE database file.\n")

	c = db.cursor()

	query = '''CREATE TABLE IF NOT EXISTS Vuls (cve TEXT PRIMARY KEY  NULL, description TEXT NULL);'''

	c.execute(query)

	print("'Vuls' table online.\n")

	urlbase = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword="
	masterP = '''[^C][^V][^E]p">([A-Z]*[a-z\s\w\.,\(\)\-:*"\$&;'#\/]+)''' #masterParser
	cP = '''>(CVE[-\d{4,10}]+)<'''	#cveParser

	insert_cve = '''INSERT INTO Vuls (cve) VALUES (?)'''
	insert_desc = '''INSERT INTO Vuls (description) VALUES (?)'''

	while True:
		searchString = input("Please enter keyword to search Common Vulnerabilities and Exposures\n")
		mainURL = urlbase + searchString
		raw_html = URL(mainURL)
		htmlSoup = soup(raw_html,"html.parser")
		processedSoup = htmlSoup.findAll('td', valign='top')
		cve = re.findall(r'>(CVE[-\d{4,10}]+)<',str(processedSoup))
		descriptions = re.findall(r'[^C][^V][^E]p">([A-Z]*[a-z\s\w\.,\(\)\-:*"\$&;\'#\/]+)',str(processedSoup))

		for i in range(len(cve)):
			vuln = cve[i]
			c.execute(insert_cve,(vuln,))
			print(vuln + " was entered into database successfully.")

		for v in range(len(descriptions)):
			description = descriptions[v]
			c.execute(insert_desc,(description,))
			print(description + " was entered into database successfully.")

		ans = input("Continue? (Y/N)\n")
		if ans.lower() != "y":
			print("Goodbye!")
			break


if __name__ == "__main__":
	gotVulns()

#Creating Tools with Python 3.  DIY Vulnerability Database   WIP    Happy Halloween  - Si3mShady aka EL AD 

