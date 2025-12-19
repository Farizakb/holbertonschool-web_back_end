#!/usr/bin/env python3
""" Changes all topics of a school document based on its name """

def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of a school document in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object
        name (str): name of the school to update
        topics (list): list of topics to set

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
