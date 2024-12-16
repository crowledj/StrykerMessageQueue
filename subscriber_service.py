from fastapi import FastAPI, WebSocket
import asyncio
from message_queue import MessageQueue  # Import the custom library

app = FastAPI()
mq = MessageQueue()

@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # Subscribe a WebSocket to a topic
    async def websocket_callback(message):
        await websocket.send_text(json.dumps(message))

    mq.subscribe("topic1", websocket_callback)

@app.on_event("startup")
async def startup_event():
    # Simulate processing of messages
    async def process_message(message):
        print(f"Consumed message: {message}")

    mq.subscribe("topic1", process_message)

