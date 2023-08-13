#Link : https://www.educative.io/answers/how-to-create-an-asyncio-task

import asyncio

async def my_task(task_name,seconds):
    """
    This is an example coroutine thats takes a name and a snumebr of seconds as input ans waits for that many seconds before returning a message
    """
    print(f"{task_name} started")
    await asyncio.sleep(seconds) # This simulates some work being done.
    print(f"{task_name} finished")
    return f"{task_name} completed in {seconds} seconds"

async def main():
    """
    This is the main coroutine that creates and runs several subtasks in parallel.
    """
    # create a list of tasks to run concurrently
    tasks = [
        asyncio.create_task(my_task("task_1",15)),
        asyncio.create_task(my_task("task_2",10)),
        asyncio.create_task(my_task("task_3",8)),
    ]

    #wait for all task to complete and retrieve their results
    results = await asyncio.gather(*tasks)
    print(results)

# Run the main coroutine in the asyncio event loop
asyncio.run(main())