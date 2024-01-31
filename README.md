# Network Analysis Application

## Introduction
This tool performs network analysis, calculating "betweenness", "closeness", and "PageRank" for the Facebook-Ego dataset.

## Prerequisites
- Docker installed on your machine.

## Setup & Usage

**Cloning the Repository:**
```
git clone https://github.com/Mohammad-Fazel-1991/network_analysis_application
```
## Running the Application:

**Option 1 - Using Docker:**
- Build Docker Image
```
docker build -t network_analysis_app .
```
- Run the Docker Image
 ```
docker run network_analysis_app
```   
**Option 2 - Using Shell Script:**

- Make the script executable and run it:
```
chmod +x run_pipeline.sh
./run_pipeline.sh
```   
