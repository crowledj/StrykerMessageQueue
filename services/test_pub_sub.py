import pytest
import asyncio
import pytest_asyncio
import sys
sys.path.append('../')
import mypythonlib
from mypythonlib.myfunctions import MessageQueue

@pytest.mark.asyncio
async def test_publish_and_subscribe():

    print("In first test")
    mq = MessageQueue()
    received_messages = []

    async def test_callback(message):
        received_messages.append(message)

    mq.subscribe("test_topic", test_callback)
    await mq.publish("test_topic", {"content": "Test message"})

    assert received_messages == [{"content": "Test message"}]

@pytest.mark.asyncio
async def test_failed_message_retry():
    print("In 2nd test")
    mq = MessageQueue()
    received_messages = []

    async def failing_callback(message):
        raise ValueError("Intentional failure")

    async def successful_callback(message):
        received_messages.append(message)

    mq.subscribe("test_topic", failing_callback)
    mq.subscribe("test_topic", successful_callback)
    
    print("Publishing message...")
    await mq.publish("test_topic", {"content": "Will fail"})
    print("Done Publishing message...")
    
    print("retrying failed message...")
    await mq.retry_failed_messages()
    print("Done retrying failed message...")

    assert len(received_messages) == 1
    assert received_messages[0] == {"content": "Will fail"}


#test_publish_and_subscribe()

#test_failed_message_retry()
