#!/usr/bin/python3
""" Storage Json"""

import json


class FileStorage():
    def __init__(self):
        self.__file_path = file.json
        self.__objects = {}


    def all(self):
        return (self.__objects)

    def new(self, obj):
        n = str(obj.__class__.__name__) + "." + str(obj.id)



    def save(self):
        with open(file.json,"w") as f:
            save_json = json.dumps(self.__objects)
            return f.write(save_json)

