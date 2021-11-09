#!/usr/bin/python3
""" Console Airbnb"""
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
