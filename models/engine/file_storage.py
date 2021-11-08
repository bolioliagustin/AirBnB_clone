#!/usr/bin/python3
""" Storage Json"""

class FileStorage:
    __file_path = file.json
    __objects = {}

    def all(self):
        return (self.__objects)

    def new(self, obj):
    __objects = type(obj).id
