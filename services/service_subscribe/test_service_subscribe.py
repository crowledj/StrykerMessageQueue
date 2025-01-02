import asyncio
import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
import sys
sys.path.append('../')
sys.path.append('../../')
from service_publish.main import app
import mypythonlib
from mypythonlib.myfunctions import MessageQueue
from typing import Callable


mq = MessageQueue()

@pytest.mark.asyncio
async def test_message_processing():
    processed_messages = []

    # Override the default process_message to capture messages
    async def mock_process_message(message):
        processed_messages.append(message)

    # Subscribe the mock callback to the topic
    mq.subscribe("topic1", mock_process_message)

    # Publish a message to the queue
    await mq.publish("topic1", {"content": "Test message"})

    # Give some time for the message to be processed
    await asyncio.sleep(0.1)

    # Verify the message was processed
    assert processed_messages == [{"content": "Test message"}]


#@pytest.mark.asyncio
#async def test_consume_message_from_queue():
#    mq = MessageQueue()

    # Add a message to the queue
#    await mq.publish("test_topic", {"content": "Message for B"})

    # Simulate Service B consuming the message
    #sync with AsyncClient(base_url="http://testserver",app=app) as client:
    #    response = await client.get("/consume")

#    with TestClient(app) as client:
#        response = client.get("/startup")

#    assert response.status_code == 200
#    assert response.json() == {"detail": "Message processed"}
