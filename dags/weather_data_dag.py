from __future__ import annotations
import pendulum
from airflow.decorators import dag, task
from weather_etl import get_weather_dataframe, export_to_json
import logging
import pendulum

logger = logging.getLogger(__name__)


@dag(
    dag_id="dag_weather_update_v2",
    schedule=None,
    description="Weather upates for 20 major cities in India",
    start_date=pendulum.datetime(2024, 11, 23, tz="Asia/Kolkata"),
    catchup=False,
    tags=["weather_updates", "airflow"],
    schedule_interval="*/5 * * * *",  ## Running the DAG at every N Minutes
)
def weather_taskflow_api():

    @task()
    def ETL():
        """
        # #### Extract Transform Load
        # Extracting the weather data for 20 cities from weatherapi in JSON format
        # And will plots the bar graph
        #"""
        try:
            df = get_weather_dataframe()
            export_path = r"/opt/airflow/dags/data/weather.csv"

            export_time = pendulum.now("Asia/Kolkata")
            # Convert to string in a specific format
            export_time_str = export_time.format("YYYY-MM-DD HH:mm:ss")
            df.to_csv(export_path)

            json_file_path = r"/opt/airflow/dags/data/metadata.json"
            export_to_json(export_time_str, export_path, json_file_path)

            logger.info(
                f"Successfully Update the dataframe and exported to {export_path}"
            )

        except Exception as e:
            logger.info("Error:" + str(e))

    ETL()


weather_taskflow_api()
