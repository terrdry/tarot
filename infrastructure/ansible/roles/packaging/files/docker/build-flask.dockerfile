# Use the official Python image as the base image
FROM python:3.13-alpine AS payload

# Update system packages to reduce vulnerabilities
RUN apk update && apk upgrade
# RUN apt-get install --no-interactive gcc build-essential libffi-dev
RUN apk add --no-cache bash
WORKDIR /app

# Copy requirements and install dependencies
# COPY . ./backend
# RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Flask application (including subfolders)
COPY backend/. .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
# CMD ["tail", "-f", "/dev/null"]
