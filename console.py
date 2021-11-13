#!/usr/bin/python3
""" Console Airbnb"""


import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

props = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
         "Amenity": Amenity, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Prompt Project Airbnb"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        'Quit command to exit the program'
        exit()
        return True

    def do_EOF(self, line):
        'Quit command to exit the program'
        exit()
        return True

    def emptyline(self):
        "empty linneee"
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""
        str_list = line.split(" ")
        if str_list == 0:
            print("** class name missing **")
        if str_list[0] in props:
            new_instance = props[str_list[0]]()
            new_instance.save()
            print(new_instance.id)

        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the object representation of an instance
        based on the class name and id"""
        str_list = line.split(" ")
        if str_list == 0:
            print("** class name missing **")
        elif str_list[0] not in props:
            print("** class doesn't exist **")
        elif str_list[0] in props and len(str_list) == 1:
            print("** instance id missing **")
        if len(str_list) == 2:
            key = str_list[0] + "." + str_list[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        else:
            pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        str_list = line.split(" ")
        if str_list == 0:
            print("** class name missing **")
        elif str_list[0] not in props:
            print("** class doesn't exist **")
        elif str_list[0] in props and len(str_list) == 1:
            print("** instance id missing **")
        if len(str_list) == 2:
            key = str_list[0] + "." + str_list[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            pass

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        if line == "":
            for i in storage.all().values():
                print(i)
        else:
            str_list = line.split(" ")
            if str_list[0] not in props:
                print("** class doesn't exist **")
            elif len(str_list) == 1:
                for key, value in storage.all().items():
                    if str_list[0] in key:
                        print(str(value))

    def do_update(self, line):
        str_line = line.split(" ")
        if str_line == 0:
            print("** class name missing **")
        elif str_line[0] not in props:
            print("** class doesn't exist **")
        elif str_line[0] in props and len(str_line) == 1:
            print("** instance id missing **")
        elif str_line[0] in props and len(str_line) == 2:
            print("** attribute name missing **")
        elif str_line[0] in props and len(str_line) == 3:
            print("** value missing **")
        else:
            key = str_line[0] + "." + str_line[1]
            setattr(storage.all()[key], str_line[2], str_line[3])
            storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
