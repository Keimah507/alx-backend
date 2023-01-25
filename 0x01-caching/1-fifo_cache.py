#!/usr/bin/env python3
"""Task 1 fifo caching"""
BaseCaching = __import__('basic_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching"""
    def __init__(self) -> None:
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Assigns item of key value to dictionary"""
        if key or item is not None:
            self.cache_data[key] = item
        else:
            pass
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_remove = sorted(self.cache_data)[0]
            self.cache_data.pop(to_remove)
            print('DISCARD {}\n'.format(to_remove))

    def get(self, key):
        """Returns value in dictionary assigned to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
