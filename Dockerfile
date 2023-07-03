# Base image
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /code/

# Copy static and media files
COPY static /code/static/
COPY media /code/media/

# Install Nginx and copy configuration
RUN apt-get update && \
    apt-get install -y nginx && \
    rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/

# Expose port
EXPOSE 80

# Run Django with Gunicorn and Nginx
CMD /etc/init.d/nginx start && gunicorn --bind 0.0.0.0:8000 config.wsgi:application
