from asyncio import Future
from python_mock_sandbox.mod2 import Hello, Hoge

from .mod1 import hello, hello_async

def main1():
    print(f"Yo {hello('Kenshiro')}")

async def main1_async():
    print(f"Yo {await hello_async('Kenshiro')}")

def main2():
    h = Hello()
    print(f"Yo {h.say('Kenshiro')}")

async def main2_async():
    h = Hello()
    print(f"Yo {await h.say_async('Kenshiro')}")

def main3():
    h = Hoge()
    print(f"Hoge i={h.i}")