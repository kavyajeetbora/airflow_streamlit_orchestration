# Geospatial Data Pipeline Orchestration using Airflow

This project demonstrates a simple geospatial data pipeline orchestration using Apache Airflow, designed to update weather data for around 30 cities in India every 5 minutes. It serves as a practical introduction to the orchestration of geospatial data pipelines, where you will learn essential concepts related to Docker, Docker Compose, Airflow, and microservices.

<img src="https://github.com/user-attachments/assets/6607d5a3-c6a1-44f9-b310-6b3411cdaacd" height=400/>

## Pipeline Workflow

<img src="https://github.com/user-attachments/assets/86858b44-cb73-4aea-8478-41550620f0fe" height=300/>

1. **Data Acquisition**: The pipeline fetches weather data from an external API and processes it before exporting the results to a CSV file. This is achieved by creating a Directed Acyclic Graph (DAG) in Apache Airflow.

2. **Scheduled Updates**: The DAG is configured to run every 5 minutes, ensuring that the weather data remains up-to-date and reflects the latest conditions.

3. **Interactive Map Visualization**: A Streamlit application is developed to display an interactive map that visualizes the weather data for various locations across India. The Folium library is utilized to create this map, with each city represented by markers that indicate temperature.

4. **Real-Time Updates**: The Streamlit app is set to refresh every 5 minutes, allowing users to view the most current weather information without needing to manually reload the page.

5. **Folder Structure**:

   ```
      app/
      ├── app.py
      ├── Dockerfile
      ├── requirements.txt
      config/
      dags/
      ├── dag1.py
      ├── dag2.py
      plugins/
      docker-compose.yaml
   ```
   The folder structure organizes the project into distinct directories:
   
   - **`app/`**: Contains the main application files, including the Streamlit app and Docker configuration.
   - **`config/`**: Holds configuration files.
   - **`dags/`**: Contains the Airflow Directed Acyclic Graphs (DAGs) for task orchestration.
   - **`plugins/`**: For any custom Airflow plugins.
   - **`docker-compose.yaml`**: Facilitates the orchestration of the entire application using Docker.


## Getting Started

### Prerequisites

- Docker: Before setting up, make sure docker is installed in your system. Otherwise refer to [Docker Installation](https://docs.docker.com/engine/install/)

### Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/kavyajeetbora/airflow_streamlit_orchestration.git
   cd <repository-directory>
   ```
2. **Setting Up Weather API Key**:
   
   - **Sign Up**: Create an account on the [OpenWeatherMap](https://openweathermap.org/) website to obtain your API key.
   - **Generate API Key**: After logging in, navigate to the API section and generate a new API key for your application.
   - **Configure Your Application**: In the `config/` folder, refer to the `config/config_example.txt` file for the format to enter your API key and create your own configuration file within the `config` folder (`config/config.cfg`).
   
3. **Build the Docker Image**:

   ```bash
   docker-compose airflow-init
   ```

4. **Run the Application in detached mode**:
   ```bash
   docker-compose up -d
   ```

### Accessing the Application

- **Airflow Web UI**: [http://localhost:8080](http://localhost:8080)
- **Streamlit App**: [http://localhost:7751](http://localhost:7751)

## Extending the Docker Image

To add additional Python packages, modify the `Dockerfile` in the `app` directory and rebuild the image.

## Resources

- [Learn Docker in 1 hour](https://youtu.be/pTFZFxd4hOI?si=BNK7WsnZxdXB3bl-)
- [Airflow Tutorial for Beginners - Full Course in 2 Hours](https://youtu.be/K9AnJ9_ZAXE?si=OdZKGaWbYLgQLeoC)
- [Airflow Documentation](https://airflow.apache.org/docs/)
- [Deploying Streamlit using Docker](https://docs.streamlit.io/deploy/tutorials/docker)
- [Introduction to docker compose ?](docs/docker-compose-up.md)
- [Why Docker Compose ?](docs/docker-compose-file.md)

## License

This project is licensed under the Apache License, Version 2.0.
