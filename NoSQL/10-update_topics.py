#!/usr/bin/env python3
"""
Module for changing topics of a school document in MongoDB.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of school documents based on the name.

    Args:
        mongo_collection: pymongo collection object
        name (string): school name to update
        topics (list of strings): new list of topics

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
