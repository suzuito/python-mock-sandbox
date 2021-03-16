
from typing import Any, Coroutine


class Hello():
    def say(self, name: str) -> str:
        return f'Hello {name}'
    async def say_async(self, name: str) -> Coroutine[Any, Any, str]:
        return f'Hello {name}'

class Hoge():
    i: int = 0