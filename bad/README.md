# Cloud Native application - workshop
# Bad - solution

Solution covers next step in cloud native envolvement.
It is 'Ugly' solution with WSO2 APIM, IS as KM and API Analitics.

Python API solution is same
Python APP solution is integrated with IS to provide sign in option.
Note: 
- You need to change ClientID & Client Secret in py_app.py line 16-17 to mach to your API definition.
- MicroGateWay need to be init, imoprt and rebuld in order to mach to your API created in APIPublisher

example command to build micro gateway (on Mac)
./micro-gw init <project_name>
./micro-gw init get_user_mgw

micro-gw import -a <API_name> -v <version> <project_name>
./micro-gw import -a getuser -v 0.0.1 get_user_mgw

micro-gw build <project-name>
./micro-gw build get_user_mgw

