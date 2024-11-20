import pandas as pd
import requests
import configparser
import json

## Load the API key for access
config_file_path = r"/opt/airflow/config/config.cfg"
parser = configparser.ConfigParser()
parser.read(config_file_path)
api_key = parser["KEYS"]["api_key"]

## Load the constants
URL = f"https://api.openweathermap.org/data/2.5/weather"
CITIES = pd.read_csv(r"/opt/airflow/config/data/top_20_cities_india.csv")
COLUMNS = [
    "temp",
    "feels_like",
    "temp_min",
    "temp_max",
    "pressure",
    "humidity",
    "sea_level",
    "grnd_level",
]


## Get the temperature data from location
def get_weather_data(lat, lon):
    params = {"lat": lat, "lon": lon, "appid": api_key, "units": "metric"}
    response = requests.get(URL, params=params)

    data = None
    if response.status_code == 200:
        json_object = json.loads(response.text)
        data = json_object["main"]
        data = list(data.values())

    else:
        print("Connection Error")

    return data


## Get the temperature data fpr all the locations
def get_weather_dataframe():

    weather_df = CITIES.copy()
    weather_df["weather_data"] = weather_df.apply(
        lambda x: get_weather_data(x["Latitude"], x["Longitude"]), axis=1
    )
    weather_df[COLUMNS] = weather_df["weather_data"].to_list()
    weather_df.drop("weather_data", axis=1, inplace=True)

    return weather_df
