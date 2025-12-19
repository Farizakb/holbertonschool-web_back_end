#!/usr/bin/env python3
""" Returns the list of schools having a specific topic """

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have the given topic in their 'topics' list.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for

    Returns:
        list of matching documents
    """
    return list(mongo_collection.find({"topics": topic}))
