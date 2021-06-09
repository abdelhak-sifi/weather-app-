import requests

cities =  ['Las Vegas','London','Algeria']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=22fc6df347b1d74613e0be0f3e39d5af'
l=[]
for city in cities:  
  city_weather = requests.get(url.format(city)).json()
  print(city_weather['main']['temp']) 
  break
  weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
            } 
  l.append( weather)           
#print(l)