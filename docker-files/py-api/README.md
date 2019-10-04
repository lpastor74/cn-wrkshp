# python REST web service  
Python REST application 

Read data from MySQL DataBase


Available calls : 
- /api/v1/resources/user?id=<id>
Retruns individual user with realted data 
(example:/api/v1/resources/user?id=1)
- /api/v1/resources/user/<id>
Retruns individual user with realted data
Retruns individual user with realted data 
(example:/api/v1/resources/user/1)
- /api/v1/resources/all
Retruns all users with related data 

#Requerments
Need access to DataBase 
(in code connection is established with MySQL DB on default port 3306)
    host="mysql",
    user="api753",
    passwd="api753_secret",
    database="api_svc",

to build a docker image run the following command 
docker build --tag [name:version] .
example 
docker build --tag py-api:0.1 .

this image will hold pyhton web api that is exposed on port 5000

# License
py-app code is distributed under Apache license 2.0.



