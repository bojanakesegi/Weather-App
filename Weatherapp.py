import requests

api_key = '068efc0b52acce34a311e1144512e8f0'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

#extracting weather and temp from text
weather = weather_data.json()["weather"][0]['main']
temp = weather_data.json()["main"]['temp']

print(weather, temp)