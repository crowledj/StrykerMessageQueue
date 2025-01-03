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


In this structure:

The shared_libs/ directory can be shared across services.

**********************************************************************************************

How to setup, install and run the publish & subscribe services, use the asynchronous Message queue and their tests.


1) A virtual python environment is setup using the 'venv' python- pip tool.

2) A custom library containing the Message Queue class was built and installed in 'mypythonlib'. This was so that it could be imported in to the Fast API service's code. 

The python version for the virtual environment is 

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



