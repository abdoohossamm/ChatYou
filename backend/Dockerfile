FROM python:3.9
ENV PYTHONBUFFERED=1
RUN pip install --upgrade pip

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python manage.py migrate
