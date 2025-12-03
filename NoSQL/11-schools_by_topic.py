#!/usr/bin/env python3
"""
Module for retrieving schools by a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of school documents that have a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic (string): topic to search for

    Returns:
        List of needed documents
    """
    return list(mongo_collection.find({"topics": topic}))
