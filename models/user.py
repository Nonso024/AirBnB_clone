#!/usr/bin/python3
""" This module contains a class User thats inherits from BaseModel """

from models.base_model import BaseModel


class User(Basemodel):
    """ a class User thats takes in user credentials """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
