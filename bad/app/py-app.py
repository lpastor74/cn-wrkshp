import os

import flask
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, g
import requests
import json
from urllib.parse import urlencode

import requests
'''
from oauthlib.oauth2 import BackendApplicationClient
from oauthlib.oauth2.rfc6749.errors import (AccessDeniedError,
                                            InvalidClientError,
                                            MissingTokenError)
                                            '''
from requests_oauthlib import OAuth2Session


import requests
# from bottle import route, redirect, request, response, template, run


app = flask.Flask(__name__)

# py-application
app.config['WSO2_ID'] = "vR6hVPGPTDPMlsC0dsvfLAfmmZMa"
app.config['WSO2_SECRET'] = "mjyVSgp9Z1deueOV9953IZNMT0sa"
app.debug = True
app.secret_key = 'development'
authorization_base_url = 'https://localhost:9445/oauth2/authorize'
token_url = 'http://is-as-km:9765/oauth2/token'
redirect_uri = 'http://py.com:5055/callback'
scope = ['openid']


@app.route("/login")
def login():
    wso2 = OAuth2Session(app.config.get('WSO2_ID'),
                         redirect_uri=redirect_uri, scope=scope)
    authorization_url, state = wso2.authorization_url(authorization_base_url)

    # authorization_redirect_url = authorization_base_url + '?response_type=code&client_id=' + app.config.get('WSO2_ID') + '&redirect_uri=' + redirect_uri + '&scope=openid'

    # State is used to prevent CSRF, keep this for later.
    app.logger.error(' TESTING ---- connection Idp')
    session['oauth_state'] = state
    return redirect(authorization_url)


def authFailure():
    """ Authentication failure --> 401 """
    # response = make_response(render_template(
    #    'error.html'), msg=401, txt='not authorized')
    # return response
    return render_template('error.html', msg=401, txt='not authorized')
    # return Response("Authentication failed!", 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


@app.route("/callback")
def callback():
    # wso2 = OAuth2Session(app.config.get('WSO2_ID'),
    #                     state=session['oauth_state'])
    # token = wso2.fetch_token(token_url, client_secret=app.config.get('WSO2_SECRET'),
    #                         authorization_response=request.url)
    app.logger.error(' TESTING ---- connection Idp')

    if not request.args.get('code'):
        return authFailure()
    params = {
        'grant_type': 'authorization_code',
        'code': request.args.get('code'),
        'client_id': app.config.get('WSO2_ID'),
        'client_secret': app.config.get('WSO2_SECRET'),
        'redirect_uri': 'http://py.com:5055/callback'
    }
    url = token_url
    r = requests.post(url, data=params)
    if r.status_code != 200:
        error_msg = 'Failed to get access token with error {}'.format(
            r.status_code)
        return error_msg
    else:
        data = r.json()
        session['accs_tkn'] = data.get('access_token')
        session['rfsh_tkn'] = data.get('refresh_token')
        session['scope'] = data.get('scope')
        session['id_tkn'] = data.get('id_token')
        session['user'] = 'true'

        resp = make_response(render_template('index.html',
                                             athr=session['accs_tkn'], bdy=session['rfsh_tkn']))
        resp.set_cookie('accs_tkn', data.get('access_token'),
                        max_age=data.get('expires_in'))
        resp.set_cookie('rfsh_tkn', '3')

        temp = "access token"

        body = data.get('access_token')

    # return resp
    return render_template('profile.html', athr='access_token', bdy=body)


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/profile')
def profile():
    if g.user:
        return render_template('profile.html')

    return redirect(url_for('index'))


"""
 ******************
 Old code from simple app
 ******************
"""


@app.route('/')
def hello_whale():
    '''res = requests.get('http://py-api:5000/api/v1/resources/all')
    y = json.loads(res.text)
    data = y['data']
    user = y['user']'''

    '''res = requests.get('https://favqs.com/api/qotd')
    y = json.loads(res.text)
    author = y['quote']['author']
    body = y['quote']['body']'''

    author = "hello"
    body = " world"

    return render_template('index.html', athr=author, bdy=body)


@app.route('/apicall/<id>', methods=['GET'])
def api_call(id):
    ''' micro gateway call '''
    '''auth_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik5UQXhabU14TkRNeVpEZzNNVFUxWkdNME16RXpPREpoWldJNE5ETmxaRFUxT0dGa05qRmlNUSJ9.eyJhdWQiOiJodHRwOlwvXC9vcmcud3NvMi5hcGltZ3RcL2dhdGV3YXkiLCJzdWIiOiJhZG1pbiIsImFwcGxpY2F0aW9uIjp7ImlkIjo1LCJuYW1lIjoiand0X2d3IiwidGllciI6IjEwUGVyTWluIiwib3duZXIiOiJhZG1pbiJ9LCJzY29wZSI6ImFtX2FwcGxpY2F0aW9uX3Njb3BlIGRlZmF1bHQiLCJpc3MiOiJodHRwczpcL1wvbG9jYWxob3N0Ojk0NDVcL29hdXRoMlwvdG9rZW4iLCJrZXl0eXBlIjoiUFJPRFVDVElPTiIsInN1YnNjcmliZWRBUElzIjpbeyJuYW1lIjoiZ2V0X3VzZXIiLCJjb250ZXh0IjoiXC9yZXNvdXJjZXNcLzAuMC4xIiwidmVyc2lvbiI6IjAuMC4xIiwicHVibGlzaGVyIjoiYWRtaW4iLCJzdWJzY3JpcHRpb25UaWVyIjoiQnJvbnplIiwic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciJ9LHsibmFtZSI6IlRvRG8iLCJjb250ZXh0IjoiXC9kZW1vXC8xLjAiLCJ2ZXJzaW9uIjoiMS4wIiwicHVibGlzaGVyIjoiYWRtaW4iLCJzdWJzY3JpcHRpb25UaWVyIjoiVW5saW1pdGVkIiwic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciJ9XSwiY29uc3VtZXJLZXkiOiJqVUhRTGtnN2ZHeV9xTGFaQWV2Rlc4ck13cG9hIiwiZXhwIjozNzE4MTU5NTk1LCJpYXQiOjE1NzA2NzU5NDg1MzYsImp0aSI6ImVlM2VlY2JmLTgzOTMtNDgzNS05MDg0LTE1YjQyMjgyNzBhYiJ9.PZAQxqorxwnJEYsiykVsqYQYFx-1UNmADI08_heWKb-UB79adQNzNkifNO9wqH-4elrBAwyGMbbDNnu9Tk3vICdlWw92r2gUztzr9HvTMERvdwgEa6LZ4ZmeyDNUJKJ1GF2IGUKj5nFyDL9R_35CJBL9dCWYZ2qncqQE0QchbCtT9tV-S2yCs3nHjLzVbcC5Ka0D3VvcHu68tsMKij2elPQWk8Sk_zvbR6PPDuYbZdj3uxsepNZ2twvIOHeEQvLOhtWagX5t2J_k5Voroo2fT3OodZuaScJbKHeuVPEjykPKiYJpPTf8iDHEM6qbsnTkk09t8dDJud23Ky-_TiAzaw=='
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {'app': 'demo'}

    url = 'http://gw-user:9090/resources/0.0.1/user/%d' % int(id)
    res = requests.get(url, headers=hed)'''

    ''' OAuth call '''
    auth_token = session['accs_tkn']
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {'app': 'demo'}

    url = 'http://py-api:5000/api/v1/resources/user/%d' % int(id)
    res = requests.get(url, headers=hed)

    #res = requests.get('http://py-api:5000/api/v1/resources/user/%d' % int(id))
    y = json.loads(res.text)
    data = y['data']
    user = y['user']

    return render_template('api.html', athr=user, bdy=data)


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

if __name__ == '__main__':
    app.run(debug=True, port=int("5115"), host='0.0.0.0')
