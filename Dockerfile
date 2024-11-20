FROM apache/airflow:2.10.3
COPY requirements.txt /requirements.txt
EXPOSE 8080
EXPOSE 8501
EXPOSE 8503
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt