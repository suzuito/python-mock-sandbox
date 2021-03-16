
import asyncio


def async_return(result) -> asyncio.Future:
    f = asyncio.Future()
    f.set_result(result)
    return f
