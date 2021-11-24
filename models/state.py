#!/usr/bin/python3
""" Initialize State class """


from models.base_model import BaseModel


class State(BaseModel):
    """ Class State """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize State """
        super().__init__(self, *args, **kwargs)
