FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y default-jre
RUN apt-get install -y python3-pip python-dev build-essential

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5001

CMD ["python3", "app.py"]