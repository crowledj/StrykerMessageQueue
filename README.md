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

project-root/
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



How to setup, install and run the publish & subscribe services, use the asynchronous Message queue and their tests.


1) A virtual python environment is setup using the 'venv' python- pip tool.

2) A custom library containing the Message Queue class was built and installed in 'mypythonlib'. This was so that it could be imported in to the Fast API service's code. 




