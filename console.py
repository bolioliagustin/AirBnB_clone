#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Prompt Project Airbnb"""
    prompt = "(hbnb) "
if __name__ == '__main__':
    HBNBCommand().cmdloop()
