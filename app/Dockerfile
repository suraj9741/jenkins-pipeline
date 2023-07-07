FROM python:3.10-slim-buster

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECDE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y libpq-dev python3-dev g++ make && rm -rf /var/lib/apt/lists/*


RUN mkdir /koko-assignment
WORKDIR /koko-assignment

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /koko-assignment/requirements.txt

COPY . .

CMD ["gunicorn",  "--bind", "0.0.0.0:5000", "app:app"]