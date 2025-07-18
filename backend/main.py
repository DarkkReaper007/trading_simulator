# backend/main.py

import asyncio
import json
import random
from collections import deque

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

price_history = []
timestamps = []
fast_window = 5
slow_window = 10

fast_queue = deque(maxlen=fast_window)
slow_queue = deque(maxlen=slow_window)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        price = round(random.uniform(100, 200), 2)
        price_history.append(price)

        fast_queue.append(price)
        slow_queue.append(price)

        sma_fast = round(sum(fast_queue) / len(fast_queue), 2) if len(fast_queue) == fast_window else None
        sma_slow = round(sum(slow_queue) / len(slow_queue), 2) if len(slow_queue) == slow_window else None

        data = {
            "price": price,
            "sma_fast": sma_fast,
            "sma_slow": sma_slow,
        }

        await websocket.send_text(json.dumps(data))
        await asyncio.sleep(1)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
