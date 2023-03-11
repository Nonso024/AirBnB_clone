#!/usr/bin/python3
""" This module contains the entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage



def tokenize(arg: str) -> list:
    """ Splits a string into tokens delimeted by space

    Args:
        arg (string): strings to be splitted

    Returns:
        list: list of strings
    """
    token = re.split(r"[ .(),]", arg)
    return token



class HBNBCommand(cmd.Cmd):
    """ the command line entry point """

    prompt = "(hbnb) "
    CLASSNAMES = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }
    intro = 'Welcome to my console'
