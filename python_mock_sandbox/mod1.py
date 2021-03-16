
from typing import Any, Coroutine


def hello(name: str) -> str:
    return f'Hello {name}'

async def hello_async(name: str) -> Coroutine[Any, Any, str]:
    return f'Hello {name}'