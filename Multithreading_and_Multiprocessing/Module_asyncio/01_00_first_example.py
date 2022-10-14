import asyncio
import time

from Multithreading_and_Multiprocessing.Module_threading.decorators import measure_time, async_measure_time


async def tick():
    print('Tick')
    # ставим await, щоб виклик був асинхронним і код,
    # який стоїть після await продовжив виконуватися
    await asyncio.sleep(1)  # time.sleep(1)
    print('Tock')


# @measure_time
@async_measure_time
async def main():
    await asyncio.gather(tick(), tick(), tick())
    # for _ in range(3):
    #     tick()


if __name__ == "__main__":
    asyncio.run(main())

# Tick
# Tock
# Tick
# Tock
# Tick
# Tock - вивід синхронного коду за 3.01 секунди
# async ставим, щоб код був coroutine. await використовується
# для асинхронного очікування результату від виконання coroutine і наступний код після асинхронного виклику корутину
# після асинхронного виклику await буде виконаний після того, яку запущений корутін завершить своє виконання
