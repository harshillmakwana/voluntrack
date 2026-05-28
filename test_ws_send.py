import asyncio
import websockets
import json

async def test_ws_send():
    uri = "ws://127.0.0.1:4521/ws/chat/"
    try:
        # We can't easily authenticate via websockets script without cookies,
        # but earlier we accepted anonymous temporarily! Wait, I put it back.
        pass
    except Exception as e:
        print(e)
