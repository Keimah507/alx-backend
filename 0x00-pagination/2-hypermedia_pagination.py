#!/usr/bin/env python3
"""Task 2 hypermedia pagination"""
import csv
import math
from typing import List
from typing import Tuple
from typing import Dict

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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        returns a dictionary containing the following key-value pairs:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        dataset_items = len(self.dataset())
        data = self.get_page(page, page_size)
        total_pages = math.ceil(dataset_items / page_size)

        res = {
            "page": page,
            "page_size": page_size,
            "data": data,
            "next_page": page + 1 if page + 1 < total_pages else None,
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": total_pages
        }
        return res

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size 2 containing a start index and an end index"""
    start = abs((page - 1) * page_size)
    end = page * page_size
    return (start, end)
