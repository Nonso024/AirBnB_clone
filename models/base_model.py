#!/usr/bin/python3
"""
    This module contains a BaseModel class that defines all
    common attributes and methods for other classes
"""

import uuid
from models import storage
from datetime import datetime


class BaseModel():

    """
        Base class for all other sub classes.
        Defines all common attributes and methods for subclasses
    """

    def __init__(self, *args, **kwargs):
        """initializes self"""

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            storage.new(self)

    def __str__(self):
        """returns the string representation of the instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the instance attribute updated_at with current time"""

        self.updated_at = datetime.now()

        storage.save

    def to_dict(self):
        """returns a dictionary containing all key values of dict"""

        dict_copy = self.__dict__.copy
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat
        dict_copy["updated_at"] = self.updated_at.isoformat
        return dict_copy
    
