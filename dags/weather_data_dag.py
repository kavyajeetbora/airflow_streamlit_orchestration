from __future__ import annotations
import pendulum
from airflow.decorators import dag, task
from weather_etl import get_weather_dataframe


@dag(
    dag_id="dag_weather_update_v1",
    schedule=None,
    description="Weather upates for 20 major cities in India",
    start_date=pendulum.datetime(2024, 11, 11, tz="Asia/Kolkata"),
    catchup=False,
    tags=["weather_updates", "airflow"],
    schedule_interval="*/5 * * * *",  ## Running the DAG at every N Minutes
)
def tutorial_taskflow_api():

    @task()
    def ETL():
        """
        # #### Extract Transform Load
        # Extracting the weather data for 20 cities from weatherapi in JSON format
        # And will plots the bar graph
        #"""
        try:
            df = get_weather_dataframe()
            export_path = r"/opt/airflow/config/data/weather.csv"
            df.to_csv(export_path)

        except Exception as e:
            print("Error:", e)

    ETL()


tutorial_taskflow_api()