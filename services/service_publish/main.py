from fastapi import FastAPI
import sys
import asyncio
sys.path.append('../../')
from mypythonlib.myfunctions import MessageQueue # Import my custom library

app = FastAPI()
mq = MessageQueue()

@app.post("/publish/")
async def publish_message(topic: str, message: dict):
    """API endpoint to publish a message."""
    await mq.publish(topic, message)
    return {"status": "Message published"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
