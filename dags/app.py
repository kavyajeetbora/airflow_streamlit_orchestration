import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from weather_etl import plot_city_temperatures
from datetime import datetime
import time


# Streamlit app header
st.header("Weather for Top 25 Cities in India 🇮🇳", divider="gray")


while True:

    ## Load the updated data
    df = pd.read_csv(
        r"C:\Users\kbora\Desktop\Development\Data Engineering\01-Airflow-Example\data\weather.csv"
    )

    ## Plot with the updated data
    fig = plot_city_temperatures(df)

    # # Display the last updated time
    # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # st.markdown(
    #     f"<p style='font-size: 14px;'>Last updated: {current_time}</p>",
    #     unsafe_allow_html=True,
    # )
    ## Render the plot in application
    st.pyplot(fig)

    time.sleep(300)  ## Sleep for N seconds
