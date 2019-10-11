FROM python:3.7-alpine

LABEL maintainer="Laslo Pastor <laslo@wso2.com>"

RUN apk add --no-cache gcc musl-dev linux-headers

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install requests_oauthlib 
RUN pip install Flask-OAuthlib
RUN pip install oauthlib

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "py-app.py" ]