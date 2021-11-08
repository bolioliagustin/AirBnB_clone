#!/usr/bin/python3
"""Base Model class"""


import uuid
import datetime


class BaseModel():
    """Base Model"""
    def __init__(self):
        self.id =  str(uuid.uuid4())
        self.created_at =  datetime.datetime.now()
        self.updated_at =  datetime.datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format (self.__class__.__name__, self.id, self.__dict__))
