
import asyncio

loop = asyncio.new_event_loop()

def async_return(result) -> asyncio.Future:
    f = asyncio.Future(loop=loop)
    f.set_result(result)
    return f
