#!/usr/bin/python3
"""
Module State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Inherits from BaseModel
    Public class attribute:
        name: (str)
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: those inherited from BaseModel
        and those specific to State
        """
        super().__init__()
        if kwargs and kwargs != []:
            try:
                self.name = kwargs["name"]
            except KeyError:
                pass
