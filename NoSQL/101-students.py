#!/usr/bin/env python3
"""Module for top_students function"""


def top_students(mongo_collection):
    """Find all top score students"""
    return mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {
                    '$avg': "$topics.score"
                }
            }
        },
        {
            '$sort': {
                "averageScore": -1
            }
        }
    ])
