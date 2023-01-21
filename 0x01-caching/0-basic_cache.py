#!/usr/bin/python3
"""
Module 0-basic_cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Overrides put() nad self()
    from parent
    """

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        value = self.cache_data.get(key)
        return value
