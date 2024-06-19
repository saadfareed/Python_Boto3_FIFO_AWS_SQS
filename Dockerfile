# We Use an official Python runtime as a parent image
FROM python:3.8-slim

WORKDIR /externalinterfacingapi

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=external_interfacing_backend.settings

# RUN Server
CMD python manage.py runserver 127.0.0.1:7000
# Expose port 7000 to the outside world
EXPOSE 7000
