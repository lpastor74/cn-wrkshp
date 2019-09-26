from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, g
import requests
import json

app = Flask(__name__)


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
