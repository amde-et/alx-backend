#!/usr/bin/env python3

"""
Module 0-simple_helper_function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Takes two integer arguments page and page_size.
    Returns a tuple of size two containing a start
    index and an end index corresponding to the range
    of indexes to return in a list for those particular
    pagination parameters.
    """
    index_tuple = page_size * (page - 1), page * page_size
    return index_tuple
