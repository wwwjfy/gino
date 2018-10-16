from functools import partial

import asyncpg
import trio_asyncio
import triopg


async def main():
   pool = await trio_asyncio.run_asyncio(partial(
       asyncpg.create_pool, database='gino'
   ))
   a = await pool.acquire().__aenter__()
   breakpoint()
   print()
    # pool = await triopg.create_pool(database='gino')
    # async with pool.acquire() as conn:
    #     breakpoint()
    #     print()


trio_asyncio.run(main)
