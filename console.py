#!/usr/bin/python3
""" Console Airbnb"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models import storage

props = {"BaseModel": BaseModel, "User": User}


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

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""
        str_list = line.split(" ")
        if str_list == 0:
            print("** class name missing **")
        if str_list[0] == "BaseModel":
            new_instance = BaseModel()
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

        if str_line[0] is not in props:
            print("** class doesn't exist **")
        if (len(str_list)) == 0:
            print ("** class name missing **")
        if (len(str_list)) == 1:
            print ("** no instance found **")
        if(len(str_list)) == 2:
            print ("")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
