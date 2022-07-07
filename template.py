import asyncio
import websockets

import warnings

warnings.filterwarnings("ignore")


class websocketClass:
    ruleSets = [
        ["example data", "example return"],
        ["example data 2", "example return 2"],
        ["example data 3", "example return 2"],
    ]

    def consoleOut(data):
        print(f" > {data}")

    def dataHandler(data):
        for i in range(0, len(websocketClass.ruleSets)):
            if data == websocketClass.ruleSets[i][0]:
                return websocketClass.ruleSets[i][1]


def main():
    def startWebsocket(port, keepAlive=True, consoleOut=True):
        async def websocketHandler(websocket, path):
            if keepAlive:
                while True:
                    incomingData = await websocket.recv()
                    if consoleOut:
                        websocketClass.consoleOut(incomingData)
                    await websocket.send(websocketClass.dataHandler(incomingData))
            else:
                incomingData = await websocket.recv()
                if consoleOut:
                    websocketClass.consoleOut(incomingData)

        startServer = websockets.serve(websocketHandler, "localhost", port)
        asyncio.get_event_loop().run_until_complete(startServer)
        asyncio.get_event_loop().run_forever()

    startWebsocket(8000)


if __name__ == "__main__":
    main()
