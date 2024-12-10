import streamlit as st
import pandas as pd
import folium
from branca.colormap import LinearColormap
from datetime import datetime, timezone, timedelta
from streamlit_autorefresh import st_autorefresh
from streamlit_folium import st_folium
import json

# Set the page configuration to wide layout
st.set_page_config(layout="wide")

# Remove whitespace from the top of the page and sidebar
st.markdown(
    """
        <style>
                .stAppHeader {
                    background-color: rgba(255, 255, 255, 0.0);  /* Transparent background */
                    visibility: visible;  /* Ensure the header is visible */
                }

               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

# Streamlit app header with reduced size
st.header(
    "Real-Time Weather for 30 Cities in India",
    divider=True,
)


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
        metadata = f"Time Exported: {export_time}"
        return metadata

    except FileNotFoundError:
        print(f"Error: The file {json_file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file {json_file_path} is not a valid JSON file.")


def plot_city_on_map(df, current_time):
    """
    Plots cities on a Folium map with markers displaying city name and temperature.
    """
    # Calculate min and max temperatures
    min_temp = df["temp"].min()
    max_temp = df["temp"].max()

    # Create a colormap
    colormap = LinearColormap(
        ["blue", "green", "yellow", "orange", "red"], vmin=min_temp, vmax=max_temp
    )

    m = folium.Map(location=[20.5937, 78.9629], zoom_start=4)

    for index, row in df.iterrows():
        city = row["City"]
        lat = row["Latitude"]
        lon = row["Longitude"]
        temp = row["temp"]

        # Determine color based on temperature
        color = colormap(temp)

        folium.CircleMarker(
            location=[lat, lon],
            radius=8,
            color=color,  # Set marker color
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            popup=f"<b>City:</b> {city}<br><b>Temperature:</b> {temp}°C",
            tooltip=f"{city}: {temp}°C",  # Display city and temperature on hover
        ).add_to(m)

    m.add_child(colormap)  # add colormap to the map
    return m


# update every 5 seconds
refreshed = st_autorefresh(interval=5 * 1000, key="dataframerefresh")

# ## Load the data
csv_path = r"shared-data/weather.csv"
json_file_path = r"shared-data/metadata.json"

## Local path for testing the streamlit app
# csv_path = r"config\data\weather.csv"
# json_file_path = r"config\data\metadata.json"

if refreshed >= 0:
    df = load_data(csv_path)
    metadata = get_metadata(json_file_path)
    st.text(metadata)
    # Render the plot in application
    Map = plot_city_on_map(df, metadata)
    st_folium(Map, width=725)
