#!/usr/bin/python3
"""
Module Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel
    Public class attributes:
        place_id:            (str) will be Place.id
        user_id:             (str) will be User.id
        text:                (str)
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: those inherited from BaseModel
        and those specific to Review
        """
        super().__init__()
        if kwargs and kwargs != []:
            try:
                self.place_id = kwargs["place_id"]
                self.user_id = kwargs["user_id"]
                self.text = kwargs["text"]
            except KeyError:
                pass
