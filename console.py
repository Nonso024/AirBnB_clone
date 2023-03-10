#!/usr/bin/python3
""" This module contains the entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
from models.user import User



class HBNBCommand(cmd.Cmd):
    """ the command line entry point """

    prompt = "(hbnb) "
    models = {
            "BaseModel": BaseModel,
            "User": User,

            }

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()

