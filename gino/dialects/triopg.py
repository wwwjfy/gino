from functools import partial

import asyncpg
import trio_asyncio
# from triopg._triopg import TrioConnectionProxy
import triopg

from . import base
from .asyncpg import AsyncpgDialect as ADialect


class Pool(base.Pool):
    def __init__(self, url, loop, **kwargs):
        self._url = url
        self._loop = loop
        self._kwargs = kwargs
        self._pool = None

    async def _init(self):
        args = self._kwargs.copy()
        args.update(
            loop=self._loop,
            host=self._url.host,
            port=self._url.port,
            user=self._url.username,
            database=self._url.database,
            password=self._url.password,
        )
        self._pool = await triopg.create_pool(**args)
        # self._pool = await trio_asyncio.run_asyncio(
        #     partial(asyncpg.create_pool, **args)
        # )
        return self

    def __await__(self):
        return self._init().__await__()

    @property
    def raw_pool(self):
        return self._pool

    async def acquire(self, *, timeout=None):
        # return TrioConnectionProxy(
        #     (await self._pool.acquire().__aenter__())._con)

        # @trio_asyncio.aio_as_trio
        # async def wrapper():
        #     return await self._pool.acquire().__aenter__()
        # return await wrapper()
        a = await self._pool.acquire().__aenter__()
        breakpoint()
        return a

    async def release(self, conn):
        pass
        # await conn.__aexit__()
        # await self._pool.release(conn_proxy._asyncpg_conn)

    async def close(self):
        await self._pool.close()


class TriopgDialect(ADialect):
    driver = 'triopg'

    async def init_pool(self, url, loop):
        return await Pool(url, loop, init=self.on_connect(),
                          **self._pool_kwargs)
