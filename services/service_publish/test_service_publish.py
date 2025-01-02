import asyncio
from fastapi.testclient import TestClient
import pytest
from httpx import AsyncClient
import sys
sys.path.append('../../')
sys.path.append('../')
import mypythonlib
from mypythonlib.myfunctions import MessageQueue # Import my custom library
import main
from main import app
import json
mq = MessageQueue()

# Create a TestClient instance
client = TestClient(app)

def test_publish_message():
    # Define the message to publish
    
    topic = "test_topic"
    message = {"key": "value"}

    # Send the topic as a query parameter and message as JSON
    response = client.post(f"/publish/?topic={topic}", json=message)

    # Send the message to the /publish/ endpoint
    #response = client.post("/publish/", json=message)
    
    # Assert the response status code is 200
    assert response.status_code == 200
    
    # Assert the response payload matches the expected output
    assert response.json() == {"status": "Message published"}

#@pytest.mark.asyncio
#async def test_publish_message():
#    """Test the publish API endpoint for asynchronous messaging."""
    # Use TestClient to simulate HTTP requests
#    client = TestClient(app)

    # Define the topic and message
#   topic = "test_topic"
#    message = {"key": "value"}

    # Send a POST request to the /publish/ endpoint
#    response = client.post(
#        "/publish/",
#        json={"topic": topic, "message": message},
#    )

    # Assertions to verify the response
#    assert response.status_code == 200
#    assert response.json() == {"status": "Message published"}

#if __name__ == "__main__":
#    pytest.main(["-v"])



