#!/usr/bin/env python3
"""Task 4 MRU caching system"""
BaseCaching = __import__('basic_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching system"""

    def __init__(self) -> None:
        self.cache_data = {}
        self.ages = {}
        self.counter = 0
        super().__init__()

    def put(self, key, item):
        """Assign item linked to key to dict cache_data"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_remove = sorted(self.ages.items(),
                                   key=lambda x: x[1], reverse=True)[0][0]
                self.cache_data.pop(to_remove)
                self.ages.pop(to_remove)
                print('Discard {}'.format(to_remove))

            self.ages[key] = self.counter
            self.counter += 1

    def get(self, key):
        """Returns value in dictionary assigned to key"""
        if key and key in self.cache_data:
            self.ages[key] = self.counter
            self.counter += 1
            return self.cache_data.get(key)
        return None
