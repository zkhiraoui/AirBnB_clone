#!/usr/bin/python3
"""
BaseModel module: Defines the BaseModel class that serves as the base class
for all other classes in this project.
"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Defines the BaseModel class. This class will be the base class for all other
    classes in the project. It includes common methods and attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance's __dict__.
        This method will be the first step in the serialization of an instance to
        a dictionary representation.
        Includes the class name under key '__class__'.
        Converts 'created_at' and 'updated_at' to string objects in ISO format.
        """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = dict_rep['created_at'].isoformat()
        dict_rep['updated_at'] = dict_rep['updated_at'].isoformat()
        return dict_rep
