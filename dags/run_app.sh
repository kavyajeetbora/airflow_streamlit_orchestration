# Kill any running Streamlit app
pkill -f "streamlit run /opt/airflow/dags/app.py"

# Run the Streamlit app
streamlit run /opt/airflow/dags/app.py --server.port=7751
