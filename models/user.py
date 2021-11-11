#!/usr/bin/python3


from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize class User"""
        super().__init__(**kwargs)
