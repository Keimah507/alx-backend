#!/usr/bin/env python3
"""Task 2 lifo cache"""
BaseCaching = __import__('basic_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""
    def __init__(self):
        super().__init__()
        self.last_put = ""
        self.cache_data = {}

    def put(self, key, item):
        """Assigns item of key value to dictionary"""
        if key or item is not None:
            self.cache_data[key] = item
        else:
            pass
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print('Discard {}\n'.format(self.last_put))
            self.cache_data.pop(self.last_put)
        if key:
            self.last_put = key

    def get(self, key):
        """Returns value in dictionary assigned to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
