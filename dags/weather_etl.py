import pandas as pd
import requests
import configparser
import json
import matplotlib.pyplot as plt
import os

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


def plot_city_temperatures(df):
    """
    Plots the temperature of cities from the given DataFrame.

    df (DataFrame): DataFrame containing city names and their corresponding temperatures.
    """
    fig, ax = plt.subplots(figsize=(12, 6))  # Create a figure and axis

    # Create a bar graph
    bars = ax.bar(df["City"], df["temp"], color="skyblue")

    # Add titles and labels
    ax.set_title("Temperature of Cities in India", fontsize=16)
    ax.set_xlabel("City", fontsize=14)
    ax.set_ylabel("Temperature (°C)", fontsize=14)

    # Rotate x-titles for better visibility
    ax.set_xticks(range(len(df["City"])))  # Set x-ticks to match the number of cities
    ax.set_xticklabels(df["City"], rotation=45, ha="right")

    # Add grid for better readability
    ax.yaxis.grid(True, linestyle="--", alpha=0.7)

    # Add value labels on top of each bar
    for bar in bars:
        yval = bar.get_height()  # Get the height of the bar
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            f"{yval:.2f}",
            ha="center",
            va="bottom",
            fontsize=10,
        )  # Add text above the bar

    # Adjust layout to prevent clipping of tick-labels
    plt.tight_layout()

    return fig
