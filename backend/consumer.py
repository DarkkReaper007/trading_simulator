import asyncio
import json
import time
from aio_pika import connect_robust, IncomingMessage
from collections import deque
import websockets

# Strategy Parameters
SMA_FAST = 3
SMA_SLOW = 5

# In-memory cache
price_queue = deque(maxlen=SMA_SLOW)
clients = set()

# Helpers
def calculate_sma(prices, window):
    if len(prices) < window:
        return None
    return round(sum(list(prices)[-window:]) / window, 2)

async def broadcast(data: dict):
    disconnected = set()
    for client in clients:
        try:
            await client.send(json.dumps(data))
        except:
            disconnected.add(client)
    clients.difference_update(disconnected)

async def handle_message(message: IncomingMessage):
    async with message.process():
        payload = json.loads(message.body.decode())
        price = payload.get("price")
        symbol = payload.get("symbol")
        timestamp = payload.get("timestamp", time.time())

        price_queue.append(price)
        sma_fast = calculate_sma(price_queue, SMA_FAST)
        sma_slow = calculate_sma(price_queue, SMA_SLOW)

        processed = {
            "timestamp": timestamp,
            "price": price,
            "sma_fast": sma_fast,
            "sma_slow": sma_slow,
            "symbol": symbol
        }

        print("Processed:", processed)
        await broadcast(processed)

async def consume():
    connection = await connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    queue = await channel.declare_queue("price_updates", durable=True)
    await queue.consume(handle_message)

async def websocket_server():
    async def handler(websocket):
        clients.add(websocket)
        try:
            await websocket.wait_closed()
        finally:
            clients.remove(websocket)

    print("WebSocket server started on ws://0.0.0.0:8765")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

async def main():
    await asyncio.gather(consume(), websocket_server())

if __name__ == "__main__":
    print("Consumer started...")
    asyncio.run(main())
