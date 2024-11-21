FROM python:3.9-slim

WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN echo "List of files in the current directory"
RUN pwd
RUN ls -la 
RUN echo "End of list of files"

EXPOSE 7751
HEALTHCHECK CMD curl --fail http://localhost:7751/_stcore/health || exit 1
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=7751", "--server.address=0.0.0.0"]

