from websockets import connect
import asyncio
import json
import random

## This script requires the websockets library
## sudo pacman -S python-websockets or pip install websockets

uri = "ws://localhost:4455"

async def main():
    async with connect(uri) as ws:
        hello = json.loads(await ws.recv())
        print("Hello:", hello)

        identify_req = {
            "op": 1,
            "d": {
                "rpcVersion": 1,
                "authentication": "",
                "eventSubscriptions": 0,
                "ToggleReplayBuffer": False
            }
        }
        await ws.send(json.dumps(identify_req))

        replay_req = {
            "op": 6,
            "d": {
                "requestType": "ToggleReplayBuffer",
                "requestId": random.randint(1, 1000),
                "requestData": "ToggleReplayBuffer"
            }
        }
        await ws.send(json.dumps(replay_req))


asyncio.run(main())