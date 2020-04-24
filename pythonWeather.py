import urllib.request
import json
class weather:
    def __init__(self, city, key):
        self.city = city
        self.key = key
        self.URL = "http://api.openweathermap.org/data/2.5/weather?q="

    def getTemprature(self):
        try:
            fullURL = str(self.URL+self.city+"&appid="+self.key+"&units=metric")
            data = urllib.request.urlopen(fullURL).read()
            temp = float(json.loads(data)["main"]["temp"])
            x = str(temp)
            return x+" degrees celcius"

        except urllib.error.HTTPError:
            return("Not Found!")

city = input("Enter your city : ")
apiKey = "54df40e238084fbf095d3540271e48a0"

cityWeather = weather(city, apiKey)
print(cityWeather.getTemprature())
