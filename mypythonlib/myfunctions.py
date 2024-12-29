import asyncio
import json
from typing import Callable, Dict, List, Optional


class MessageQueue:
    def __init__(self):
        self.topics: Dict[str, List[Callable]] = {}  # Topic to subscriber mapping
        self.failed_messages: List[Dict] = []       # Retry queue

    def subscribe(self, topic: str, callback: Callable):
        """Subscribe to a topic with a callback."""
        if topic not in self.topics:
            self.topics[topic] = []
        self.topics[topic].append(callback)

    async def publish(self, topic: str, message: dict):
        """Publish a message to a topic."""
        if topic not in self.topics:
            print(f"No subscribers for topic: {topic}")
            return
        for callback in self.topics[topic]:
            try:
                await callback(message)
            except Exception as e:
                print(f"Error processing message: {e}")
                self.failed_messages.append({"topic": topic, "message": message})

    async def retry_failed_messages(self):
        """Retry processing failed messages."""
        #while self.failed_messages:
            #failed_message = self.failed_messages.pop(0)
            #await self.publish(failed_message["topic"], failed_message["message"])
        retry_queue = self.failed_messages.copy()
        self.failed_messages.clear()

        for topic, message in retry_queue:
            if topic in self.topics:
                for callback in self.topics[topic]:
                    try:
                        await callback(message)
                    except Exception:
                        print(f"Retry failed for message: {message}")
                        self.failed_messages.append((topic, message))



# Example callback function for subscribers
async def example_callback(message):
    print(f"Processing message: {message}")
    if "fail" in message:
        raise ValueError("Simulated failure")




