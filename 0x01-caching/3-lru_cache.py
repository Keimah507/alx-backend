#!/usr/bin/env python3
"""Task 3 LRU caching system"""
from typing import Any

BaseCaching = __import__('basic_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching system"""

    def __init__(self):
        self.ages = {}
        self.counter = 0
        self.cache_data = {}
        super().__init__()

    def put(self, key, item):
        """Assign item linked to key to dict cache_data"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_remove = sorted(self.ages.items(),
                                   key=lambda x: x[1])[0][0]
                self.cache_data.pop(to_remove)
                self.ages.pop(to_remove)
                print('Discard {}'.format(to_remove))

            self.ages[key] = self.counter
            self.counter += 1

    def get(self, key: Any):
        """Returns value in dictionary assigned to items"""
        if key and key in self.cache_data:
            self.ages[key] = self.counter
            self.counter += 1
            return self.cache_data.get(key)
        return None
