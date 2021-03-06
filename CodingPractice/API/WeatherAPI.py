import urllib.request
import json

api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
# Allow the user to input a city
city = input()
api_key = ""

#form the request url
url = api_endpoint + "?q=" + city + "&appid=" + api_key

#Print the URL
#print (url)

#use the url to get the response and store the response in a variable.
response = urllib.request.urlopen(url)

#Print the initial response from the server upon initial request
#print (response)

#If you want to use json to view all the responses
parseResponse = json.loads(response.read())

#Extract just the relevant data (All part of the json file)
temperature = parseResponse ['main'] ['temp']
weather = parseResponse ['weather'] [0] ['description']

print (temperature)
print (weather)


#print (parseResponse)