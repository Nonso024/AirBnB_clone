#!/usr/bin/python3
""" This module contains a class City thats inherits from BaseModel """

from models.base_model import BaseModel


class City(BaseModel):
    """ A class that inherits from BaseModel """

    state_id = ""
    name = ""
