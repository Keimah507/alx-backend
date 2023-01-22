#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size 2 containing a start index and an end index"""
    start = abs((page - 1) * page_size)
    end = page * page_size
    return (start, end)


res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)
