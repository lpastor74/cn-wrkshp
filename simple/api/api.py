import flask
from flask import request, jsonify, render_template
import mysql.connector
import requests
import json

mydb = mysql.connector.connect(
    host="mysql",
    user="api753",
    passwd="api753_secret",
    database="api_svc",
    port=3306
)

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Simple API</h1><p>available methods <ul><li><a href='/api/v1/resources/all'> All</a</li><li><a href='/api/v1/resources/user/1'> User1  </a></li></ul></p>"


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/all', methods=['GET'])
def api_all_v1():

    mycursor = mydb.cursor()
    query = "SELECT users.FirstName,users.LastName,resource.Name,resource.Value FROM  users inner join  resource where users.EXtID=resource.ExtID"

    mycursor.execute(query)
    myresult = mycursor.fetchall()

    return jsonify(myresult)


@app.route('/api/v1/resources/user', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    query = "SELECT users.FirstName, users.LastName FROM  users where  users.idUsers=%d " % int(
        id)

    query1 = "SELECT resource.Name,resource.Value FROM  users inner join  resource on users.ExtID=resource.ExtID where  users.idUsers=%d " % int(
        id)

    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    mycursor1 = mydb.cursor()
    mycursor1.execute(query1)
    myresult1 = mycursor.fetchall()

    result = {'data': myresult1, 'user': myresult}

    # result = {'user': myresult, 'date': [dict(zip(tuple(query.keys()), i))
    #                       for i in query.cursor]}
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(result)


@app.route('/api/v1/resources/user/<id>', methods=['GET'])
def api_id1(id):
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    # if 'id' in request.args:
    #    id = int(request.args['id'])
    # else:
    #    return "Error: No id field provided. Please specify an id."

    query = "SELECT  users.FirstName,users.LastName FROM users where users.idUsers=%d " % int(
        id)

    query1 = "SELECT resource.Name,resource.Value FROM users inner join resource on users.ExtID=resource.ExtID where users.idUsers=%d " % int(
        id)

    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    mycursor1 = mydb.cursor()
    mycursor1.execute(query1)
    myresult1 = mycursor.fetchall()

    result = {'data': myresult1, 'user': myresult}

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(result)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# app.run()
app.run(host="0.0.0.0", port=int("5000"), debug=True)
