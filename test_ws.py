import asyncio
import websockets
import sys

async def test_ws():
    uri = "ws://127.0.0.1:4521/ws/chat/"
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected successfully!")
            await websocket.close()
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_ws())
