import asyncio
import pytest
from fastapi.testclient import TestClient
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
from main import app

mq = MessageQueue()

# Create a TestClient instance
client = TestClient(app)

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

@pytest.mark.asyncio
async def test_subscribe_to_topic():
    """Test subscribing to a topic with a valid callback."""
    async def callback(message):
        return f"Processed: {message}"

    mq.subscribe("test_topic", callback)
    assert "test_topic" in mq.topics
    assert callback in mq.topics["test_topic"]


@pytest.mark.asyncio
async def test_publish_to_subscribed_topic():
    """Test publishing a message to a subscribed topic."""
    received_messages = []

    async def callback(message):
        received_messages.append(message)

    mq.subscribe("test_topic", callback)
    await mq.publish("test_topic", {"key": "value"})

    # Allow the callback to process
    await asyncio.sleep(0.1)
    assert received_messages == [{"key": "value"}]

@pytest.mark.asyncio
async def test_publish_to_unsubscribed_topic():
    """Test publishing a message to a topic with no subscribers."""
    # Ensure the topic has no subscribers
    assert "unsubscribed_topic" not in mq.topics

    # Publishing should not raise an error
    await mq.publish("unsubscribed_topic", {"key": "value"})
    # Check that no callbacks were invoked
    assert mq.topics.get("unsubscribed_topic") is None


