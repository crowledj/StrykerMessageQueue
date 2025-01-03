1. Message Queue Library
Key Components:
Publish/Subscribe: Clients can publish messages to a topic and subscribe to topics of interest.
Message Filtering: Subscribers can filter messages based on criteria.
Retries and Exception Handling: Messages are retried on failure.
WebSocket Delivery: Support for delivering messages to WebSocket clients.



2. FastAPI Microservices
Service A (Publisher):
Publishes messages to the queue.
Service B (Consumer):
Consumes messages and processes them.
Includes WebSocket support for delivering messages to the front end.


Directory Structure :

project-root/  (asycnmsglib)
│
├── message_queue_lib/  ('mypythonlib')
│   ├── __init__.py
│   ├── message_queue.py
│   ├── setup.py
│
├── service_publish/
│   ├── main.py
│   ├── requirements.txt
    ├── test_service_publish.py 
│
├── service_subscribe/
│   ├── main.py
│   ├── websocket_manager.py
│   ├── requirements.txt
├   ├── test_service_subscribe.py 
│
└── run_all.sh          # Bash script to run everything


******************************
Explanation of the Structure
******************************

1. mypythonlib/ (the message_queue_lib)
Purpose: Contains the reusable Message Queue Library. This keeps the library modular and independent.
Key Files:
message_queue.py: Implements the core logic (publish, subscribe, retries, etc.).

tests/: Contains unit tests specifically for the library.
2. service_publish/
Purpose: Represents Service A, which publishes messages to the queue.
Key Files:
main.py: Entry point for the FastAPI app.
requirements.txt: Contains only the dependencies Service A needs (e.g., fastapi, httpx).
Dockerfile: Defines how to containerize Service A.
test_service_publish: Contains unit and integration tests specific to the publish Service .
3. service_subscribe/
Purpose: Represents Service B, which consumes messages and supports WebSocket delivery.
Key Files:
main.py: Entry point for the FastAPI app.
websocket_manager.py: A utility for managing WebSocket connections and delivery.
requirements.txt: Contains only the dependencies Service B needs.
test_service_subscribe: Contains unit and integration tests specific to this Service .

6. README.md
Purpose: Provides documentation on the project setup, installation, structure, and usage.


**********************************************************************************************

How to setup, install and run the publish & subscribe services, use the asynchronous Message queue and their tests.

**********************************************************************************************


The root folder bash script "run_all.sh" will set up, build/install everything required for the project including checking that the two services can run .

THis script can be run by just enabling it to be executed by the user and running it using ,

                chmod +x ./run_all.sh

                ./run_all.sh

Inside this script , the follwing happens - 

1) A virtual python environment is setup using the 'venv' python- pip tool.

2) A custom library containing the Message Queue class was built and installed in 'mypythonlib'. This was so that it could be imported in to the Fast API service's code. 

3) The dependencies - libraries needed to install for the project to work are done using pip and a requirements.txt file.

4) Both the publish and subscribe services are started and checked that they are running properly 

- this is all printed to the screen for the user , including any errors in the process.

The python version for the virtual environment is :
$ python --version

Python 3.12.5

packages/dependencies required :

$ pip list
Package           Version
----------------- ----------
annotated-types   0.7.0
anyio             4.7.0
certifi           2024.12.14
click             8.1.7
colorama          0.4.6
fastapi           0.115.6
h11               0.14.0
httpcore          1.0.7
httpx             0.28.1
idna              3.10
iniconfig         2.0.0
mypythonlib       0.1.0
packaging         24.2
pip               24.2
pluggy            1.5.0
pydantic          2.10.3
pydantic_core     2.27.1
pytest            8.3.4
pytest-asyncio    0.25.0
setuptools        75.6.0
sniffio           1.3.1
starlette         0.41.3
typing_extensions 4.12.2
uvicorn           0.34.0


But running a "pip install -r ./requirements.txt" in the asyncmsglib folder should install all the required pacakages to use the Message queue library and the Fast API services.


###########################
############################
    Running the tests :
############################
##########################


There are unit tests for the Message Queue in 'test_myfunctions.py'

Run this by moving to its directory in 'asyncmsglib/mypythonlib/tests/' and simply do a 

'pytest ./test_myfunctions'


there are also individual units tests for both of the FASTAPI services, thesed can be run from either the base directory 
or their owd directories - '/services/servce_publish/' and '/services/servce_subscribe/' again using pytest as above.


