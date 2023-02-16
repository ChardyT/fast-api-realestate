import aiohttp

class ExternalApiCallAiohttp():
    def __init__(self, url, headers, params):
        self.url = None
        self.headers = None
        self.params = None

    async def get(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            response = await session.get(self.url, params=self.params)
            return await response.json()

    async def post(self, data):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            response = await session.post(self.url, params=self.params, data=data)
            return await response.json()

    async def put(self, data):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            response = await session.put(self.url, params=self.params, data=data)
            return await response.json()

    async def delete(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            response = await session.delete(self.url, params=self.params)
            return await response.json()