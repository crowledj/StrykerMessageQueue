from fastapi import FastAPI, WebSocket
import asyncio
import sys
sys.path.append('../')
from mypythonlib.myfunctions import MessageQueue # Import my custom library


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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
