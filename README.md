# A Data Quality-Driven View of MLOps : 

### Project Description

* In this Project, I implemented a comprehensive data quality management framework that integrates automated validation, cleansing processes, and real-time monitoring within Apache Airflow-based data pipelines. This framework includes distinct DAGs for data cleansing, quality assessment and performance evaluation, ensuring each aspect of the data pipeline is handled efficiently and independently. The real-time monitoring system triggers subsequent DAGs based on the detection of data anomalies, allowing for dynamic and adaptive responses to data quality issues.

### Tools 

* Python
* Airflow

### How to Run(VSCODE):

* Create Virtual Environment and Activate it.

* Install Airflow :
* > pip install apache-airflow

* After installation, set up the metadata database :
  > airflow db init

* Airflow needs a user to access the web interface. You can create a user like this:
  > airflow users create \
   --username admin \
   --password admin \
   --firstname Admin \
   --lastname User \
   --role Admin \
   --email admin@example.com

* Start Airflow Scheduler and Web Server, Open two separate terminals:
  > For Scheduler : airflow scheduler \
  > For Web Server : airflow webserver --port 8080







