import asyncio
import pytest
from httpx import AsyncClient
import sys
#Allow tests to be run from various location in the directory
sys.path.append('.')
sys.path.append('../')
sys.path.append('../../')
sys.path.append('services/service_subscribe/')
sys.path.append('services/service_publish/')
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


