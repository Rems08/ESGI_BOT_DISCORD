FROM python:3.9.12
WORKDIR /ESGI_BOT
RUN apt-get install gcc
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD python3 main.py