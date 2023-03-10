#!/usr/bin/python3
"""
    This module contains a class FileStorage that serializes instances to JSON file
    and deserilizes JSON file to instances
"""
import json


class FileStorage:
    """ A class that serializes and deserializes instances to json """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """

        return FileStorage.__objects

    def new(self):
        """ sets an object in __objects """

        key = "{} {}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to json file """

        json_dict = {key: value.to_dict() for key, value in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumpd(json_dict))
