import asyncio
import websockets

from ws_client import send_message

asyncio.run(send_message(str(128)))

