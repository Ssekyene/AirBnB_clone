#!/usr/bin/python3
from datetime import datetime as dt
from uuid import uuid4
import models


"""
Module BaseModel
Parent of all classes
"""


class BaseModel():
    """
    Base class for AirBnB clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        save(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: uuid4, time created/updated
        """
        if kwargs and kwargs != []:
            value = kwargs["created_at"]
            self.id = kwargs["id"]
            self.created_at = dt.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = self.created_at
        else:
            self.id = str(uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def __repr__(self):
        """
        returns string representation
        """
        return (self.__str__())

    def save(self):
        """
        Update istance with updated time $ save to serialized file
        """
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dict of class info and time in str
        """
        obj_dict = {}
        obj_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, (dt, )):
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        return obj_dict
