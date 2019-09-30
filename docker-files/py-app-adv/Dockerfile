FROM python:3.7-alpine

WORKDIR /app
ADD . .
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install  -r requirements.txt
RUN pip install oauthlib

ENTRYPOINT [ "python" ]
CMD [ "py-app.py" ]