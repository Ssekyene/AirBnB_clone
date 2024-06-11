#!/usr/bin/python3
"""
Module City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from BaseModel
    Public class attributes:
        state_id: (str) will be State.id
        name:     (str)
    """
    state_id = ""
    name = ""
       
    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: those inherited from BaseModel
        and those specific to City
        """
        super().__init__()
        if kwargs and kwargs != []:
            try:
                self.state_id = kwargs["state_id"]
                self.name = kwargs["name"]
            except KeyError:
                pass
