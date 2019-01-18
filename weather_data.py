import requests,shelve

class Brick_Tamland:
    def __init__(self,city):
        self.baseurl = "http://api.apixu.com/v1/current.json?key="
        self.city = city
        self.apikey = self.get_weather_apikey()
        self.main_url = self.baseurl +  self.apikey +  self.city       
        self.weather_report = self.fetch_weather_data()
              
    def fetch_weather_data(self): 
        data = requests.get(self.main_url)
        json_data = data.json()
        return json_data

    def get_weather_apikey(self):
        with shelve.open('apikey') as api:
            key = api['api_key']
        return key





       