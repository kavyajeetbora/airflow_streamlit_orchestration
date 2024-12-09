import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timezone, timedelta
from streamlit_autorefresh import st_autorefresh
import json

# Streamlit app header
st.header("Weather for Top 25 Cities in India 🇮🇳", divider="gray")


def load_data(path):
    df = pd.read_csv(path)
    df = df.sort_values(by="temp")
    return df


def get_metadata(json_file_path):
    """
    Reads export information from a JSON file and prints it in a specified format.

    Parameters:
    - json_file_path (str): The path to the JSON file containing export information.
    """
    try:
        # Read the JSON file
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        # Extract export time and export path
        export_time = data.get("export_time", "N/A")  # Default to 'N/A' if not found
        export_path = data.get("export_path", "N/A")  # Default to 'N/A' if not found

        # Print the export information
        metadata = f"Time Exported: {export_time} | Export Path: {export_path}"
        return metadata

    except FileNotFoundError:
        print(f"Error: The file {json_file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file {json_file_path} is not a valid JSON file.")


def plot_city_temperatures(data):
    """
    Plots the temperature of cities from the given DataFrame.

    df (DataFrame): DataFrame containing city names and their corresponding temperatures.
    """
    fig, ax = plt.subplots(figsize=(12, 6))  # Create a figure and axis
    # Create a bar graph
    bars = ax.bar(data["City"], data["temp"], color="skyblue")

    # Add titles and labels
    ax.set_title("Temperature of Cities in India", fontsize=16)
    ax.set_xlabel("City", fontsize=14)
    ax.set_ylabel("Temperature (°C)", fontsize=14)

    # Rotate x-titles for better visibility
    ax.set_xticks(range(len(data["City"])))  # Set x-ticks to match the number of cities
    ax.set_xticklabels(data["City"], rotation=45, ha="right")

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
    plt.tight_layout()
    return fig


# update every 5 seconds
refreshed = st_autorefresh(interval=5 * 1000, key="dataframerefresh")

# ## Load the data
csv_path = r"shared-data/weather.csv"
json_file_path = r"shared-data/metadata.json"

## Local path for testing the streamlit app
# local_path = r"config\data\weather.csv"
# local_json_file = r"config\data\metadata.json"

if refreshed >= 0:
    df = load_data(csv_path)
    metadata = get_metadata(json_file_path)
    st.text(metadata)
    st.dataframe(df)

    # Render the plot in application
    fig = plot_city_temperatures(df)
    st.pyplot(fig)
