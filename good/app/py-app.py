from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, g
import requests
import json
import os

app = Flask(__name__)


@app.route('/')
def hello_whale():
    res = requests.get('https://favqs.com/api/qotd')
    y = json.loads(res.text)
    author = y['quote']['author']
    body = y['quote']['body']

    return render_template('index.html', athr=author, bdy=body)


@app.route('/apicall/<id>', methods=['GET'])
def api_call(id):

    auth_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik5UQXhabU14TkRNeVpEZzNNVFUxWkdNME16RXpPREpoWldJNE5ETmxaRFUxT0dGa05qRmlNUSJ9.eyJhdWQiOiJodHRwOlwvXC9vcmcud3NvMi5hcGltZ3RcL2dhdGV3YXkiLCJzdWIiOiJhZG1pbiIsImFwcGxpY2F0aW9uIjp7ImlkIjo1LCJuYW1lIjoiand0X2d3IiwidGllciI6IjEwUGVyTWluIiwib3duZXIiOiJhZG1pbiJ9LCJzY29wZSI6ImFtX2FwcGxpY2F0aW9uX3Njb3BlIGRlZmF1bHQiLCJpc3MiOiJodHRwczpcL1wvbG9jYWxob3N0Ojk0NDVcL29hdXRoMlwvdG9rZW4iLCJrZXl0eXBlIjoiUFJPRFVDVElPTiIsInN1YnNjcmliZWRBUElzIjpbeyJuYW1lIjoiZ2V0X3VzZXIiLCJjb250ZXh0IjoiXC9yZXNvdXJjZXNcLzAuMC4xIiwidmVyc2lvbiI6IjAuMC4xIiwicHVibGlzaGVyIjoiYWRtaW4iLCJzdWJzY3JpcHRpb25UaWVyIjoiQnJvbnplIiwic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciJ9LHsibmFtZSI6IlRvRG8iLCJjb250ZXh0IjoiXC9kZW1vXC8xLjAiLCJ2ZXJzaW9uIjoiMS4wIiwicHVibGlzaGVyIjoiYWRtaW4iLCJzdWJzY3JpcHRpb25UaWVyIjoiVW5saW1pdGVkIiwic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciJ9XSwiY29uc3VtZXJLZXkiOiJqVUhRTGtnN2ZHeV9xTGFaQWV2Rlc4ck13cG9hIiwiZXhwIjozNzE4MTU5NTk1LCJpYXQiOjE1NzA2NzU5NDg1MzYsImp0aSI6ImVlM2VlY2JmLTgzOTMtNDgzNS05MDg0LTE1YjQyMjgyNzBhYiJ9.PZAQxqorxwnJEYsiykVsqYQYFx-1UNmADI08_heWKb-UB79adQNzNkifNO9wqH-4elrBAwyGMbbDNnu9Tk3vICdlWw92r2gUztzr9HvTMERvdwgEa6LZ4ZmeyDNUJKJ1GF2IGUKj5nFyDL9R_35CJBL9dCWYZ2qncqQE0QchbCtT9tV-S2yCs3nHjLzVbcC5Ka0D3VvcHu68tsMKij2elPQWk8Sk_zvbR6PPDuYbZdj3uxsepNZ2twvIOHeEQvLOhtWagX5t2J_k5Voroo2fT3OodZuaScJbKHeuVPEjykPKiYJpPTf8iDHEM6qbsnTkk09t8dDJud23Ky-_TiAzaw=='
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {'app': 'aaaaa'}

    url = 'http://gw-user:9090/resources/0.0.1/user/%d' % int(id)
    res = requests.get(url, headers=hed)

    y = json.loads(res.text)
    data = y['data']
    user = y['user']

    return render_template('api.html', athr=user, bdy=data)


#os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

if __name__ == '__main__':
    app.run(debug=True, port=int("5055"), host='0.0.0.0')
