# Get base image
FROM python:3.7

WORKDIR /usr/src/apitests

# Install all dependencies
COPY requirements.txt /usr/src/apitests/
RUN pip install --no-cache-dir -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org --user

COPY . /usr/src/apitests/

CMD bash

