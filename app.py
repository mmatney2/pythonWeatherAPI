#create flask application and call API
#call the data in python 
import requests
import configparser

#configparser reads the config.ini file and get the api key
def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

#function takes in a zip and api key 
def get_weather_results(zip_code, api_key):
    api_url="http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}".format(zip_code, api_key)
    #convert data and call it in python
    r = requests.get(api_url)
    return r.json()

print(get_weather_results("95129", get_api_key()))

