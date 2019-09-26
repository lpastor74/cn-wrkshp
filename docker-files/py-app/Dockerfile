FROM ubuntu:latest
WORKDIR /app
ADD . .
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["py-app.py"]