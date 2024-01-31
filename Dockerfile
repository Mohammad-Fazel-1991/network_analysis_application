# Using the official Python base image
FROM python:3.7.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script, data file, and requirements
COPY network_analysis.py .
COPY 686.edges .
COPY requirements.txt .

# Install packages from requirements file
RUN pip install -r requirements.txt

# Command to run the script
CMD ["python", "./network_analysis.py"]


