# micro gateway
more info you can fing on https://docs.wso2.com/display/MG301/About+WSO2+API+Microgateway

- download the binary 


position you r self in desired folder and run
micro-gw init <project_name>
example : ./micro-gw init get_user_mgw

import API definition (APIM need to running and API need to be in published status)
micro-gw import -a <API_name> -v <version> <project_name>
example : ./micro-gw import -a getuser -v 0.0.1 get_user_mgw

build a project in order to get file with .balx extension
micro-gw build <project-name>
example : ./micro-gw build get_user_mgw

for solutons 'good' and 'better' fbalx file is in gw folder. Docker image will get this during startup.
Docker image used is wso2/wso2micro-gw:3.0.1





# License
py-app code is distributed under Apache license 2.0.