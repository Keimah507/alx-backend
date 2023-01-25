#!/usr/bin/env python3
"""Task 0 basic cache"""
BaseCaching = __import__('basic_caching').BaseCaching


class BasicCache(BaseCaching):
    """Caching system"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Assigns item of key value to cache_data"""
        if key or item is not None:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """return value in cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
