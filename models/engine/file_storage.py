#!/usr/bin/python3
""" Storage Json"""


from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
import json

props = {"BaseModel": BaseModel, "User": User,"State": State, "City": City, "Amenity": Amenity, "Review": Review}


class FileStorage():
    """ Storage Json """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """return objects"""
        return (self.__objects)

    def new(self, obj):
        """add object to __objects"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """save to JSON file"""
        dic_json = {}
        for key, value in self.__objects.items():
            dic_json[key] = value.to_dict()
            with open(self.__file_path, 'w') as f:
                json.dump(dic_json, f)

    def reload(self):
        """Deserialize the JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                jso = json.load(f)
                for key, value in jso.items():
                    splitt = key.split('.')[0]
                    self.__objects[key] = props[splitt](**value)
        except:
            pass
