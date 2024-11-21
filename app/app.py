import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import time

# global variables
csv_path = r"../opt/airflow/config/data/weather.csv"
refresh_time = 20

# Streamlit app header
st.header("Weather for Top 25 Cities in India 🇮🇳", divider="gray")


@st.cache_data(ttl=refresh_time)
def load_data(csv_path):
    df = pd.read_csv(csv_path)
    return df


@st.cache_data(ttl=refresh_time)
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


## Load the data
df = load_data(csv_path)

## Plot with the updated data
fig = plot_city_temperatures(df)

# Display the last updated time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
update_time = st.markdown(
    f"<p style='font-size: 14px;'>Last updated: {current_time}</p>",
    unsafe_allow_html=True,
)
# Render the plot in application
updated_plot = st.pyplot(fig)

time.sleep(refresh_time)
