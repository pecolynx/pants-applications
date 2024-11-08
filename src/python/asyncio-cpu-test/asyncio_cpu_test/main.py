print("hello")



import asyncio
import logging

from logging import getLogger


import aiohttp
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
import time


logger = getLogger(__name__)
async def cpu_sleep(sec: int)-> None:
    time.sleep(sec)


async def gql_request() -> str:
    client_session_args = {"timeout": aiohttp.ClientTimeout(total=5)}
    transport = AIOHTTPTransport(
        url="http://localhost:8000/grqphql",
        client_session_args=client_session_args,
    )
    query = gql("query task { user { name } }")
    async with Client(
        transport=transport, fetch_schema_from_transport=False
    ) as session:
        data = await session.execute(query)
        return data["user"]["name"]

async def main():
    f = []
    for i in range(20):
        f.append(cpu_sleep(3))
        f.append(gql_request())
    results = await asyncio.gather(*f)
    print(results)

logging.basicConfig()
asyncio.run(main())
