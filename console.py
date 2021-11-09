#!/usr/bin/python3
""" Console Airbnb"""
import cmd
import sys
from models.base_model import BaseModel

props = {"BaseModel": BaseModel}

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
    
    def do_create(self,line):
        """Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id."""
        str_list = line.split(" ")
        if str_list == 0:
            print("** class name missing **")
        if str_list[0] in props and len(str_list) == 1:
            new_obj = props[str_list[0]]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")
    
    def do_show(self, line):
        """Prints the string representation of an instance 
        based on the class name and id"""
        str_list = line.split(" ")
        if str_list != 0:
            if str_list[0] in props and str_list[1] in props[id]:
                print(self.__str__(props[str_list[0]]))
            if str_list[0] not in props:
                print("*** class doesn't exist ***")
            if str_list[1] not in props[id]:
                print("*** instance id missing ***")           
        else:
            print("*** class name missing ***")
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
