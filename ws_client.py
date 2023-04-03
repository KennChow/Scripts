import asyncio
import websockets

async def send_message(msg):
    # 当连接关闭时，async with 语句块会自动关闭 WebSocket 连接
    async with websockets.connect("ws://localhost:8888") as websocket:
        await websocket.send(msg)  # 使用 await 等待连接建立完成
        # message = await websocket.recv()
        # print("Message received from server:", message)
if __name__ == '__main__':
    asyncio.run(send_message(str(23533)))
# websockets.colse()
