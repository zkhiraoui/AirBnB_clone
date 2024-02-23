import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from json.decoder import JSONDecodeError

class FileStorage:
    """File storage engine for the AirBnB clone"""

    def __init__(self):
        """Initializes FileStorage"""
        self.file_path = "file.json"
        self.objects = {}

    def all(self):
        """Returns the dictionary objects"""
        return self.objects

    def new(self, obj):
        """Sets in self.objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.file_path, "w") as f:
            objects = {k: v.to_dict() for k, v in self.objects.items()}
            json.dump(objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.file_path, "r") as f:
                objects = json.load(f)
                for obj_id, obj_dict in objects.items():
                    cls_name = obj_dict["__class__"]
                    del obj_dict["__class__"]
                    if cls_name == "BaseModel":
                        self.objects[obj_id] = BaseModel(**obj_dict)
                    elif cls_name == "User":
                        self.objects[obj_id] = User(**obj_dict)
                    elif cls_name == "State":
                        self.objects[obj_id] = State(**obj_dict)
                    elif cls_name == "City":
                        self.objects[obj_id] = City(**obj_dict)
                    elif cls_name == "Amenity":
                        self.objects[obj_id] = Amenity(**obj_dict)
                    elif cls_name == "Place":
                        self.objects[obj_id] = Place(**obj_dict)
                    elif cls_name == "Review":
                        self.objects[obj_id] = Review(**obj_dict)
        except FileNotFoundError:
            pass
        except JSONDecodeError:
            pass
