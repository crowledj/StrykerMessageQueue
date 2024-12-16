from fastapi import FastAPI
import asyncio
from message_queue import MessageQueue  # Import the custom library

app = FastAPI()
mq = MessageQueue()

@app.post("/publish/")
async def publish_message(topic: str, message: dict):
    """API endpoint to publish a message."""
    await mq.publish(topic, message)
    return {"status": "Message published"}

