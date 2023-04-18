import requests

API_KEY = "41a2220720568f359b5b3d238c78d2e8"
city = "Cachoeiro de Itapemirim"
link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br"

request = requests.get(link)
requestDict = request.json()

temperature = requestDict['main']['temp'] - 273.15

if (temperature < 36):
    print('Temperature is below normal')
elif (temperature > 37):
    print('Temperature is above normal')
else:
    print('Temperature is within normal')