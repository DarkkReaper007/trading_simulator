import asyncio
import json
import time
import random
import aio_pika

async def send_price():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    await channel.declare_queue("price_updates", durable=True)

    symbol = "AAPL"
    price = 100

    while True:
        price += random.uniform(-1, 1)
        payload = {
            "symbol": symbol,
            "price": round(price, 2),
            "timestamp": time.time()
        }
        await channel.default_exchange.publish(
            aio_pika.Message(body=json.dumps(payload).encode()),
            routing_key="price_updates"
        )
        print("Sent:", payload)
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(send_price())
