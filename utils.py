from functools import reduce
from typing import Union

def add(*args: Union[int, float]) -> int | float:
    return reduce(lambda a, b: a+b, args, 0)

def multiply(*args: Union[int, float]) -> int | float:
    return reduce(lambda a, b: a*b, args, 1)
