FROM python:3.7-alpine

WORKDIR /app
ADD . .
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install  -r requirements.txt

ENV FLASK_APP app.py
EXPOSE 5000
CMD ["python","./api.py"]