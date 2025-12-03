#!/usr/bin/env python3
"""This module defines the function that adds a new document in the base of kwargs in Python"""
def insert_school(mongo_collection, **kwargs):
    """
    Adds a new document based on kwargs
    Arguments:
        mongo_collection: An object for pymongo collection.
        **kwargs: Any key word arguments that are included like a document.
    Returns: New _id value of an included document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
