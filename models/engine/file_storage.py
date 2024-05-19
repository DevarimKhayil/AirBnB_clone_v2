#!/usr/bin/python3
"""
Defines the FileStorage class.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage."""
        if cls is None:
            return FileStorage.__objects
        else:
            return {key: value for key, value in FileStorage.__objects.items() if isinstance(value, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary."""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file."""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = eval(val['__class__'])(**val)
        except FileNotFoundError:
            pass

    def close(self):
        """Call reload method for deserializing the JSON file to objects."""
        self.reload()

