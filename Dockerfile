FROM python:3.10
WORKDIR /app

# Copy the current directory contents into the container at /app to build proj
COPY . /app

# Install flask and ansible-creator
RUN pip install flask ansible-creator

# Expose the port your service runs on
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=app.py

# Command to run your application
CMD ["flask", "run", "--host=0.0.0.0"]

# Define a health check to ensure the container is ready to serve traffic
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:5000/health || exit 1
