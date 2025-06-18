# Use the official Python image as the base image
FROM python:3.13-alpine AS payload

# Update system packages to reduce vulnerabilities
RUN apk update && apk upgrade
# RUN apt-get install --no-interactive gcc build-essential libffi-dev

WORKDIR /app

# Copy requirements and install dependencies
# ADD requirements.txt /app/requirements.txt

COPY ./backend/. /app/
RUN pip install --no-cache-dir -r requirements.txt

# # Copy the entire Flask application (including subfolders)
# COPY . /app

EXPOSE 5001

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
#  CMD ["python", "-c", "while 1: import ctypes; ctypes.CDLL(None).pause()"]
# CMD ["tail", "-f", "/dev/null"]
