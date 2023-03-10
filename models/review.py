#!/usr/bin/python3
""" This module contains a class that inherits from BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """ a class that inherits from BaseModel """

    place_id = ""
    user_ide = ""
    text = ""
