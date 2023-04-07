#!/usr/bin/python3
""" 4. MRU Caching
"""
from datetime import datetime
from collections import defaultdict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ BaseCache defines:
      - overwrite functions 'put' and 'get' for implement
      MRU caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_by_time = {}
        self.cache_by_frequency_use = defaultdict(int)  # >>> Default value: 0

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item
        value for the key key
        If the number of items in self.cache_data is higher
        that BaseCaching.MAX_ITEMS:
        - must discard the most recently used item (MRU algorithm)
        - must print DISCARD: with the key discarded and following by
        a new line
        """
        if key and item:
            self.cache_by_time[key] = datetime.now()
            self.cache_data[key] = item
            self.cache_by_frequency_use[key] += 1

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Sorted elements by frequency_used
                frequency_use_filtered = {}
                for k, v in self.cache_by_frequency_use.items():
                    if k != key:
                        frequency_use_filtered[k] = v
                keys_by_frequency_used = sorted(frequency_use_filtered,
                                                key=frequency_use_filtered.get)
                key_to_delete = keys_by_frequency_used[0]

                # There are more elements with same frequency used count?
                count = frequency_use_filtered[key_to_delete]
                posibles_elements_to_discard_dict = {}
                for k, v in frequency_use_filtered.items():
                    if v == count:
                        posibles_elements_to_discard_dict[k] = v
                if len(posibles_elements_to_discard_dict) > 1:
                    elements_to_discard_by_time = {}
                    for k, v in self.cache_by_time.items():
                        if k in posibles_elements_to_discard_dict.keys():
                            elements_to_discard_by_time[k] = v

                    elements_by_time = sorted(
                                          elements_to_discard_by_time,
                                          key=elements_to_discard_by_time.get)
                    key_to_delete = elements_by_time[0]

                # Delete element with least_frequency_used
                del self.cache_by_time[key_to_delete]
                del self.cache_data[key_to_delete]
                del self.cache_by_frequency_use[key_to_delete]
                print('DISCARD: {}'.format(key_to_delete))

    def get(self, key):
        """
            Return the value in self.cache_data linked to key
        """
        element = self.cache_data.get(key)
        if element:
            self.cache_by_time[key] = datetime.now()
            self.cache_by_frequency_use[key] += 1
        return element
