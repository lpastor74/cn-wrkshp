## Cloud Native application - workshop

Python API url :
http://localhost:5000

Python app url :
http://localhost:5000

Change: In solution there is micro-gateway 'gw-user'- no direct communication between application and API.
Python application calling API trought micro-gateway using JWT token.

Note: Update you JWT token accordingly. Only 10 call per minute is allowed (request will be throttled out afterwards). For demo pupose the application connected with micro-gateway 'gw-user' on http 9090 port.

