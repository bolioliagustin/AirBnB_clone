#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize Amenity """
        super().__init__(self, *args, **kwargs)
