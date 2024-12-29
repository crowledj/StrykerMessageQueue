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





