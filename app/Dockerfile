# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app1

# Copy the current directory into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip3 install flask

# Make port 80 available to the world outside this container
EXPOSE 8080

# Run the app using the python image when the container launches
CMD ["python", "app.py"]
