#!/usr/bin/python3
"""
    This module contains a class FileStorage that serializes
    instances to JSON file and deserilizes JSON file to instances
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

        json_dict = {key: value.to_dict()
                     for key, value in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(json_dict))

        def reload(self):
            """ deserializes json file to __objects """
            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review

            model_dict = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review
                    }

            try:
                with open(FileStorage.__file_path, "r") as f:
                    json_dict = json.loads(f.read())
                    FileStorage.__objects = {}

                    for key, value in json_dict.items():
                        if value["__class__"] in model_dict:
                            cls = model_dict[value["__class__"]]
                            obj = cls(**value)
                            FileStorage.__objects[key] = obj
            except FileNotFoundError:
                pass
