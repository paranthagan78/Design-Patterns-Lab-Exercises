import asyncio
import time

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    
    start = time.time()
    asyncio.run(main())
    end=time.time()
    elapsed = end-start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

#sync operation

import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for i in range(3):
        count()

if __name__ == "__main__":
    s = time.time()
    main()
    elapsed = time.time() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
