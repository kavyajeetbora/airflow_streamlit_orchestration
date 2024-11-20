# Create Data Pipeline using Airflow

The tutorial is based on the following video:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/q8q3OFFfY6c/0.jpg)](https://www.youtube.com/watch?v=q8q3OFFfY6c)

## Refreshing the streamlit application

Here is how we can rerun the streamlit application with a time interval: [link](https://discuss.streamlit.io/t/st-memization-memo-ttl-question/28655/2?u=kavyajeetbora)

## Extending the docker image

Using `Docker file` we can extend the default docker image with external python packages and many more

Create a `Docker file` in the current directory:

```
FROM apache/airflow:2.10.3
COPY requirements.txt /requirements.txt
EXPOSE 8080
EXPOSE 8503
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt
```

After creating this, we can use this docker file to create a new docker image with these specify extensions:

```
docker build . --tag extending_airflow:latest
```
