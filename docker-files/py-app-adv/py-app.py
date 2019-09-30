from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, g
import requests
import json

from urllib.parse import urlencode

import requests
from oauthlib.oauth2 import BackendApplicationClient
from oauthlib.oauth2.rfc6749.errors import (AccessDeniedError,
                                            InvalidClientError,
                                            MissingTokenError)
from requests_oauthlib import OAuth2Session

app = Flask(__name__)

app.config['WSO2_ID'] = "3mFfNIiAbVpIiUOpVY9V9bHEZhIa"
app.config['WSO2_SECRET'] = "whlwDc74o8GwPNMfwufkvl4UWaEa"
app.debug = True
app.secret_key = 'development'
authorization_base_url = 'https://localhost:9445/oauth2/authorize'
token_url = 'http://localhost:9765/oauth2/token'
redirect_uri = 'http://py.com:5055/apicall/callback'
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
        'redirect_uri': 'http://py.com:5005/callback'
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

    # return resp
    return redirect(url_for('profile'))


def authFailure():
    """ Authentication failure --> 401 """
    # response = make_response(render_template(
    #    'error.html'), msg=401, txt='not authorized')
    # return response
    return render_template('error.html', msg=401, txt='not authorized')
    # return Response("Authentication failed!", 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


"""
 ******************
 Old code from simple app
 ******************
"""


@app.route('/')
def hello_whale():
    #auth = request.cookies.get('accs_tkn')
    res = requests.get('https://favqs.com/api/qotd')
    y = json.loads(res.text)
    author = y['quote']['author']
    body = y['quote']['body']

    return render_template('index.html', athr=author, bdy=body)


@app.route('/apicall')
def api_call():
    #auth = request.cookies.get('accs_tkn')
    res = requests.get('http://py-api:5000/api/v1/resources/user/1')
    y = json.loads(res.text)
    data = y['data']
    user = y['user']

    return render_template('api.html', athr=user, bdy=data)


if __name__ == '__main__':
    app.run(debug=True, port=int("5024"), host='0.0.0.0')
