import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timezone, timedelta
from streamlit_autorefresh import st_autorefresh


# Streamlit app header
st.header("Weather for Top 25 Cities in India 🇮🇳", divider="gray")


def load_data(path):
    df = pd.read_csv(path)
    return df


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
# Display the last updated time
# Get the current time in the GMT+5:30 timezone
time_zone = timezone(timedelta(hours=5, minutes=30))
current_time = datetime.now(time_zone).strftime("%Y-%m-%d | %H:%M:%S")
update_time = st.markdown(
    f"<p style='font-size: 14px;'>Last updated: {current_time}</p>",
    unsafe_allow_html=True,
)

## Load the data
csv_path = r"shared-data/weather.csv"
df = load_data(csv_path)

# Render the plot in application
fig = plot_city_temperatures(df)
st.pyplot(fig)
