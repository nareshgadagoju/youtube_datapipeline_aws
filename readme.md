# YouTube Comments ETL Project

## Project Overview
This project involves extracting YouTube video comments, including the username and timestamp, using the YouTube Data API. The extracted data is then transformed and cleaned using Python, and finally, it is loaded into an AWS S3 bucket for future analysis.

## Task 1: Extract Data from YouTube API
To extract data from the YouTube API, we have implemented a Python script named `youtube_etl.py`. This script uses the Google API Client Library to connect to the YouTube Data API and retrieve comments for a specified video.

### Dependencies
- [Pandas](https://pandas.pydata.org/): Used for data manipulation.
- [S3fs](https://s3fs.readthedocs.io/en/latest/): Used for interacting with AWS S3.
- [Google API Client Library](https://developers.google.com/youtube/registering_an_application): Used to connect to the YouTube Data API. You need to replace `'YOUR_API_KEY'` in the script with your actual YouTube Data API key.

### Usage
1. Replace `'YOUR_API_KEY'` in the script with your actual YouTube Data API key.
2. Specify the video ID for which you want to extract comments by setting the `video_id` variable.
3. Run the script to retrieve comments and save them in a CSV file on AWS S3.

## Task 2: Transform Data
Data transformation and cleaning are performed within the `youtube_etl.py` script. The script converts the retrieved data into a Pandas DataFrame, which allows for easy data manipulation and cleaning. You can add additional data transformation steps as needed.

## Task 3: Load Data/Store Data
The cleaned data is loaded into an AWS S3 bucket for storage. The S3 path for storing the data is specified in the `s3_path` variable in the `youtube_etl.py` script. You should replace `'s3://naresh-airflow/youtube_comments.csv'` with the appropriate path to your S3 bucket.

## Project Structure
- `youtube_etl.py`: Python script for extracting, transforming, and loading data.
- `youtube_dag.py`: Airflow DAG for scheduling and automating the ETL process.
- `README.md`: This documentation file.

## Usage
You can run the ETL process manually by executing the `youtube_etl.py` script or use an automation tool like Apache Airflow to schedule and monitor the ETL tasks.

### Apache Airflow
- The `youtube_dag.py` file defines an Apache Airflow DAG named 'youtube_dag'.
- The `PythonOperator` is used to run the `run_youtube_etl` function within the DAG.

Ensure you configure Apache Airflow with the necessary settings and dependencies to run the ETL process on a schedule.

## Author
Naresh

Feel free to adapt this README to your specific project needs and provide more details as necessary.
