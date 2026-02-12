# Using ubuntu as base image 
FROM ubuntu:latest

# Changing the workdir to /app
WORKDIR /app

#Copying the current directory contents to /app
COPY . /app

#Install the necessary packages and python
RUN apt-get update && apt-get install -y python3 python3-pip

#Run command to start the application
CMD [ "python3", "app.py"]
