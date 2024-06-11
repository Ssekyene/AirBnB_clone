#!/usr/bin/python3
"""
class User
"""

from models.base_model import BaseModel

class User(BaseModel):
    '''base model class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: those inherited from BaseModel
        and those specific to User
        """
        super().__init__()
        if kwargs and kwargs != []:
            try: 
                self.email = kwargs["email"]
                self.password = kwargs["password"]
                self.first_name = kwargs["first_name"]
                self.last_name = kwargs["last_name"]
            except KeyError:
                pass
            
