#!/usr/bin/env python3
"""Task 1 Simple pagination"""
import csv
import math
from typing import List
from typing import Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Finds the correct indexes to paginate the dataset correctly 
        and return the appropriate age of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        range_d = index_range(page, page_size)
        server = Server()
        s = range_d[0]
        e = range_d[1]
        if e > len(server.dataset()):
            return []
        return (server.dataset()[s: e])

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size 2 containing a start index and an end index"""
    start = abs((page - 1) * page_size)
    end = page * page_size
    return (start, end)
