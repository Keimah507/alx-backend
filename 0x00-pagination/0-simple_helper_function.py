#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size 2 containing a start index and an end index"""
    start = abs((page - 1) * page_size)
    end = page * page_size
    return (start, end)
