#!/usr/bin/env python3
"""Task 5 LFU caching system"""
from basic_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching system"""
    def __init__(self):
        self.counter = 0
        self.ages = {}
        self.used = {}
        super().__init__()

    def count_used(self, key):
        """Increases key by 1 if it exists"""
        if key in self.used:
            self.used[key] += 1
        else:
            self.used[key] = 1

    def put(self, key, item):
        """Assign item linked to key to dict cache_data"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_used = min(self.used.values())
                for k, _ in sorted(self.ages.items(),
                                   key=lambda x: x[1]):
                    if self.used[k] == least_used:
                        self.cache_data.pop(k)
                        self.ages.pop(k)
                        self.used.pop(k)
                        break
                    print('Discard {}'.format(k))
            self.ages[key] = self.counter
            self.counter += 1
            self.count_used(key)

    def get(self, key):
        """Returns value in dictionary assigned to key"""
        if key and key in self.cache_data:
            self.ages[key] = self.counter
            self.counter += 1
            self.count_used(key)
            return self.cache_data[key]
        return None
