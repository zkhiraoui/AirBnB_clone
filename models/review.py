#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    place_id = ""  # It will be the Place.id
    user_id = ""  # It will be the User.id
    text = ""
