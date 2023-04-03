# import asyncio     # 异步I/O
# import websockets

# async def echo(websocket):
#     async for message in websocket:
#         await websocket.send(message+"哈哈哈");
#
# async def main():
#     async with websockets.serve(echo, "localhost", 8888):
#         await asyncio.Future();
#
# asyncio.run(main())

# websocket_server.py

import asyncio
import websockets

# 创建一个列表，用于存储所有 WebSocket 连接的对象
websocket_connections = []

async def handle_connection(websocket, path):
    # 将新连接的 WebSocket 对象添加到列表中
    websocket_connections.append(websocket)

    # websocket.send("欢迎使用Websocket!")
    async for message in websocket:
        print("Message received from client:", message)
        # for conn in websocket_connections:
        #     print(conn)
        #     await conn.send(message)
        await websocket_connections[0].send(message)


async def start_server():
    async with websockets.serve(handle_connection, "localhost", 8888):
        print("Python WebSocket server started!")
        await asyncio.Future()  # run forever
if __name__ == '__main__':
    asyncio.run(start_server())

