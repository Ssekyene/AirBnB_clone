#!/usr/bin/python3
"""
Module Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Inherits from BaseModel
    Public class attributes:
        city_id:             (str) will be City.id
        user_id:             (str) will be User.id
        name:                (str)
        description:         (str)
        number_rooms:        (int) 0
        number_bathrooms:    (int) 0
        max_guest:           (int) 0
        price_by_night:      (int) 0
        latitude:            (float) 0.0
        longitude:           (float) 0.0
        amenity_ids:         (list) will be Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: those inherited from BaseModel
        and those specific to Place
        """
        super().__init__()
        if kwargs and kwargs != []:
            try:
                self.city_id = kwargs["city_id"]
                self.user_id = kwargs["user_id"]
                self.name = kwargs["name"]
                self.description = kwargs["description"]
                self.number_rooms = kwargs["number_rooms"]
                self.number_bathrooms = kwargs["number_bathrooms"]
                self.max_guest = kwargs["max_guest"]
                self.price_by_night = kwargs["price_by_night"]
                self.latitude = kwargs["latitude"]
                self.longitude = kwargs["longitude"]
                self.amenity_ids = kwargs["amenity_ids"]
            except KeyError:
                pass
