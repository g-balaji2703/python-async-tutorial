import asyncio

async def main():
    print('loading...')
    await asyncio.sleep(1)
    print('loading completed')

asyncio.run(main())