import asyncio

async def produce(q: asyncio.Queue) -> None:
        a = 1
        await q.put((a))

async def consume(q: asyncio.Queue) -> None:
    while True:
        a = await q.get()
        print(a)
        q.task_done()

async def main():
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(q)) for n in range(3)]
    consumers = [asyncio.create_task(consume(q)) for n in range(3)]
    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers, too
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    asyncio.run(main())
