#!/usr/bin/python3
""" test for Base Model"""
from models.base_model import BaseModel
from datetime import datetime
import unittest
my_model = BaseModel()
my_model.name = "My Model Pro"
my_model.my_number = 49
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
          my_model_json[key]))
