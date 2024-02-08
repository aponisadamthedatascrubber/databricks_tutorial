import asyncio
import random
import time

async def my_task_2():
    try:
        sleep_time = round(random.random()*10)
        print(f'sleep time: {sleep_time}')
        time.sleep(sleep_time)
        return 'TASK COMPLETE!'
    except asyncio.CancelledError:
        return 'TASK CANCELLED!'

async def my_task_3():
    try:
        sleep_time = random.random()*10
        print(f'sleep time: {sleep_time}')
        time.sleep(sleep_time)
    except asyncio.CancelledError:
        return "Task was cancelled"

async def my_task():
    try:
        await my_task_3()
        await my_task_3()
        return "Task completed successfully"
    except asyncio.CancelledError:
        return "Task was cancelled"
        
async def run_with_timeout(function, timeout):
    try:
        result = await asyncio.wait_for(function, timeout)
        return result
    except asyncio.TimeoutError:
        return None
        
async def main():
    while True:
        start_time = time.time()
        timeout = 5
        
        result = await run_with_timeout(function=my_task_3(), timeout=timeout)
        print(result)
        print(f'Total duration {time.time()-start_time}')


asyncio.run(main())