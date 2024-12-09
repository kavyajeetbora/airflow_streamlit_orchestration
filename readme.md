# Geospatial Data Pipeline with Airflow

This project demonstrates how to orchestrate a geospatial data pipeline using Apache Airflow. The pipeline updates weather data for the top 25 cities in India every 5 minutes.

## Overview

- **Data Source**: Weather data is fetched from the [OpenWeatherMap API](https://openweathermap.org/api).
- **Folder Structure**:
  ```
  app/
  ├── app.py
  ├── Dockerfile
  ├── requirements.txt
  config/
  dags/
  plugins/
  docker-compose.yaml
  ```

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Airflow

### Setup

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Build the Docker Image**:

   ```bash
   docker-compose --build
   ```

3. **Run the Application**:
   ```bash
   docker-compose up
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

## License

This project is licensed under the Apache License, Version 2.0.
