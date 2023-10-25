#!/usr/bin/python3
"""  basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class that inherits from BaseCaching and is a caching system
        this caching system doesn’t have limit """
    def put(self, key, item):
        """ assign to the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value linked """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
