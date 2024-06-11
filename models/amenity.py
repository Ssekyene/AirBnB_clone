#!/usr/bin/python3
"""
Module Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherits from BaseModel
    Public class attribute:
        name: (str)
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: those inherited from BaseModel
        and those specific to Amenity
        """
        super().__init__()
        if kwargs and kwargs != []:
            try:
                self.name = kwargs["name"]
            except KeyError:
                pass
