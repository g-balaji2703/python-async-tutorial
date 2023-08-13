import asyncio

async def fetch_data():
    print('start fetching data')
    await asyncio.sleep(2)
    print('done fetching data')
    return {'data':1}

async def print_number():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_number())
    val = await task1
    print(val)
    await task2
asyncio.run(main())









